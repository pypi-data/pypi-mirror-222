from abc import ABC, abstractmethod
from typing import Callable, Union
import pandas as pd

from sunpeek.common.unit_uncertainty import Q
from sunpeek.components.base import AlgoCheckMode
from sunpeek.core_methods.common.main import is_valid_collector
from sunpeek.components.physical import Plant, Array
from sunpeek.core_methods.pc_method import AvailablePCEquations
from sunpeek.common.errors import PCMethodError
from sunpeek.serializable_models import ProblemReport, ProblemType, AlgoProblem

# Common to all equations
MAX_DELTA_T_COLLECTOR = Q(5.0, 'K hour**-1')
MIN_TE_AMB = Q(5.0, 'degC')
MAX_WIND_SPEED = Q(10, 'm s**-1')


# TODO Use this for all equations?
MAX_AOI = Q(80, 'deg')

MAX_AOI_EQ2 = Q(75, 'deg')

# Equation 1
MIN_RD_GTI = Q(800, 'W m**-2')

# Equation 2
MIN_RD_BTI = Q(600, 'W m**-2')


# noinspection PyArgumentList
class Equation(ABC):
    """Template class for the equations / formulae for calculating power output, as defined in the ISO 24194:

    The equations are defined in ISO 24194 chapter 5.2.1. The equations specify
    1. how power output is calculated / estimated
    2. and what restrictions are applied to data: the criteria in ISO 24194 Table 1 depend on the equation choice.

    "
    # 5.1 Stating an estimate for the thermal power output of a collector field
    The estimated power output of the collector array is given as an equation depending on the collector parameters
    according to ISO 9806 and operation conditions. The measured power shall comply with the corresponding calculated
    power according to this equation. Measured and calculated power are only compared under some specific conditions
    to avoid too large uncertainties - see section 5.4

    The estimate is given by stating the equation to be used for calculating the power output, including specific
    values for the parameters in equation. The three possible equations are given in the next three subsections.
    The collector module efficiency parameters eta0_hem, eta0_b, Kb(theta) Kd, a1, a2, a5 [1] and a8 should be based on
    certified test results. When an estimate is given it shall always be stated which equation shall be used for
    checking the performance:

    a) Simple check, using total radiation on the collector plane when checking the power output (ISO this standard,
    eq 1).
    b) Advanced check, using direct and diffuse radiation on collector plane when checking the power output
    (ISO this standard, eq 2).
    c) Advanced check, using only direct radiation on collector plane when checking the power output
    (ISO this standard, eq3)

    [1] in the older Solar Keymark data sheets a5 is denoted c_eff
    "
    """

    id = None

    # Restrictions on operating conditions based on Table 1 of ISO 24194.
    # Only data that pass these restrictions (as averages over given time range) are used for calculation of estimated
    # array power.
    # Common to equations 1 & 2
    max_deltat_collector = MAX_DELTA_T_COLLECTOR
    min_te_amb = MIN_TE_AMB
    max_wind_speed = MAX_WIND_SPEED

    @classmethod
    def create(cls, equation: Union[AvailablePCEquations, int], use_wind: bool) -> 'Equation':
        if equation == AvailablePCEquations.one:
            return Equation1(use_wind)

        elif equation == AvailablePCEquations.two:
            return Equation2(use_wind)

        else:
            raise PCMethodError(f'Unknown equation number "{equation}". '
                                f'Valid equations: {", ".join(map(str, AvailablePCEquations))}.')
            # f'Valid equations: {", ".join([str(e.value) for e in AvailablePCEquations])}.')

    def __init__(self, use_wind: bool):
        """
        Parameters
        ----------
        use_wind : bool
            if False, the wind speed sensor is ignored as a restriction to finding valid intervals
            in the data filtering process for meeting the ISO 24194 requirements.
        """
        self.use_wind = use_wind
        return

    def report_problems(self, array: Array, check_mode: AlgoCheckMode) -> ProblemReport:
        r = ProblemReport()

        for attrib in ['area_gr']:
            if array.is_attrib_missing(attrib):
                r.add_own(AlgoProblem(ProblemType.component_attrib, array, attrib))

        if not is_valid_collector(array.collector_type, check_mode):
            r.add_own(AlgoProblem(ProblemType.component_attrib,
                                  array, 'collector_type',
                                  'Collector type is None or UninitialisedCollectorType.'))
        else:
            for attrib in ['a1', 'a2', 'a5', 'eta0b', 'kd']:
                if getattr(array.collector_type, attrib) is None:
                    r.add_own(AlgoProblem(ProblemType.component_attrib,
                                          array.collector_type, attrib,
                                          f'Collector coefficient "{attrib}" is required but is None / not available.'))

        for slot_name in ['te_op', 'te_op_deriv', 'is_shadowed', 'iam']:
            if array.is_slot_missing(slot_name, check_mode):
                r.add_own(AlgoProblem(ProblemType.component_slot, array, slot_name))

        if self.use_wind:
            if array.plant.is_slot_missing('ve_wind', check_mode):
                r.add_own(AlgoProblem(ProblemType.component_slot, array.plant, 've_wind'))

        return r

    @abstractmethod
    def get_nan_mask(self, plant: Plant):
        """This method checks whether all sensors required to apply an equations are available.

        Returns
        -------
        bool : True where any of the sensors required to calculate equation are NaN.

        Notes
        -----
        In this PC Method implementation, only data records are used where none of the needed sensor records is NaN.
        Make sure _set_equation() has been called before, so self.equation is not None.
        """
        raise NotImplementedError

    def _get_nan_mask_common(self, plant):
        """This method checks sensors common to both equations 1 and 2.
        """

        # Plant
        mask = plant.te_amb.data.isna()
        mask = mask | plant.tp.data.isna()
        mask = mask | plant.sun_apparent_elevation.data.isna()
        if self.use_wind:
            mask = mask | plant.ve_wind.data.isna()

        # Arrays
        for array in plant.arrays:
            mask = mask | array.te_op.data.isna()
            mask = mask | array.te_op_deriv.data.isna()
            mask = mask | array.is_shadowed.data.isna()

        return mask

    @abstractmethod
    def calc_pc_restrictions(self, plant: Plant, resampler: Callable) -> pd.Series:
        """Check the operating condition restrictions of ISO 24194. Implements Table 1, chapter 5.4.

        Parameters
        ----------
        plant : Plant
        resampler : Callable
            Aggregates single records into an aggregated value, e.g. hourly mean.

        Returns
        -------
        pd.Series : bool mask, True where any of the sensors required to calculate equation are NaN.

        Notes
        -----
        From the ISO 24194:
            # 6.2 Valid data records
            Only data records (hourly average values) fulfilling the requirements in section 5.4 are valid.
            For checking the collector performance, the measuring period shall have at least 20 datapoints.
            [...]
            All valid datapoints should be used unless it is obvious that errors in the data or very atypical
            operating conditions occur (omitting valid data points shall be reported and justified).
        """
        raise NotImplementedError

    def _calc_pc_restrictions_common(self, plant, resampler) -> pd.Series:
        """Checks the operating condition restrictions that are common to Equation 1 and Equation 2.

        Returns
        -------
        pd.Series : bool mask
        """
        # Minimum ambient temperature
        is_valid = resampler(plant.te_amb.data) >= self.min_te_amb
        if self.use_wind:
            # Maximum wind speed
            is_valid = is_valid & (resampler(plant.ve_wind.data) <= self.max_wind_speed)

        for array in plant.arrays:
            # Shading
            is_valid = is_valid & (resampler(array.is_shadowed.data, 'sum') == 0)
            # Maximum temperature change
            is_valid = is_valid & (resampler(array.te_op_deriv.data).abs() <= self.max_deltat_collector)

        return is_valid

    @abstractmethod
    def calc_estimated_power(self, array: Array, aggregator: Callable) -> pd.Series:
        """Calculates the estimated specific power output of the collector based on the ISO equation formula.

        Parameters
        ----------
        array : Array
        aggregator : Callable
            Aggregates single records into an aggregated value, e.g. hourly mean.

        Returns
        -------
        pd.Series : Estimated power output of the collector, unit-aware series compatible to unit [W m**-2]
        """
        raise NotImplementedError


# noinspection PyArgumentList
class Equation1(Equation):
    """ Implements Equation 1 of the ISO 24194. See Equation base class for more infos.
    """
    id = 1

    # Restrictions specific to equation 1
    # max_aoi = Q(30, 'deg')
    # Deliberately set maximum incidence angle (not defined in ISO 24194) to avoid numerical problems and problems
    # with calculated Kd values at high incidence angles.

    # TODO change for newest ISO 24194 version
    max_aoi_eq1 = MAX_AOI_EQ2
    min_rd_gti = MIN_RD_GTI

    def report_problems(self, array: Array, check_mode: AlgoCheckMode) -> ProblemReport:
        r = super().report_problems(array, check_mode)

        for attrib in ['eta0hem']:
            if getattr(array.collector_type, attrib) is None:
                r.add_own(AlgoProblem(ProblemType.component_attrib,
                                      array.collector_type, attrib,
                                      f'Collector coefficient "{attrib}" is required for equation 1 but '
                                      f'is None / not available.'))

        for slot_name in ['rd_gti', 'aoi']:
            if array.is_slot_missing(slot_name, check_mode):
                r.add_own(AlgoProblem(ProblemType.component_slot, array, slot_name))

        return r

    def get_nan_mask(self, plant:Plant):
        # Common sensors
        mask = self._get_nan_mask_common(plant)

        # Specific to equation 1
        for array in plant.arrays:
            mask = mask | array.rd_gti.data.isna()
            mask = mask | array.aoi.data.isna()

        return mask

    def calc_pc_restrictions(self, plant, resampler) -> pd.Series:
        is_valid = self._calc_pc_restrictions_common(plant, resampler)

        for array in plant.arrays:
            # Minimum diffuse radiation
            is_valid = is_valid & (resampler(array.rd_gti.data) >= self.min_rd_gti)
            # Question: Use max aoi here, or mean, or...? Fails occasionally with 'max', not sure why, see #268
            # maximum incidence angle --> This criterion got removed in version ISO 24194:2022(E).
            # is_valid = is_valid & (resampler(array.aoi.data, 'mean') <= self.max_aoi)
            # Maximum incidence angle: not included as a criterion in ISO 24194:2022(E), but necessary to ensure
            # stability  
            is_valid = is_valid & (resampler(array.aoi.data, 'mean') <= self.max_aoi_eq1)

        return is_valid

    def calc_estimated_power(self, array, aggregator) -> pd.Series:
        """Calculates the estimated power output of a collector array based on equation 1 formula in ISO 24194.
        """
        # Collector coefficients
        a1 = array.collector_type.a1
        a2 = array.collector_type.a2
        a5 = array.collector_type.a5
        eta0b = array.collector_type.eta0b
        eta0hem = array.collector_type.eta0hem
        kd = array.collector_type.kd

        # Measurements
        rd_gti = aggregator(array.rd_gti.data)
        te_amb = aggregator(array.plant.te_amb.data)
        te_op = aggregator(array.te_op.data)
        te_op_deriv = aggregator(array.te_op_deriv.data)

        # Calculation of hemispheric incidence angle modifier for global tilted radiation:
        # Calculation is based on ISO 9806:2017 annex B, with variable name iam_xx used here instead of K_xx
        # G * iam_hem * eta0hem = G * eta0b * (0.85 * iam_b + 0.15 * iam_d)
        kb = aggregator(array.iam.data)
        khem = (eta0b / eta0hem) * (0.85 * kb + 0.15 * kd)

        tp_estimated_specific = eta0hem * khem * rd_gti \
                                - a1 * (te_op - te_amb) \
                                - a2 * (te_op - te_amb) ** 2 \
                                - a5 * te_op_deriv

        return tp_estimated_specific.astype('pint[W m**-2]')


class Equation2(Equation):
    """ Implements Equation 2 of the ISO 24194. See Equation base class for more infos.
    """
    id = 2

    # Restrictions specific to equation 2
    min_rd_bti = MIN_RD_BTI

    def get_nan_mask(self, plant: Plant):
        # Common sensors
        mask = self._get_nan_mask_common(plant)

        # Specific to equation 2
        for array in plant.arrays:
            mask = mask | array.rd_bti.data.isna()
            mask = mask | array.rd_dti.data.isna()
            mask = mask | array.iam.data.isna()

        return mask

    def report_problems(self, array: Array, check_mode: AlgoCheckMode) -> ProblemReport:
        r = super().report_problems(array, check_mode)

        for slot_name in ['rd_bti', 'rd_dti']:
            if array.is_slot_missing(slot_name, check_mode):
                r.add_own(AlgoProblem(ProblemType.component_slot, array, slot_name))

        return r

    def calc_pc_restrictions(self, plant, resampler) -> pd.Series:
        is_valid = self._calc_pc_restrictions_common(plant, resampler)

        for array in plant.arrays:
            # Minimum beam radiation
            is_valid = is_valid & (resampler(array.rd_bti.data) >= self.min_rd_bti)

        return is_valid

    def calc_estimated_power(self, array, aggregator) -> pd.Series:
        """Calculates the estimated specific power output of a collector array based on equation 2 formula in ISO 24194.
        """
        # Collector coefficients
        a1 = array.collector_type.a1
        a2 = array.collector_type.a2
        a5 = array.collector_type.a5
        eta0b = array.collector_type.eta0b
        kd = array.collector_type.kd

        # Measurements
        rd_bti = aggregator(array.rd_bti.data)
        rd_dti = aggregator(array.rd_dti.data)
        iam_b = aggregator(array.iam.data)
        te_amb = aggregator(array.plant.te_amb.data)
        te_op = aggregator(array.te_op.data)
        te_op_deriv = aggregator(array.te_op_deriv.data)

        tp_estimated_specific = eta0b * iam_b * rd_bti + eta0b * kd * rd_dti \
                                - a1 * (te_op - te_amb) \
                                - a2 * (te_op - te_amb) ** 2 \
                                - a5 * te_op_deriv

        return tp_estimated_specific.astype('pint[W m**-2]')
