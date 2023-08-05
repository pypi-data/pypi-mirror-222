"""_2589.py

TorqueConverter
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590, _2592


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverter',)


class TorqueConverter(_2565.Coupling):
    """TorqueConverter

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER

    class _Cast_TorqueConverter:
        """Special nested class for casting TorqueConverter to subclasses."""

        def __init__(self, parent: 'TorqueConverter'):
            self._parent = parent

        @property
        def coupling(self):
            return self._parent._cast(_2565.Coupling)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def torque_converter(self) -> 'TorqueConverter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_to_oil_heat_transfer_coefficient(self) -> 'float':
        """float: 'ClutchToOilHeatTransferCoefficient' is the original name of this property."""

        temp = self.wrapped.ClutchToOilHeatTransferCoefficient

        if temp is None:
            return 0.0

        return temp

    @clutch_to_oil_heat_transfer_coefficient.setter
    def clutch_to_oil_heat_transfer_coefficient(self, value: 'float'):
        self.wrapped.ClutchToOilHeatTransferCoefficient = float(value) if value is not None else 0.0

    @property
    def has_lock_up_clutch(self) -> 'bool':
        """bool: 'HasLockUpClutch' is the original name of this property."""

        temp = self.wrapped.HasLockUpClutch

        if temp is None:
            return False

        return temp

    @has_lock_up_clutch.setter
    def has_lock_up_clutch(self, value: 'bool'):
        self.wrapped.HasLockUpClutch = bool(value) if value is not None else False

    @property
    def heat_transfer_area(self) -> 'float':
        """float: 'HeatTransferArea' is the original name of this property."""

        temp = self.wrapped.HeatTransferArea

        if temp is None:
            return 0.0

        return temp

    @heat_transfer_area.setter
    def heat_transfer_area(self, value: 'float'):
        self.wrapped.HeatTransferArea = float(value) if value is not None else 0.0

    @property
    def specific_heat_capacity(self) -> 'float':
        """float: 'SpecificHeatCapacity' is the original name of this property."""

        temp = self.wrapped.SpecificHeatCapacity

        if temp is None:
            return 0.0

        return temp

    @specific_heat_capacity.setter
    def specific_heat_capacity(self, value: 'float'):
        self.wrapped.SpecificHeatCapacity = float(value) if value is not None else 0.0

    @property
    def static_to_dynamic_friction_ratio(self) -> 'float':
        """float: 'StaticToDynamicFrictionRatio' is the original name of this property."""

        temp = self.wrapped.StaticToDynamicFrictionRatio

        if temp is None:
            return 0.0

        return temp

    @static_to_dynamic_friction_ratio.setter
    def static_to_dynamic_friction_ratio(self, value: 'float'):
        self.wrapped.StaticToDynamicFrictionRatio = float(value) if value is not None else 0.0

    @property
    def thermal_mass(self) -> 'float':
        """float: 'ThermalMass' is the original name of this property."""

        temp = self.wrapped.ThermalMass

        if temp is None:
            return 0.0

        return temp

    @thermal_mass.setter
    def thermal_mass(self, value: 'float'):
        self.wrapped.ThermalMass = float(value) if value is not None else 0.0

    @property
    def tolerance_for_speed_ratio_of_unity(self) -> 'float':
        """float: 'ToleranceForSpeedRatioOfUnity' is the original name of this property."""

        temp = self.wrapped.ToleranceForSpeedRatioOfUnity

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_speed_ratio_of_unity.setter
    def tolerance_for_speed_ratio_of_unity(self, value: 'float'):
        self.wrapped.ToleranceForSpeedRatioOfUnity = float(value) if value is not None else 0.0

    @property
    def torque_capacity(self) -> 'float':
        """float: 'TorqueCapacity' is the original name of this property."""

        temp = self.wrapped.TorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @torque_capacity.setter
    def torque_capacity(self, value: 'float'):
        self.wrapped.TorqueCapacity = float(value) if value is not None else 0.0

    @property
    def pump(self) -> '_2590.TorqueConverterPump':
        """TorqueConverterPump: 'Pump' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Pump

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def turbine(self) -> '_2592.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'Turbine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Turbine

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverter._Cast_TorqueConverter':
        return self._Cast_TorqueConverter(self)
