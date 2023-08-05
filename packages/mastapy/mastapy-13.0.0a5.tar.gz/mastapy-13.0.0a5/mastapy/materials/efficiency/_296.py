"""_296.py

OilPumpDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility import _1577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_PUMP_DETAIL = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'OilPumpDetail')

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.materials.efficiency import _297


__docformat__ = 'restructuredtext en'
__all__ = ('OilPumpDetail',)


class OilPumpDetail(_1577.IndependentReportablePropertiesBase['OilPumpDetail']):
    """OilPumpDetail

    This is a mastapy class.
    """

    TYPE = _OIL_PUMP_DETAIL

    class _Cast_OilPumpDetail:
        """Special nested class for casting OilPumpDetail to subclasses."""

        def __init__(self, parent: 'OilPumpDetail'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.materials.efficiency import _296
            
            return self._parent._cast(_1577.IndependentReportablePropertiesBase)

        @property
        def oil_pump_detail(self) -> 'OilPumpDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OilPumpDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_motor_efficiency(self) -> 'float':
        """float: 'ElectricMotorEfficiency' is the original name of this property."""

        temp = self.wrapped.ElectricMotorEfficiency

        if temp is None:
            return 0.0

        return temp

    @electric_motor_efficiency.setter
    def electric_motor_efficiency(self, value: 'float'):
        self.wrapped.ElectricMotorEfficiency = float(value) if value is not None else 0.0

    @property
    def electric_power_consumed_vs_speed(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'ElectricPowerConsumedVsSpeed' is the original name of this property."""

        temp = self.wrapped.ElectricPowerConsumedVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @electric_power_consumed_vs_speed.setter
    def electric_power_consumed_vs_speed(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.ElectricPowerConsumedVsSpeed = value

    @property
    def oil_flow_rate_vs_speed(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'OilFlowRateVsSpeed' is the original name of this property."""

        temp = self.wrapped.OilFlowRateVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @oil_flow_rate_vs_speed.setter
    def oil_flow_rate_vs_speed(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.OilFlowRateVsSpeed = value

    @property
    def oil_pump_drive_type(self) -> '_297.OilPumpDriveType':
        """OilPumpDriveType: 'OilPumpDriveType' is the original name of this property."""

        temp = self.wrapped.OilPumpDriveType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.Efficiency.OilPumpDriveType')
        return constructor.new_from_mastapy('mastapy.materials.efficiency._297', 'OilPumpDriveType')(value) if value is not None else None

    @oil_pump_drive_type.setter
    def oil_pump_drive_type(self, value: '_297.OilPumpDriveType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.Efficiency.OilPumpDriveType')
        self.wrapped.OilPumpDriveType = value

    @property
    def oil_pump_efficiency(self) -> 'float':
        """float: 'OilPumpEfficiency' is the original name of this property."""

        temp = self.wrapped.OilPumpEfficiency

        if temp is None:
            return 0.0

        return temp

    @oil_pump_efficiency.setter
    def oil_pump_efficiency(self, value: 'float'):
        self.wrapped.OilPumpEfficiency = float(value) if value is not None else 0.0

    @property
    def operating_oil_pressure_vs_speed(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'OperatingOilPressureVsSpeed' is the original name of this property."""

        temp = self.wrapped.OperatingOilPressureVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @operating_oil_pressure_vs_speed.setter
    def operating_oil_pressure_vs_speed(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.OperatingOilPressureVsSpeed = value

    @property
    def cast_to(self) -> 'OilPumpDetail._Cast_OilPumpDetail':
        return self._Cast_OilPumpDetail(self)
