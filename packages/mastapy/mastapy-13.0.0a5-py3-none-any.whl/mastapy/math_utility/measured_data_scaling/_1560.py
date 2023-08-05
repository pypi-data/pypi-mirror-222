"""_1560.py

DataScalingOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_OPTIONS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredDataScaling', 'DataScalingOptions')

if TYPE_CHECKING:
    from mastapy.math_utility import _1496, _1480
    from mastapy.math_utility.measured_data_scaling import _1561
    from mastapy.utility.units_and_measurements.measurements import (
        _1603, _1604, _1608, _1612,
        _1620, _1627, _1633, _1639,
        _1667, _1675, _1656, _1680,
        _1681, _1685, _1684, _1690,
        _1700, _1658, _1714, _1606,
        _1630, _1723, _1705, _1706,
        _1717, _1718, _1716, _1679,
        _1722, _1661, _1715, _1607
    )


__docformat__ = 'restructuredtext en'
__all__ = ('DataScalingOptions',)


class DataScalingOptions(_0.APIBase):
    """DataScalingOptions

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_OPTIONS

    class _Cast_DataScalingOptions:
        """Special nested class for casting DataScalingOptions to subclasses."""

        def __init__(self, parent: 'DataScalingOptions'):
            self._parent = parent

        @property
        def data_scaling_options(self) -> 'DataScalingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataScalingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_scaling(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling':
        """enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling: 'DynamicScaling' is the original name of this property."""

        temp = self.wrapped.DynamicScaling

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @dynamic_scaling.setter
    def dynamic_scaling(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DynamicScaling = value

    @property
    def weighting(self) -> '_1480.AcousticWeighting':
        """AcousticWeighting: 'Weighting' is the original name of this property."""

        temp = self.wrapped.Weighting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.MathUtility.AcousticWeighting')
        return constructor.new_from_mastapy('mastapy.math_utility._1480', 'AcousticWeighting')(value) if value is not None else None

    @weighting.setter
    def weighting(self, value: '_1480.AcousticWeighting'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.MathUtility.AcousticWeighting')
        self.wrapped.Weighting = value

    @property
    def acceleration_reference_values(self) -> '_1561.DataScalingReferenceValues[_1603.Acceleration]':
        """DataScalingReferenceValues[Acceleration]: 'AccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1603.Acceleration](temp) if temp is not None else None

    @property
    def angle_reference_values(self) -> '_1561.DataScalingReferenceValues[_1604.Angle]':
        """DataScalingReferenceValues[Angle]: 'AngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1604.Angle](temp) if temp is not None else None

    @property
    def angular_acceleration_reference_values(self) -> '_1561.DataScalingReferenceValues[_1608.AngularAcceleration]':
        """DataScalingReferenceValues[AngularAcceleration]: 'AngularAccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularAccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1608.AngularAcceleration](temp) if temp is not None else None

    @property
    def angular_velocity_reference_values(self) -> '_1561.DataScalingReferenceValues[_1612.AngularVelocity]':
        """DataScalingReferenceValues[AngularVelocity]: 'AngularVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1612.AngularVelocity](temp) if temp is not None else None

    @property
    def damage_rate(self) -> '_1561.DataScalingReferenceValues[_1620.DamageRate]':
        """DataScalingReferenceValues[DamageRate]: 'DamageRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageRate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1620.DamageRate](temp) if temp is not None else None

    @property
    def energy_reference_values(self) -> '_1561.DataScalingReferenceValues[_1627.Energy]':
        """DataScalingReferenceValues[Energy]: 'EnergyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1627.Energy](temp) if temp is not None else None

    @property
    def force_reference_values(self) -> '_1561.DataScalingReferenceValues[_1633.Force]':
        """DataScalingReferenceValues[Force]: 'ForceReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1633.Force](temp) if temp is not None else None

    @property
    def frequency_reference_values(self) -> '_1561.DataScalingReferenceValues[_1639.Frequency]':
        """DataScalingReferenceValues[Frequency]: 'FrequencyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1639.Frequency](temp) if temp is not None else None

    @property
    def linear_stiffness_reference_values(self) -> '_1561.DataScalingReferenceValues[_1667.LinearStiffness]':
        """DataScalingReferenceValues[LinearStiffness]: 'LinearStiffnessReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearStiffnessReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1667.LinearStiffness](temp) if temp is not None else None

    @property
    def mass_per_unit_time_reference_values(self) -> '_1561.DataScalingReferenceValues[_1675.MassPerUnitTime]':
        """DataScalingReferenceValues[MassPerUnitTime]: 'MassPerUnitTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPerUnitTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1675.MassPerUnitTime](temp) if temp is not None else None

    @property
    def medium_length_reference_values(self) -> '_1561.DataScalingReferenceValues[_1656.LengthMedium]':
        """DataScalingReferenceValues[LengthMedium]: 'MediumLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MediumLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1656.LengthMedium](temp) if temp is not None else None

    @property
    def percentage(self) -> '_1561.DataScalingReferenceValues[_1680.Percentage]':
        """DataScalingReferenceValues[Percentage]: 'Percentage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Percentage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1680.Percentage](temp) if temp is not None else None

    @property
    def power_reference_values(self) -> '_1561.DataScalingReferenceValues[_1681.Power]':
        """DataScalingReferenceValues[Power]: 'PowerReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1681.Power](temp) if temp is not None else None

    @property
    def power_small_per_unit_area_reference_values(self) -> '_1561.DataScalingReferenceValues[_1685.PowerSmallPerArea]':
        """DataScalingReferenceValues[PowerSmallPerArea]: 'PowerSmallPerUnitAreaReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallPerUnitAreaReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1685.PowerSmallPerArea](temp) if temp is not None else None

    @property
    def power_small_reference_values(self) -> '_1561.DataScalingReferenceValues[_1684.PowerSmall]':
        """DataScalingReferenceValues[PowerSmall]: 'PowerSmallReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1684.PowerSmall](temp) if temp is not None else None

    @property
    def pressure_reference_values(self) -> '_1561.DataScalingReferenceValues[_1690.Pressure]':
        """DataScalingReferenceValues[Pressure]: 'PressureReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1690.Pressure](temp) if temp is not None else None

    @property
    def safety_factor(self) -> '_1561.DataScalingReferenceValues[_1700.SafetyFactor]':
        """DataScalingReferenceValues[SafetyFactor]: 'SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1700.SafetyFactor](temp) if temp is not None else None

    @property
    def short_length_reference_values(self) -> '_1561.DataScalingReferenceValues[_1658.LengthShort]':
        """DataScalingReferenceValues[LengthShort]: 'ShortLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1658.LengthShort](temp) if temp is not None else None

    @property
    def short_time_reference_values(self) -> '_1561.DataScalingReferenceValues[_1714.TimeShort]':
        """DataScalingReferenceValues[TimeShort]: 'ShortTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1714.TimeShort](temp) if temp is not None else None

    @property
    def small_angle_reference_values(self) -> '_1561.DataScalingReferenceValues[_1606.AngleSmall]':
        """DataScalingReferenceValues[AngleSmall]: 'SmallAngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1606.AngleSmall](temp) if temp is not None else None

    @property
    def small_energy_reference_values(self) -> '_1561.DataScalingReferenceValues[_1630.EnergySmall]':
        """DataScalingReferenceValues[EnergySmall]: 'SmallEnergyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallEnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1630.EnergySmall](temp) if temp is not None else None

    @property
    def small_velocity_reference_values(self) -> '_1561.DataScalingReferenceValues[_1723.VelocitySmall]':
        """DataScalingReferenceValues[VelocitySmall]: 'SmallVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1723.VelocitySmall](temp) if temp is not None else None

    @property
    def stress_reference_values(self) -> '_1561.DataScalingReferenceValues[_1705.Stress]':
        """DataScalingReferenceValues[Stress]: 'StressReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1705.Stress](temp) if temp is not None else None

    @property
    def temperature_reference_values(self) -> '_1561.DataScalingReferenceValues[_1706.Temperature]':
        """DataScalingReferenceValues[Temperature]: 'TemperatureReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1706.Temperature](temp) if temp is not None else None

    @property
    def torque_converter_inverse_k(self) -> '_1561.DataScalingReferenceValues[_1717.TorqueConverterInverseK]':
        """DataScalingReferenceValues[TorqueConverterInverseK]: 'TorqueConverterInverseK' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverterInverseK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1717.TorqueConverterInverseK](temp) if temp is not None else None

    @property
    def torque_converter_k(self) -> '_1561.DataScalingReferenceValues[_1718.TorqueConverterK]':
        """DataScalingReferenceValues[TorqueConverterK]: 'TorqueConverterK' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverterK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1718.TorqueConverterK](temp) if temp is not None else None

    @property
    def torque_reference_values(self) -> '_1561.DataScalingReferenceValues[_1716.Torque]':
        """DataScalingReferenceValues[Torque]: 'TorqueReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1716.Torque](temp) if temp is not None else None

    @property
    def unmeasureable(self) -> '_1561.DataScalingReferenceValues[_1679.Number]':
        """DataScalingReferenceValues[Number]: 'Unmeasureable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Unmeasureable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1679.Number](temp) if temp is not None else None

    @property
    def velocity_reference_values(self) -> '_1561.DataScalingReferenceValues[_1722.Velocity]':
        """DataScalingReferenceValues[Velocity]: 'VelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1722.Velocity](temp) if temp is not None else None

    @property
    def very_short_length_reference_values(self) -> '_1561.DataScalingReferenceValues[_1661.LengthVeryShort]':
        """DataScalingReferenceValues[LengthVeryShort]: 'VeryShortLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VeryShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1661.LengthVeryShort](temp) if temp is not None else None

    @property
    def very_short_time_reference_values(self) -> '_1561.DataScalingReferenceValues[_1715.TimeVeryShort]':
        """DataScalingReferenceValues[TimeVeryShort]: 'VeryShortTimeReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VeryShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1715.TimeVeryShort](temp) if temp is not None else None

    @property
    def very_small_angle_reference_values(self) -> '_1561.DataScalingReferenceValues[_1607.AngleVerySmall]':
        """DataScalingReferenceValues[AngleVerySmall]: 'VerySmallAngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerySmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1607.AngleVerySmall](temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'DataScalingOptions._Cast_DataScalingOptions':
        return self._Cast_DataScalingOptions(self)
