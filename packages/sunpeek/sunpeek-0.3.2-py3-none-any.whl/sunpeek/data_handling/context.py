"""
This module implements data access and data handling.

The Context class implements 2 data backends: database and dataframe.
- Database is e.g. for use over WebUI, DataFrame for use as a package and for testing.
A sensor cache is implemented to speed up database access times.
- To quickly add csv data / test something, just do: use_csv(plant, [file_list])

Internally, data is always stored without unit (double / float64); the correct unit (stored in sensor.native_unit)
is attached at data access.
"""

import numpy as np
import enum
import datetime
import warnings
from typing import Union, Dict
from dataclasses import dataclass
import pandas as pd
import datetime
import pytz
from pydantic import validator

from sunpeek.common.utils import sp_logger
from sunpeek.base_model import BaseModel
from sunpeek.db_utils import DATETIME_COL_NAME
from sunpeek.common.errors import ConfigurationError, CalculationError, TimeZoneError
from sunpeek.common.time_zone import validate_timezone
import sunpeek.core_methods.virtuals as virtuals
import parquet_datastore_utils as pu


class NanReportResponse(BaseModel):
    nan_report: Union[Dict[str, str], None]

    @validator('nan_report', pre=True)
    def df_to_val(cls, dct):
        if dct is not None:
            return {k: v.to_json(date_format='iso') for k, v in dct.items() if not isinstance(v, str)}


def import_db_ops():
    """
    Imports the db_data_operations module and raises a specific error if any of the required modules is missing.
    This is used because some functions in this module only need the db modules imported when using the database backend
    """
    try:
        import sunpeek.db_utils.db_data_operations as db_ops
        return db_ops
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Some modules that a required to work with the database backend are not installed. "
                                  "They can be installed with pip install sunpeek[db].")


def sanitize_dataframe(df: pd.DataFrame) -> (pd.DataFrame, int):
    if df is None:
        return None, 0

    df = df[~df.index.isna()]
    # Some core methods require data to be sorted (e.g. PC Method extended -> rolling operation)
    df = df.sort_index()
    # Check for duplicate indices
    index_duplicates = df.index.duplicated(keep=False)
    n_duplicates_index = index_duplicates.sum()
    df = df[~index_duplicates]

    return df, n_duplicates_index


class Context:
    class Datasources(str, enum.Enum):
        pq = "pq"
        parquet = "parquet"  # stored as 'pq'
        df = "df"
        dataframe = "dataframe"  # stored as 'df'

    VALID_DATASOURCES = [el.value for el in Datasources]

    @dataclass
    class EvalInterval:
        start: datetime.date
        end: datetime.date

        def __post_init__(self):
            if self.start is None:
                self.start = pd.to_datetime('1970-01-01 00:00', utc=True)
            if self.end is None:
                self.end = pd.to_datetime('2200-01-01 00:00', utc=True)
            # validate start, end
            for x in (self.start, self.end):
                if not isinstance(x, datetime.date):
                    raise TypeError('Context limits expected to be of type datetime.')
                if x.tzinfo is None:
                    raise TimeZoneError(
                        "Both elements of a Context eval_interval tuple must be timezone-aware datetime objects.")
            if self.end <= self.start:
                raise ValueError('A Context eval_interval must have increasing timestamps: end must be greater than '
                                 'start.')

    # Cannot add plant type hint because of circular imports.

    def __init__(self, plant,
                 datasource: str = None,
                 dataframe: pd.DataFrame = None,
                 df_timezone: str = None,
                 eval_start: datetime.date = None,
                 eval_end: datetime.date = None,
                 raw_data_path: str = None,
                 calc_data_path: str = None,
                 ):
        if plant is None:
            raise ConfigurationError('Context parameter "plant" must not be None.')
        self.plant = plant
        self._df = None
        self._sensor_cache = {}
        self._eval_interval = None
        self.set_eval_interval(eval_start, eval_end)
        self.session = None

        if datasource is None and dataframe is not None:
            datasource = 'df'
        self.datasource = datasource
        if self.datasource == 'df':
            self.session = None
            self.use_dataframe(dataframe, timezone=df_timezone)

        elif self.datasource == 'pq':
            if dataframe is not None:
                raise ConfigurationError('You are trying to set a context datasource to "pq" but also provided a '
                                         'DataFrame. This is ambiguous.')

    @classmethod
    def validate_datasource(cls, val):
        """Validates datasource string and returns either 'df' or 'db'.

        Raises
        ------
        ValueError
        """
        if (val is not None) and val.lower() not in [s.lower() for s in cls.VALID_DATASOURCES]:
            raise ValueError(f'Context.datasource must be one of {cls.VALID_DATASOURCES}.')
        val = 'df' if (val == 'dataframe') else val
        val = 'pq' if (val == 'parquet') else val
        return val

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, val):
        raise NotImplementedError(
            'You cannot directly set the DataFrame df of a Context. Use context.use_dataframe() instead.')

    @property
    def eval_start(self):
        return self._eval_interval.start

    @property
    def eval_end(self):
        return self._eval_interval.end

    @property
    def time_index(self) -> pd.DatetimeIndex:
        self._assert_datasource_df_pq()

        if DATETIME_COL_NAME in self._sensor_cache:
            return self._sensor_cache[DATETIME_COL_NAME]

        idx = None
        if self.datasource == 'df':
            idx = self.df[self.eval_start:self.eval_end].index
        elif self.datasource == 'pq':
            idx = pu.read(self.plant.raw_data_path, columns=[DATETIME_COL_NAME],
                          filters=((DATETIME_COL_NAME, '>=', self.eval_start), (DATETIME_COL_NAME, '<=', self.eval_end))
                          ).index

        index = idx.tz_convert(self.plant.tz_data)
        self._sensor_cache[DATETIME_COL_NAME] = index

        return index

    @property
    def datasource(self):
        return self._datasource

    @datasource.setter
    def datasource(self, val):
        self._datasource = self.validate_datasource(val)
        if self._datasource == 'pq':
            self._df = None
        self._sensor_cache.clear()

    def set_eval_interval(self, eval_start=None, eval_end=None):
        eval_interval = self.EvalInterval(start=eval_start, end=eval_end)
        self._eval_interval = eval_interval
        self.reset_cache()

    def reset_cache(self):
        """To be called whenever something happens (outside Context) that invalidates the sensor_cache, e.g.
        editing a sensor's min or max, or adding an OperationEvent to a plant.
        """
        self._sensor_cache.clear()

    def use_dataframe(self,
                      df: pd.DataFrame,
                      calculate_virtuals: bool = False,
                      timezone: Union[str, pytz.timezone] = None,
                      drop_unneeded_columns: bool = False,
                      missing_columns: str = 'ignore'):
        """Configures Context to use the supplied dataframe as the datasource, instead of accessing the database.

        Parameters
        ----------
        df : pd.DataFrame. Must have a DateTimeIndex index.
        calculate_virtuals : bool. Whether virtual sensor calculation should be triggered (might be slow).
        timezone : timezone string or pytz timezone, example 'Europe/Berlin' or 'UTC' or pytz.FixedOffset(60).
        missing_columns : str, one of ['ignore', 'raise', 'nan']. Treatment of real sensor names expected but not found
        in the df columns.
        drop_unneeded_columns : bool. If True, columns not needed according to plant.get_raw_names(True) are dropped.

        Notes
        -----
        - Only numeric information in df is used. pint dtypes are ignored. No automatic unit conversion implemented.
        - Treatment of missing columns in df compared to expected sensor raw_names: missing_columns kwarg
        """
        if df is None:
            df_none_warning = 'Cannot set plant DataFrame in context module: DataFrame is None.'
            sp_logger.warning(df_none_warning)
            warnings.warn(df_none_warning)
            return None

        df.index = validate_timezone(df.index, timezone=timezone, plant=self.plant)
        df, n_duplicates = sanitize_dataframe(df)

        # Store only numeric data.
        for (col, dtype) in zip(df.columns, df.dtypes):
            if not pd.api.types.is_numeric_dtype(dtype):
                raise ValueError(
                    "To use a DataFarme as data source for a plant / Context, "
                    "the DataFrame must only contain numeric columns. "
                    f"Column {col} has dtype {dtype}.")
        # pint unit dtype is added at sensor.data, or plant.context.get_sensor_data()
        df = df.astype('float64', errors='raise')

        assert missing_columns in ['ignore', 'raise', 'nan'], f'Invalid "missing_columns": {missing_columns}'
        if missing_columns != 'ignore':
            cols_missing = set(self.plant.get_raw_names(include_virtuals=False)) - set(df.columns)
            if (len(cols_missing) > 0) and (missing_columns == 'raise'):
                raise ValueError(
                    f'DataFrame does not have all required columns. Columns missing: {cols_missing}.')
            if cols_missing == 'nan':
                df[cols_missing] = np.nan

        # Drop unneeded columns (not used by any sensor in the self.plant)
        if drop_unneeded_columns:
            df = df.drop(df.columns.difference(self.plant.get_raw_names(include_virtuals=True)), axis=1)

        self.reset_cache()
        self._datasource = 'df'
        self._df = df
        # By default, use whole dataframe
        self.set_eval_interval(eval_start=df.index[0], eval_end=df.index[-1])

        if calculate_virtuals:
            virtuals.calculate_virtuals(self.plant)
        else:
            virtuals.config_virtuals(self.plant)

        return

    def get_sensor_data(self, sensor: 'sunpeek.components.Sensor'):
        """Given a sensor and raw data Returns processed data for a given sensor. Usually called as sensor.data

        Parameters
        ----------
        sensor : Sensor. Data are returned in this sensor's native units, with time zone aware DatetimeIndex.

        Returns
        -------
        pandas Series, raw sensor values to which processing steps defined in self.process_data() to raw sensor values.

        Notes
        -----
        - If sensor.raw_name is found in context._sensor_cache, unprocessed data is returned (since the data in the cache
        should already be processed. In all other cases, context._process_data() is called.
        - For a parquet datasource, data is always returned, even if the raw name is not found in the sensor cache, in
        which case an all null series will be returned.
        """
        self._assert_datasource_df_pq()

        if sensor.raw_name in self._sensor_cache:
            # Note: If found in _sensor_cache, data is returned as-is, therefore no call to _process_data()
            s = self._sensor_cache[sensor.raw_name]

        else:
            # Retrieve data from datasource (df or db) and process it
            if self.datasource == 'df':
                if sensor.raw_name not in self.df.columns:
                    raise KeyError(f'Data for sensor {sensor.raw_name} was not found in the cache or the dataframe.'
                                   f' The context datasource is {self.datasource}.')
                s = self.df.loc[self.eval_start:self.eval_end, sensor.raw_name]

            elif self.datasource == 'pq':
                uri = self.plant.calc_data_path if sensor.is_virtual else self.plant.raw_data_path
                sensor_data_df = pu.read(uri=uri, columns=[sensor.raw_name], types_dict=self._get_types_dict(sensor),
                                         filters=(
                                             (DATETIME_COL_NAME, '>=', self.eval_start),
                                             (DATETIME_COL_NAME, '<=', self.eval_end)))

                s = sensor_data_df.squeeze()

            # Attach unit, call data cleaning
            s = self._process_data__native_unit(sensor, s)
            s = s.astype(f'pint[{sensor.native_unit}]')
            # Store processed data in cache
            self._sensor_cache[sensor.raw_name] = s

        # Convert to plant data time zone
        s = s.tz_convert(self.plant.tz_data)

        return s

    def store_data(self, sensor: 'sunpeek.components.Sensor', data: pd.Series):
        """Stores virtual sensor calculation results in the cache and, if the datasource is `df`, to the dataframe. If
        the datasource is `pq`, data will _not_ be stored by this method; in this case, `flush_virtuals_to_parquet`
        method should be used when all virtual sensor updates have been completed.

        Parameters
        ----------
        sensor : Sensor. Data will be stored for this virtual sensor.
        data : Union[pd.Series, None]
            Virtual sensor calculation results, with dtype numeric.

        Returns
        -------
        Nothing, new data is stored in the context DataFrame self.df

        Notes
        -----
        - Assumes dataframe backend for speed reason. Calling code needs to take care of storing things to database.
        - Also populates ._sensor_cache
        """
        self._assert_datasource_df_pq()

        # If a vsensor calculation was not possible (for whatever reason), Context will store an all-NaN series.
        if data is None:
            data = pd.Series(data=np.nan, index=self.time_index, name=sensor.raw_name)
        else:
            if len(data) != len(self.time_index):
                raise CalculationError(
                    'Size of virtual sensor data is incompatible with size of Plant.time_index')
            data.index = self.time_index

            # pint unit is stored with sensor.native_unit and attached at context.get_sensor_data
            data = data.astype(float).astype(float)

            data.name = sensor.raw_name

            # All subsequent algorithms shall rely that everything is either a number or NaN.
            # Inf may arise in virtual sensors, e.g. due to CoolProp returning Inf.
            data[~np.isfinite(data)] = np.nan

        if self.datasource == 'df':
            self.df[sensor.raw_name] = data

        # Populate Context sensor cache for faster data retrieval in subsequent accesses
        self._sensor_cache[sensor.raw_name] = data.astype(f'pint[{sensor.native_unit}]')

    def flush_virtuals_to_parquet(self):
        """
        Stores any virtual sensor data in the sensor cache to the configured parquet datasource. The data is removed
        from the cache during this process.
        """
        self._assert_datasource_df_pq()
        if self.datasource == 'df':
            raise ValueError("Storing virtual sensor data to parquet is only possible when the backend is parquet")

        v_sensors = []
        for name in self.plant.get_raw_names(only_virtuals=True):
            v_sensors.append(self._sensor_cache.pop(name))

        data = pd.concat(v_sensors, axis=1)
        data['year'] = data.index.year
        data['quarter'] = data.index.quarter
        pu.write(data=data, uri=self.plant.calc_data_path, partition_cols=['year', 'quarter'], overwrite_period=True)

    N_TOTAL_TIMESTAMPS = "n_total_timestamps"
    N_AVAILABLE_TIMESTAMPS = "n_available_timestamps"
    NAN_DENSITY_IN_AVAILABLE = "nan_density_in_available"

    def get_nan_report(self,
                       include_virtuals: bool = False) -> NanReportResponse:
        """Data quality information about the plant's sensors' NaN values, taking ignored ranges into account.

        Returns
        -------
        nan_report : dict
            Dictionary keys are sensor.raw_name, dictionary value is a DataFrame reporting data quality.
            DataFrame index are all days between first and last data (within current context limits), regardless whether
            for data of a specific day were included in the current upload. DataFrame column names and descriptions:
            - `n_total_timestamps`: Number of total uploaded timestamps, including timestamps in ignored ranges
            - `n_available_timestamps`: Number of timestamps available for analysis, that is: outside ignored ranges
            - `nan_density_in_available`: NaN density (ratio of NaNs to all values), outside ignored ranges
        """
        # not_ignored: marks the relevant pieces of data. True if timestamp is not within ignored range
        not_ignored = pd.Series(True, index=self.time_index)
        for r in self.plant.ignored_ranges:
            mask = (self.time_index >= r.left) & (self.time_index <= r.right)
            not_ignored.loc[mask] = False

        sensor_names = self.plant.get_raw_names(include_virtuals=include_virtuals)
        nan_report = {s: self._create_sensor_nan_report(not_ignored, self.plant.get_raw_sensor(s))
                      for s in sensor_names}

        nrr = NanReportResponse()
        nrr.nan_report = nan_report

        return nrr

    def _create_sensor_nan_report(self, not_ignored: pd.Series, sensor: 'sunpeek.components.Sensor') -> pd.DataFrame:
        """For a given DataFrame and sensor (raw_name), create a DataFrame, aggregating NaN information by day.

        Parameters
        ----------
        not_ignored : pd.Series, True where outside an ignored range.
        sensor : Sensor

        Returns
        -------
        df : pd.DataFrame with DatetimeIndex. See docstring of `Context.get_nan_report()`.
        """
        # Total number of timestamps per day
        days = self.time_index.date
        n_total_timestamps = not_ignored.groupby(by=days).count()

        # Number of not_ignored timestamps per day == available ranges
        n_available_timestamps = not_ignored.groupby(by=days).sum()

        # Nans in available ignored ranges (the ones that actually hurt)
        is_nan_in_available = sensor.data.isna() & not_ignored
        n_nans_in_available = is_nan_in_available.groupby(by=days).sum()

        # Nan density in available ranges.
        nan_density_in_available = n_nans_in_available / n_available_timestamps

        df_out = pd.concat([n_total_timestamps.rename(self.N_TOTAL_TIMESTAMPS),
                            n_available_timestamps.rename(self.N_AVAILABLE_TIMESTAMPS),
                            nan_density_in_available.rename(self.NAN_DENSITY_IN_AVAILABLE),
                            ], axis=1)
        df_out.index = pd.to_datetime(df_out.index)

        return df_out

    def _process_data__native_unit(self, sensor: 'sunpeek.components.Sensor', s_raw):
        """This is the main data processing method, it implements e.g. min max filtering, plant.ignored_ranges etc.
        This method is intended for sensor data which is given as numeric pd.Series, not dtype pint, to accelerate
        runtime.

        Parameters
        ----------
        sensor : Sensor. Process this sensor's data.
        s_raw : pd.Series
            Unprocessed data for sensor, with float (or equiv.) dtype, typically obtained from self.get_sensor_data()

        Returns
        -------
        s : pd.Series
            Processed data for sensor, with numeric dtype.
        """
        s = s_raw
        # Set values in ignored ranges to NaN
        for irng in self.plant.ignored_ranges:  # pd.Interval
            mask = (s.index >= irng.left) & (s.index <= irng.right)
            s[mask] = np.nan
        # Lower and Upper replacement intervals (see HarvestIT #177)
        s = self._replace_lower__native(s, sensor)
        s = self._replace_upper__native(s, sensor)

        return s

    def _assert_datasource_df_pq(self):
        if self.datasource is None:
            raise ConfigurationError('Context datasource is None.')
        if self.datasource not in ['df', 'pq']:
            raise ConfigurationError(f'Unexpected Context datasource {self.datasource}.')

    def verify_time_index(self):
        """Make sure context has a valid time index."""
        self.time_index
        return

    @staticmethod
    def _replace_lower__native(data, sensor):
        """Implement lower replacement interval, see #177.

        Parameters
        ----------
        data : pd.Series with unprocessed data
        sensor : Sensor

        Returns
        -------
        s : pd.Series with replaced values.
        """
        left, right, replace = sensor.value_replacements__native['lower']
        if (left is None) and (right is None) and (replace is None):
            # all None: nothing to do
            return data

        if right is None and replace is None:
            # no replacement value given, only left is not None
            data[data < left] = np.nan
            return data

        if left is None and replace is None:
            # no replacement value given, only right is not None
            data[data < right] = np.nan
            return data

        if left is None:
            data[data < right] = replace
            return data

        # all are not-NaN
        data[data < left] = np.nan
        data[(data >= left) & (data < right)] = replace
        # Does not work, package incompatibility... s[(s >= left) & (s < right)] = replace
        return data

    @staticmethod
    def _replace_upper__native(data, sensor):
        """Implement upper replacement interval, see #177.

        Parameters
        ----------
        data : pd.Series with unprocessed data
        sensor : Sensor

        Returns
        -------
        s : pd.Series with replaced values.
        """
        left, right, replace = sensor.value_replacements__native['upper']
        if (left is None) and (right is None) and (replace is None):
            # all None: nothing to do
            return data

        if left is None and replace is None:
            # no replacement value given, only right is not None
            data[data > right] = np.nan
            return data

        if right is None and replace is None:
            # no replacement value given, only left is not None
            data[data > left] = np.nan
            return data

        if right is None:
            data[data > left] = replace
            return data

        # all are not-NaN
        data[data > right] = np.nan
        data[(data > left) & (data <= right)] = replace
        return data

    @staticmethod
    def _get_types_dict(sensor):
        types_dict = {}
        # if getattr(sensor.sensor_type, 'name', '') == 'bool':
        #     types_dict[sensor.raw_name] = bool
        if getattr(sensor.sensor_type, 'compatible_unit_str', '') == 'str':
            types_dict[sensor.raw_name] = str
        else:
            types_dict[sensor.raw_name] = float

        return types_dict
