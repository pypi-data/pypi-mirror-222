﻿"""_600.py

PlasticCylindricalGearMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.materials import _588
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_CYLINDRICAL_GEAR_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'PlasticCylindricalGearMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticCylindricalGearMaterial',)


class PlasticCylindricalGearMaterial(_588.CylindricalGearMaterial):
    """PlasticCylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE = _PLASTIC_CYLINDRICAL_GEAR_MATERIAL

    class _Cast_PlasticCylindricalGearMaterial:
        """Special nested class for casting PlasticCylindricalGearMaterial to subclasses."""

        def __init__(self, parent: 'PlasticCylindricalGearMaterial'):
            self._parent = parent

        @property
        def cylindrical_gear_material(self):
            return self._parent._cast(_588.CylindricalGearMaterial)

        @property
        def gear_material(self):
            from mastapy.gears.materials import _591
            
            return self._parent._cast(_591.GearMaterial)

        @property
        def material(self):
            from mastapy.materials import _267
            
            return self._parent._cast(_267.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def plastic_cylindrical_gear_material(self) -> 'PlasticCylindricalGearMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticCylindricalGearMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def glass_transition_temperature(self) -> 'float':
        """float: 'GlassTransitionTemperature' is the original name of this property."""

        temp = self.wrapped.GlassTransitionTemperature

        if temp is None:
            return 0.0

        return temp

    @glass_transition_temperature.setter
    def glass_transition_temperature(self, value: 'float'):
        self.wrapped.GlassTransitionTemperature = float(value) if value is not None else 0.0

    @property
    def material_type(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'MaterialType' is the original name of this property."""

        temp = self.wrapped.MaterialType

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @material_type.setter
    def material_type(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.MaterialType = value

    @property
    def melting_temperature(self) -> 'float':
        """float: 'MeltingTemperature' is the original name of this property."""

        temp = self.wrapped.MeltingTemperature

        if temp is None:
            return 0.0

        return temp

    @melting_temperature.setter
    def melting_temperature(self, value: 'float'):
        self.wrapped.MeltingTemperature = float(value) if value is not None else 0.0

    @property
    def modulus_of_elasticity(self) -> 'float':
        """float: 'ModulusOfElasticity' is the original name of this property."""

        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity.setter
    def modulus_of_elasticity(self, value: 'float'):
        self.wrapped.ModulusOfElasticity = float(value) if value is not None else 0.0

    @property
    def n0_bending(self) -> 'float':
        """float: 'N0Bending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.N0Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def n0_contact(self) -> 'float':
        """float: 'N0Contact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.N0Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_temperature_for_continuous_operation(self) -> 'float':
        """float: 'PermissibleTemperatureForContinuousOperation' is the original name of this property."""

        temp = self.wrapped.PermissibleTemperatureForContinuousOperation

        if temp is None:
            return 0.0

        return temp

    @permissible_temperature_for_continuous_operation.setter
    def permissible_temperature_for_continuous_operation(self, value: 'float'):
        self.wrapped.PermissibleTemperatureForContinuousOperation = float(value) if value is not None else 0.0

    @property
    def permissible_temperature_for_intermittent_operation(self) -> 'float':
        """float: 'PermissibleTemperatureForIntermittentOperation' is the original name of this property."""

        temp = self.wrapped.PermissibleTemperatureForIntermittentOperation

        if temp is None:
            return 0.0

        return temp

    @permissible_temperature_for_intermittent_operation.setter
    def permissible_temperature_for_intermittent_operation(self, value: 'float'):
        self.wrapped.PermissibleTemperatureForIntermittentOperation = float(value) if value is not None else 0.0

    @property
    def use_custom_material_for_bending(self) -> 'bool':
        """bool: 'UseCustomMaterialForBending' is the original name of this property."""

        temp = self.wrapped.UseCustomMaterialForBending

        if temp is None:
            return False

        return temp

    @use_custom_material_for_bending.setter
    def use_custom_material_for_bending(self, value: 'bool'):
        self.wrapped.UseCustomMaterialForBending = bool(value) if value is not None else False

    @property
    def use_custom_material_for_contact(self) -> 'bool':
        """bool: 'UseCustomMaterialForContact' is the original name of this property."""

        temp = self.wrapped.UseCustomMaterialForContact

        if temp is None:
            return False

        return temp

    @use_custom_material_for_contact.setter
    def use_custom_material_for_contact(self, value: 'bool'):
        self.wrapped.UseCustomMaterialForContact = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial':
        return self._Cast_PlasticCylindricalGearMaterial(self)
