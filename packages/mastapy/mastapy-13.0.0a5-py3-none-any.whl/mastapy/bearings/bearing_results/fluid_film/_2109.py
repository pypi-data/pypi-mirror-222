"""_2109.py

LoadedPlainJournalBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.fluid_film import _2106
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_JOURNAL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedPlainJournalBearingResults')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2110


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedPlainJournalBearingResults',)


class LoadedPlainJournalBearingResults(_2106.LoadedFluidFilmBearingResults):
    """LoadedPlainJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_JOURNAL_BEARING_RESULTS

    class _Cast_LoadedPlainJournalBearingResults:
        """Special nested class for casting LoadedPlainJournalBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedPlainJournalBearingResults'):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_results(self):
            return self._parent._cast(_2106.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(self):
            from mastapy.bearings.bearing_results import _1941
            
            return self._parent._cast(_1941.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1944
            
            return self._parent._cast(_1944.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(self):
            from mastapy.bearings.bearing_results import _1936
            
            return self._parent._cast(_1936.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1862
            
            return self._parent._cast(_1862.BearingLoadCaseResultsLightweight)

        @property
        def loaded_grease_filled_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2107
            
            return self._parent._cast(_2107.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_results.fluid_film import _2111
            
            return self._parent._cast(_2111.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_plain_journal_bearing_results(self) -> 'LoadedPlainJournalBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedPlainJournalBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_position_of_the_minimum_film_thickness_from_the_x_axis(self) -> 'float':
        """float: 'AngularPositionOfTheMinimumFilmThicknessFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularPositionOfTheMinimumFilmThicknessFromTheXAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def attitude_angle(self) -> 'float':
        """float: 'AttitudeAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AttitudeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def attitude_force(self) -> 'float':
        """float: 'AttitudeForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AttitudeForce

        if temp is None:
            return 0.0

        return temp

    @property
    def diametrical_clearance(self) -> 'float':
        """float: 'DiametricalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiametricalClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def eccentricity_ratio(self) -> 'float':
        """float: 'EccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EccentricityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def kinematic_viscosity(self) -> 'float':
        """float: 'KinematicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @property
    def lubricant_density(self) -> 'float':
        """float: 'LubricantDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_central_film_thickness(self) -> 'float':
        """float: 'MinimumCentralFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCentralFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_load(self) -> 'float':
        """float: 'NonDimensionalLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def non_dimensional_power_loss(self) -> 'float':
        """float: 'NonDimensionalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_temperature(self) -> 'float':
        """float: 'OperatingTemperature' is the original name of this property."""

        temp = self.wrapped.OperatingTemperature

        if temp is None:
            return 0.0

        return temp

    @operating_temperature.setter
    def operating_temperature(self, value: 'float'):
        self.wrapped.OperatingTemperature = float(value) if value is not None else 0.0

    @property
    def pressure_velocity(self) -> 'float':
        """float: 'PressureVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_load_per_unit_of_projected_area(self) -> 'float':
        """float: 'RadialLoadPerUnitOfProjectedArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialLoadPerUnitOfProjectedArea

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_relative_rotation_speed(self) -> 'float':
        """float: 'ShaftRelativeRotationSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftRelativeRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def journal_bearing_rows(self) -> 'List[_2110.LoadedPlainJournalBearingRow]':
        """List[LoadedPlainJournalBearingRow]: 'JournalBearingRows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JournalBearingRows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedPlainJournalBearingResults._Cast_LoadedPlainJournalBearingResults':
        return self._Cast_LoadedPlainJournalBearingResults(self)
