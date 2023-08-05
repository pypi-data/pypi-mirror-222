"""_668.py

HobbingProcessProfileCalculation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _663
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_PROFILE_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessProfileCalculation')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1023
    from mastapy.utility_gui.charts import _1854
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _659


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessProfileCalculation',)


class HobbingProcessProfileCalculation(_663.HobbingProcessCalculation):
    """HobbingProcessProfileCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_PROFILE_CALCULATION

    class _Cast_HobbingProcessProfileCalculation:
        """Special nested class for casting HobbingProcessProfileCalculation to subclasses."""

        def __init__(self, parent: 'HobbingProcessProfileCalculation'):
            self._parent = parent

        @property
        def hobbing_process_calculation(self):
            return self._parent._cast(_663.HobbingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
            
            return self._parent._cast(_677.ProcessCalculation)

        @property
        def hobbing_process_profile_calculation(self) -> 'HobbingProcessProfileCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessProfileCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_display_method(self) -> '_1023.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property."""

        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.cylindrical._1023', 'CylindricalGearProfileMeasurementType')(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_1023.CylindricalGearProfileMeasurementType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType')
        self.wrapped.ChartDisplayMethod = value

    @property
    def left_flank_profile_modification_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_profile_bands(self) -> 'int':
        """int: 'NumberOfProfileBands' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def result_z_plane(self) -> 'float':
        """float: 'ResultZPlane' is the original name of this property."""

        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    def result_z_plane(self, value: 'float'):
        self.wrapped.ResultZPlane = float(value) if value is not None else 0.0

    @property
    def right_flank_profile_modification_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank(self) -> '_659.CalculateProfileDeviationAccuracy':
        """CalculateProfileDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_659.CalculateProfileDeviationAccuracy':
        """CalculateProfileDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HobbingProcessProfileCalculation._Cast_HobbingProcessProfileCalculation':
        return self._Cast_HobbingProcessProfileCalculation(self)
