﻿"""_1007.py

CylindricalGearCuttingOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CUTTING_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearCuttingOptions')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1046, _1003, _1028
    from mastapy.gears.manufacturing.cylindrical import _609


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCuttingOptions',)


class CylindricalGearCuttingOptions(_0.APIBase):
    """CylindricalGearCuttingOptions

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CUTTING_OPTIONS

    class _Cast_CylindricalGearCuttingOptions:
        """Special nested class for casting CylindricalGearCuttingOptions to subclasses."""

        def __init__(self, parent: 'CylindricalGearCuttingOptions'):
            self._parent = parent

        @property
        def cylindrical_gear_cutting_options(self) -> 'CylindricalGearCuttingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearCuttingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_specification_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType':
        """enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType: 'GeometrySpecificationType' is the original name of this property."""

        temp = self.wrapped.GeometrySpecificationType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @geometry_specification_type.setter
    def geometry_specification_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.GeometrySpecificationType = value

    @property
    def thickness_for_analyses(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ThicknessForAnalyses' is the original name of this property."""

        temp = self.wrapped.ThicknessForAnalyses

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @thickness_for_analyses.setter
    def thickness_for_analyses(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ThicknessForAnalyses = value

    @property
    def use_design_default_toleranced_measurement(self) -> 'bool':
        """bool: 'UseDesignDefaultTolerancedMeasurement' is the original name of this property."""

        temp = self.wrapped.UseDesignDefaultTolerancedMeasurement

        if temp is None:
            return False

        return temp

    @use_design_default_toleranced_measurement.setter
    def use_design_default_toleranced_measurement(self, value: 'bool'):
        self.wrapped.UseDesignDefaultTolerancedMeasurement = bool(value) if value is not None else False

    @property
    def cylindrical_gear_cutter(self) -> '_1003.CylindricalGearAbstractRack':
        """CylindricalGearAbstractRack: 'CylindricalGearCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_configuration(self) -> '_609.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_configuration_selection(self) -> '_1028.CylindricalGearSetManufacturingConfigurationSelection':
        """CylindricalGearSetManufacturingConfigurationSelection: 'ManufacturingConfigurationSelection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfigurationSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearCuttingOptions._Cast_CylindricalGearCuttingOptions':
        return self._Cast_CylindricalGearCuttingOptions(self)
