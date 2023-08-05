"""
Implements the data ingestion process as roughly described in HarvestIT #187.
Data source backend can either be DataFrame or database (as implemented in Context class).
This module implements the same data ingestion process for both data sources.

Instantiate with DataUploader_df or DataUploader_pq,
then do_upload() to trigger the upload.

Data ingestion is implemented in this module. Data stored (in database or dataframe) have gone through some
sanity checking. As a result, we can rely on having a timezone-aware, sorted datetime index with no duplicates,
data is either numeric or NaN, all component slots are populated with data.
The same import & sanity procedures are used for both database and dataframe backend.
Any further, dynamic data processing steps are done on-the-fly (see `Context` class), things like ignored intervals and
min-max replacement intervals.
In this way, for instance, an ignored range can be added or deleted in a plant, and sensor data will behave
accordingly. This is implemented in common.context.

Data ingestion triggers virtual sensor calculation.
do_upload() returns data quality check ("sensor validation"), available as per-day and per-sensor information.

Notes
-----
Main method is do_upload() which returns the upload response in a dict. What it does:
- checks timezone info in csv files
- handles strings in data
- sorts timestamps and drops duplicates
- calculates virtual sensors
- calls sensor validation and kernel method validation
- uploads data to store in raw_data table in db#
"""

import os
import warnings
import pathlib
import numpy as np
from typing import List, Union
import time
import pandas as pd
import pytz
from io import BytesIO
import datetime

import sunpeek.common.time_zone as time_zone
from sunpeek.common.utils import DatetimeTemplates
from sunpeek.common.utils import sp_logger
from sunpeek.data_handling.context import Context, sanitize_dataframe
from sunpeek.base_model import BaseModel
from sunpeek.common.errors import DataProcessingError, TimeZoneError
from sunpeek.db_utils import DATETIME_COL_NAME
import parquet_datastore_utils as pu
from sunpeek.common.time_zone import process_timezone


class DataUploadResponseFile(BaseModel):
    name: Union[str, None]
    exists: Union[bool, None]
    size_bytes: Union[int, None]
    missing_columns: Union[List[str], None]
    error_cause: Union[str, None]


class DataUploadResponse(BaseModel):
    n_uploaded_data_rows: Union[int, None]
    # n_available_data_rows: Union[int, None]
    # nan_density: Union[float, None]
    n_duplicates_index: Union[int, None]
    response_per_file: Union[List[DataUploadResponseFile], None]
    db_response: Union[dict, None]


class DataColumnsResponse(BaseModel):
    sensors: Union[List[str], None]
    index: Union[str, None]


class DataUploader_df:
    """
    Data uploads of csv files to a plant using Context backend with datasource 'dataframe'.

    Notes
    -----
    - This class does not need and not use the database. Use DataUploader_pq for parquet backend.
    - The csv files need not be in chronological order.
    - Number of columns needs not be the same across files.
    - Time zone information must either be given in csv timestamps or as timezone.
    """

    def __init__(self,
                 plant,
                 datetime_template: DatetimeTemplates = None,
                 datetime_format: str = None,
                 timezone: Union[str, pytz.timezone] = None,
                 csv_separator: str = ';',
                 csv_decimal: str = '.',
                 csv_encoding: str = 'utf-8',
                 index_col: int = 0,
                 eval_start: datetime.date = None,
                 eval_end: datetime.date = None,
                 on_file_error: str = 'report',
                 ):
        """
        Parameters
        ----------
        plant : Plant
        timezone : str or pytz.timezone.
            Optional. To be provided if timestamps in the data have no time zone information.
        csv_separator : str
            Used in pd.read_csv as 'sep' kwarg
        csv_decimal : str
            Used in pd.read_csv as 'decimal' kwarg
        csv_encoding : str
            Used in pd.read_csv as 'encoding' kwarg
        datetime_format : str
            Used to parse datetimes from csv file. Leave to None infers the format.
        index_col : int
            DataUploader will try to parse timestamps from this column.
        eval_start : datetime
            Limit the data that is read and imported
        eval_end : datetime
            Limit the data that is read and imported
        on_file_error : str
            Behaviour if an error is encountered reading a file, either `report` to store details in the file response
            and continue, or `raise`, to raise the error and stop.
        """
        self.plant = plant
        self.eval_start = eval_start
        self.eval_end = eval_end
        self.output = DataUploadResponse()

        if (datetime_template is None) and (datetime_format is None):
            raise DataProcessingError('Either "datetime_template" or "datetime_format" needs to be specified.')

        if isinstance(datetime_template, str):
            self.datetime_template = DatetimeTemplates[datetime_template]
        else:
            self.datetime_template = datetime_template

        self.datetime_format = datetime_format
        self.timezone = process_timezone(timezone, plant=self.plant)
        self.csv_decimal = csv_decimal
        self.index_col = index_col
        self.on_file_error = on_file_error

        def read_csv(csv, **kwargs):
            try:
                return pd.read_csv(csv,
                                   encoding=csv_encoding, sep=csv_separator,
                                   on_bad_lines='skip',
                                   parse_dates=False,
                                   dtype='str',
                                   **kwargs)
            except LookupError as e:
                raise DataProcessingError(str(e))

        self.read_csv = read_csv

    def do_upload(self, files: Union[str, os.PathLike, List[Union[str, os.PathLike]]],
                  calculate_virtuals: bool = True) -> DataUploadResponse:
        """Full measurement data ingestion process, also triggers virtual sensor calculation and sensor validation.

        Parameters
        ----------
        files : UploadFile, str, os.PathLike
            Files to upload.
        calculate_virtuals : bool
            Whether to trigger virtual sensor calculation.

        Raises
        ------
        FileNotFoundError
        ConnectionError

        Returns
        -------
        DataUploadResponse : Response from the data upload, various info fields.
        """
        files = self.__validate_files(files)

        start_time = time.time()
        self._pre_upload()

        # Full data ingestion process, common for all context datasources (dataframe, parquet).
        self._csv_to_plant(files, calculate_virtuals)

        self._post_upload()
        sp_logger.debug(f"[data_uploader] --- Finished after {(time.time() - start_time):.1f} seconds ---")

        return self.output

    def get_sensor_names(self, files):
        """Returns names of the sensors based on an example file (or BytesIO)

        Parameters
        ----------
        files : UploadFile, str, os.PathLike
            Files to upload.
        """
        files = self.__validate_files(files)
        bio = self._to_BytesIO(files[0])
        bio.seek(0)
        df = self.read_csv(bio, nrows=1, index_col=self.index_col)

        return df.columns

    def get_index_name(self, files):
        """Returns name of the index column based on an example file (or BytesIO)

        Parameters
        ----------
        files : UploadFile, str, os.PathLike
            Files to upload.
        """
        files = self.__validate_files(files)
        bio = self._to_BytesIO(files[0])
        bio.seek(0)
        df = self.read_csv(bio, nrows=1, index_col=self.index_col, usecols=[])

        return df.index.name

    @staticmethod
    def __validate_files(files):
        if files is None:
            raise DataProcessingError('No files to upload supplied.')
        if not isinstance(files, list):
            files = [files]
        if not (len(files) > 0):
            raise DataProcessingError('No files to upload supplied.')
        return files

    @staticmethod
    def _to_BytesIO(bio_or_file):  # noqa
        if hasattr(bio_or_file, 'filename'):
            bio = bio_or_file.file
        elif isinstance(bio_or_file, BytesIO):
            bio = bio_or_file
        else:
            with open(bio_or_file, 'rb') as f:
                bio = BytesIO(f.read())
        return bio

    def _csv_to_plant(self, files, calculate_virtuals: bool):
        """Full data ingestion process, from csv to plant with dataframe context.
        Reads files to DataFrame, sets plant context datasource, does sensor validation.
        """
        df = self._all_csv_to_single_df(files)
        self.plant.context.use_dataframe(df, calculate_virtuals=calculate_virtuals)
        return

    def _all_csv_to_single_df(self, files):
        """Concatenates the uploaded files into a single df.

        Returns
        -------
        df_all_files : pd.DataFrame

        Raises
        ------
        AssertionError

        Notes
        -----
        - Columns which do not match with any of the plant's sensor raw_names are dropped.
        - Works for fastAPI's UploadFile as well as for normal csv files.
        """
        sp_logger.debug(f"[data_uploader] Reading csv files to DataFrame.")
        sp_logger.debug(f"[data_uploader] Concatenating {len(files)} files.")
        start_time = time.time()

        # Iterate trough files and gather DataFrames
        df_all_files = None
        self.output.response_per_file = []
        for file in files:
            file_response = DataUploadResponseFile()
            try:
                # is either a FlaskApi File or file-path, or a BytesIO object
                if hasattr(file, 'filename'):
                    file_response.name = file.filename
                    file_response.exists = True
                elif isinstance(file, str) or isinstance(file, pathlib.Path):
                    file_response.name = os.path.basename(file)
                    file_response.exists = os.path.exists(file)
                elif isinstance(file, BytesIO):
                    file_response.name = None
                    file_response.exists = True
                else:
                    raise FileNotFoundError(f'Cannot interpret input for file: "{file}".')

                if not file_response.exists:
                    raise FileNotFoundError(f'Cannot find file: "{file_response.name}".')

                # Create BytesIO object
                bio = self._to_BytesIO(file)

                # get size
                bio.seek(0, os.SEEK_END)
                file_response.size_bytes = bio.tell()
                bio.seek(0)

                try:
                    df_file, missing_columns = self._one_csv_to_df(bio)
                except (ValueError, TimeZoneError) as ex:
                    sp_logger.exception(ex)
                    if self.on_file_error == 'raise':
                        raise
                    file_response.error_cause = f'Error: {ex}'
                    continue
                file_response.missing_columns = missing_columns

                # Concatenate the dataframes
                if len(df_file) > 0:
                    df_all_files = pd.concat([df_all_files, df_file], ignore_index=False)
                    if not isinstance(df_all_files.index, pd.DatetimeIndex):
                        raise DataProcessingError('Cannot concatenate DataFrames with mixed timezones since this '
                                                  'results in the DataFrame index not being a DatetimeIndex anymore.')

            finally:
                self.output.response_per_file.append(file_response)

        # Check for duplicates etc.
        df_all_files, n_duplicates_index = sanitize_dataframe(df_all_files)
        self.output.n_duplicates_index = n_duplicates_index
        if self.output.n_duplicates_index:
            duplicate_warning = f"Found {self.output.n_duplicates_index} duplicate index entries in data. " \
                                f"All rows with duplicate index will be removed."
            sp_logger.warning(duplicate_warning)
            warnings.warn(duplicate_warning)

        if (df_all_files is None) or len(df_all_files) < 2:
            df_all_files = None
            self.output.n_uploaded_data_rows = 0
            # self.output.n_available_data_rows = 0
            # self.output.nan_density = 1

            df_none_warning = 'Reading csv files resulted in a DataFrame with less than 2 rows.'
            sp_logger.warning(df_none_warning)
            warnings.warn(df_none_warning)
            # raise DataProcessingError('Reading csv files resulted in a DataFrame with less than 2 rows.')
        else:
            self.output.n_uploaded_data_rows = len(df_all_files)
            # # not_ignored: marks the relevant pieces of data. True if timestamp is not within ignored range
            # not_ignored = pd.Series(True, index=df_all_files.index)
            # for r in self.plant.ignored_ranges:
            #     mask = (df_all_files.index >= r.left) & (df_all_files.index <= r.right)
            #     not_ignored.loc[mask] = False
            # self.output.n_available_data_rows = not_ignored.to_numpy().sum()
            # self.output.nan_density =

        sp_logger.debug(
            f"[data_uploader] --- Done parsing {len(files)} files in {(time.time() - start_time):.1f} seconds.")

        return df_all_files

    def _one_csv_to_df(self, bio):
        """Read a BytesIO object to DataFrame.

        Parameters
        ----------
        bio : BytesIO object
            From an UploadFile or from a normal csv file.

        Returns
        -------
        df : pandas.DataFrame
            DataFrame with tz-aware DatetimeIndex
        missing_columns : List[str]
            Columns not found in the file

        Raises
        ------
        AssertionError

        Notes
        -----
        - Returns a DataFrame with DatetimeIndex taken from the first column, index is named according to
         sunpeek.db_utils.DATETIME_COL_NAME.
        - Missing columns are added as all-NaN columns.
        """
        # Parse timestamps from first column
        ds_cache = self._parse_timestamps(bio)
        try:
            skiprows = ds_cache.isna()
            # Limit the rows to read in the file, if bounds were provided
            if self.eval_start is not None:
                skiprows = skiprows | (ds_cache < self.eval_start)
            if self.eval_end is not None:
                skiprows = skiprows | (ds_cache > self.eval_end)
            ds_cache = ds_cache[~skiprows]
            # convert to numbers, for pd.read_csv()
            skiprows = [i for i, x in enumerate(np.insert(skiprows, 0, False)) if x]

            # Main read_csv call
            bio.seek(0)
            df = self.read_csv(bio,
                               usecols=lambda x: x in self.plant.get_raw_names(include_virtuals=False),
                               skiprows=skiprows)
            # read_csv with decimal kwarg fails when reading string, hence the two calls to apply()
            if self.csv_decimal is not None:
                df = df.apply(lambda x: x.str.replace(self.csv_decimal, '.'))
            df = df.apply(pd.to_numeric, errors='coerce')
            df = pd.DataFrame(index=ds_cache) if df.empty else df.set_index(ds_cache)
            df = df.rename_axis(DATETIME_COL_NAME)

            # Add missing real sensor column names as NaN columns
            missing_columns = set(self.plant.get_raw_names(include_virtuals=False)) - set(df.columns)
            df[list(missing_columns)] = np.nan

            return df, list(missing_columns)

        except Exception as ex:
            sp_logger.exception(ex)
            warnings.warn(f'Failed to read csv file using pandas read_csv. {ex}')
            raise ValueError(f'Failed to read csv file using pandas read_csv. {ex}') from ex

    def _parse_timestamps(self, bio):
        """Parse timestamps from first column in bio, validate timezone, return tz-aware DatetimeIndex
        """
        bio.seek(0)
        ds = self.read_csv(bio, usecols=[self.index_col]).iloc[:, 0]
        # In parsing timestamps, priority is given to the more explicit self.datetime_format:
        if self.datetime_format is not None:
            ds = pd.to_datetime(ds, errors='coerce', format=self.datetime_format)
        else:
            dayfirst = True if (self.datetime_template == DatetimeTemplates.day_month_year) else False
            yearfirst = True if (self.datetime_template == DatetimeTemplates.year_month_day) else False
            try:
                ds = pd.to_datetime(ds, errors='coerce', dayfirst=dayfirst, yearfirst=yearfirst)
            except (pd.errors.ParserError, ValueError) as e:
                raise DataProcessingError(
                    f"Pandas to_datetime was unable to parse timestamps from the file, given datetime_template="
                    f"{self.datetime_template}. Try to set an explicit 'datetime_format' instead.")
        # Does not parse timezone-aware datetimes correctly, e.g. '2017-04-30 00:00:00+00:00' is parsed as NaT:
        # ds = pd.to_datetime(ds, errors='coerce', infer_datetime_format=True)

        try:
            ds = pd.DatetimeIndex(ds)
        except:
            # Mixed timezone timestamp columns lead to Index class df.index with dtype 'object'
            # see https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
            raise TimeZoneError(
                '[data_uploader] Could not convert timestamps of the csv file to a DatetimeIndex. '
                'One cause why this happens are mixed-timezone timestamps or only some rows having timezones.')

        ds = time_zone.validate_timezone(ds, timezone=self.timezone, plant=self.plant)

        return ds

    def _pre_upload(self):
        pass

    def _post_upload(self):
        pass


# class DataUploader_db(DataUploader_df):
#     """Data upload from csv files to database.
#     """
#
#     def __init__(self, session, **kwargs):
#         super().__init__(**kwargs)
#         self._sensor_raw_names = None
#         self.output.db_response = {}
#         # Try to establish database connection, raises ConnectionError
#         self.db_connection = import_db_ops().get_db_connection()
#         self.session = session
#
#     @property
#     def table_name(self):
#         return self.plant.raw_table_name
#
#     def _get_types_dict(self):
#         types_dict = {DATETIME_COL_NAME: datetime.datetime}
#         for sensor in self.plant.raw_sensors:
#             if getattr(sensor.sensor_type, 'name', '') == 'bool':
#                 types_dict[sensor.raw_name] = bool
#             elif getattr(sensor.sensor_type, 'compatible_unit_str', '') == 'str':
#                 types_dict[sensor.raw_name] = str
#             else:
#                 types_dict[sensor.raw_name] = float
#
#         return types_dict
#
#     def _create_raw_data_table(self):
#         """Creates raw data table if it does not exists in the database.
#         """
#         # Create database inferring runtime types
#         try:
#             types_dict = self._get_types_dict()
#             import_db_ops().create_table_dynamic(self.session.get_bind(), self.table_name, types_dict)
#             self.output.db_response['new_table_created'] = True
#             self.output.db_response['new_table_name'] = self.table_name
#
#         except Exception as ex:
#             sp_logger.exception(ex)
#             raise
#
#     def _update_table(self):
#         types_dict = self._get_types_dict()
#         import_db_ops().create_new_data_cols(self.session.get_bind(), self.table_name, types_dict)
#
#     def _pre_upload(self):
#         table_exists = import_db_ops().db_table_exists(self.session.get_bind(), self.table_name)
#         if table_exists:
#             sp_logger.debug(f"[data_uploader] Table {self.table_name} exists in database. Adding columns for any "
#                             f"new sensors for plant {self.plant.name}.")
#             self._update_table()
#         else:
#             sp_logger.debug(f"[data_uploader] Creating table {self.table_name} in database.")
#             self._create_raw_data_table()
#
#     def _post_upload(self):
#         """Save dataframe to database
#         """
#         df = self.plant.context.df
#         #if df is not None:
#         #    # Before writing to database, any overlapping (not only duplicate) data in db is deleted.
#         #    sp_logger.debug(f"[data_uploader] Deleting overlapping data from table {self.table_name}.")
#         #    self.output.db_response['overlap_response'] = \
#         #        import_db_ops().delete_overlapping_data(self.db_connection, self.table_name,
#         #                                                overlapping_boundaries=(df.index[0], df.index[-1]))
#
#         # Before writing to database, any overlapping (not only duplicate) data in db is deleted.
#         sp_logger.debug(f"[data_uploader] Deleting overlapping data from table {self.table_name}.")
#         self.output.db_response['overlap_response'] = \
#             import_db_ops().delete_overlapping_data(self.db_connection, self.table_name,
#                                                     overlapping_boundaries=(df.index[0], df.index[-1]))
#
#         #    # Write new data (including virtual sensors) to db.
#         #    sp_logger.debug(f"[data_uploader] Writing dataframe to table {self.table_name}...")
#         #    self.output.db_response['measure_data_saved_db_ok'] = import_db_ops().df_to_db(self.db_connection, df,
#         #                                                                                   self.table_name)
#         #    if self.output.db_response['measure_data_saved_db_ok']:
#         #        self.db_connection.commit()
#         #        sp_logger.debug(f"[data_uploader] Data succesfully saved in db table {self.table_name}.")
#         #        import_db_ops().disconnect_db(self.db_connection)
#         #    else:
#         #        sp_logger.debug(f"[data_uploader] Error writing data to db table {self.table_name}.")
#         #        self.db_connection.rollback()
#         #        import_db_ops().disconnect_db(self.db_connection)
#         #        raise ConnectionError('Failed to store data in database table.')
#
#         # From now on, data is accessed by 'db' and uses the full datetime range available in the db
#         self.plant.context = Context(plant=self.plant, datasource='db',
#                                      eval_start=self.eval_start, eval_end=self.eval_end)


class DataUploader_pq(DataUploader_df):
    """
    Data upload from csv files to parquet datastore.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sensor_raw_names = None
        self.raw_data_path = self.plant.raw_data_path
        self.calc_data_path = self.plant.calc_data_path

    def _post_upload(self):
        df = self.plant.context.df
        if df is None:
            # Do nothing, this is already accounted for by Context. 
            return

        df['year'] = df.index.year
        df['quarter'] = df.index.quarter

        raw_df = df[self.plant.get_raw_names(include_virtuals=False) + ['year', 'quarter']]
        calc_df = df[self.plant.get_raw_names(only_virtuals=True) + ['year', 'quarter']]

        pu.write(data=raw_df, uri=self.raw_data_path, partition_cols=['year', 'quarter'], overwrite_period=True)
        pu.write(data=calc_df, uri=self.calc_data_path, partition_cols=['year', 'quarter'], overwrite_period=True)

        # From now on, data is accessed by 'pq' and uses the full datetime range available in the datastore
        self.plant.context = Context(plant=self.plant, datasource='pq', eval_start=self.eval_start,
                                     eval_end=self.eval_end)
