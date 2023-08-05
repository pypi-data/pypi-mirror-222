﻿"""_2449.py

OilSeal
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2430
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.materials.efficiency import _298, _299
    from mastapy.bearings.bearing_results import _1947


__docformat__ = 'restructuredtext en'
__all__ = ('OilSeal',)


class OilSeal(_2430.Connector):
    """OilSeal

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL

    class _Cast_OilSeal:
        """Special nested class for casting OilSeal to subclasses."""

        def __init__(self, parent: 'OilSeal'):
            self._parent = parent

        @property
        def connector(self):
            return self._parent._cast(_2430.Connector)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def oil_seal(self) -> 'OilSeal':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OilSeal.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def drag_torque_vs_rotational_speed(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'DragTorqueVsRotationalSpeed' is the original name of this property."""

        temp = self.wrapped.DragTorqueVsRotationalSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @drag_torque_vs_rotational_speed.setter
    def drag_torque_vs_rotational_speed(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.DragTorqueVsRotationalSpeed = value

    @property
    def intercept_of_linear_equation_defining_the_effect_of_temperature(self) -> 'float':
        """float: 'InterceptOfLinearEquationDefiningTheEffectOfTemperature' is the original name of this property."""

        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfTemperature

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation_defining_the_effect_of_temperature.setter
    def intercept_of_linear_equation_defining_the_effect_of_temperature(self, value: 'float'):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfTemperature = float(value) if value is not None else 0.0

    @property
    def oil_seal_characteristic_life(self) -> 'float':
        """float: 'OilSealCharacteristicLife' is the original name of this property."""

        temp = self.wrapped.OilSealCharacteristicLife

        if temp is None:
            return 0.0

        return temp

    @oil_seal_characteristic_life.setter
    def oil_seal_characteristic_life(self, value: 'float'):
        self.wrapped.OilSealCharacteristicLife = float(value) if value is not None else 0.0

    @property
    def oil_seal_frictional_torque(self) -> 'float':
        """float: 'OilSealFrictionalTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSealFrictionalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_seal_loss_calculation_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod':
        """enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod: 'OilSealLossCalculationMethod' is the original name of this property."""

        temp = self.wrapped.OilSealLossCalculationMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @oil_seal_loss_calculation_method.setter
    def oil_seal_loss_calculation_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.OilSealLossCalculationMethod = value

    @property
    def oil_seal_material(self) -> '_299.OilSealMaterialType':
        """OilSealMaterialType: 'OilSealMaterial' is the original name of this property."""

        temp = self.wrapped.OilSealMaterial

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.Efficiency.OilSealMaterialType')
        return constructor.new_from_mastapy('mastapy.materials.efficiency._299', 'OilSealMaterialType')(value) if value is not None else None

    @oil_seal_material.setter
    def oil_seal_material(self, value: '_299.OilSealMaterialType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.Efficiency.OilSealMaterialType')
        self.wrapped.OilSealMaterial = value

    @property
    def oil_seal_mean_time_before_failure(self) -> 'float':
        """float: 'OilSealMeanTimeBeforeFailure' is the original name of this property."""

        temp = self.wrapped.OilSealMeanTimeBeforeFailure

        if temp is None:
            return 0.0

        return temp

    @oil_seal_mean_time_before_failure.setter
    def oil_seal_mean_time_before_failure(self, value: 'float'):
        self.wrapped.OilSealMeanTimeBeforeFailure = float(value) if value is not None else 0.0

    @property
    def oil_seal_orientation(self) -> '_1947.Orientations':
        """Orientations: 'OilSealOrientation' is the original name of this property."""

        temp = self.wrapped.OilSealOrientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingResults.Orientations')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_results._1947', 'Orientations')(value) if value is not None else None

    @oil_seal_orientation.setter
    def oil_seal_orientation(self, value: '_1947.Orientations'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingResults.Orientations')
        self.wrapped.OilSealOrientation = value

    @property
    def slope_of_linear_equation_defining_the_effect_of_temperature(self) -> 'float':
        """float: 'SlopeOfLinearEquationDefiningTheEffectOfTemperature' is the original name of this property."""

        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfTemperature

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation_defining_the_effect_of_temperature.setter
    def slope_of_linear_equation_defining_the_effect_of_temperature(self, value: 'float'):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfTemperature = float(value) if value is not None else 0.0

    @property
    def width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @width.setter
    def width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Width = value

    @property
    def cast_to(self) -> 'OilSeal._Cast_OilSeal':
        return self._Cast_OilSeal(self)
