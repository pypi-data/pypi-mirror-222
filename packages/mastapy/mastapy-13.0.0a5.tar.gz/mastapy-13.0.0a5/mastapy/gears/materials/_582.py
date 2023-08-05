﻿"""_582.py

BevelGearISOMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.materials import _584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ISO_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearISOMaterial')

if TYPE_CHECKING:
    from mastapy.materials import _276


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearISOMaterial',)


class BevelGearISOMaterial(_584.BevelGearMaterial):
    """BevelGearISOMaterial

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ISO_MATERIAL

    class _Cast_BevelGearISOMaterial:
        """Special nested class for casting BevelGearISOMaterial to subclasses."""

        def __init__(self, parent: 'BevelGearISOMaterial'):
            self._parent = parent

        @property
        def bevel_gear_material(self):
            return self._parent._cast(_584.BevelGearMaterial)

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
        def bevel_gear_iso_material(self) -> 'BevelGearISOMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearISOMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self) -> 'float':
        """float: 'AllowableBendingStress' is the original name of this property."""

        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @allowable_bending_stress.setter
    def allowable_bending_stress(self, value: 'float'):
        self.wrapped.AllowableBendingStress = float(value) if value is not None else 0.0

    @property
    def allowable_contact_stress(self) -> 'float':
        """float: 'AllowableContactStress' is the original name of this property."""

        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @allowable_contact_stress.setter
    def allowable_contact_stress(self, value: 'float'):
        self.wrapped.AllowableContactStress = float(value) if value is not None else 0.0

    @property
    def iso_material_type(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ISOMaterialType' is the original name of this property."""

        temp = self.wrapped.ISOMaterialType

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @iso_material_type.setter
    def iso_material_type(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ISOMaterialType = value

    @property
    def limited_pitting_allowed(self) -> 'bool':
        """bool: 'LimitedPittingAllowed' is the original name of this property."""

        temp = self.wrapped.LimitedPittingAllowed

        if temp is None:
            return False

        return temp

    @limited_pitting_allowed.setter
    def limited_pitting_allowed(self, value: 'bool'):
        self.wrapped.LimitedPittingAllowed = bool(value) if value is not None else False

    @property
    def long_life_life_factor_bending(self) -> 'float':
        """float: 'LongLifeLifeFactorBending' is the original name of this property."""

        temp = self.wrapped.LongLifeLifeFactorBending

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_bending.setter
    def long_life_life_factor_bending(self, value: 'float'):
        self.wrapped.LongLifeLifeFactorBending = float(value) if value is not None else 0.0

    @property
    def long_life_life_factor_contact(self) -> 'float':
        """float: 'LongLifeLifeFactorContact' is the original name of this property."""

        temp = self.wrapped.LongLifeLifeFactorContact

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_contact.setter
    def long_life_life_factor_contact(self, value: 'float'):
        self.wrapped.LongLifeLifeFactorContact = float(value) if value is not None else 0.0

    @property
    def material_has_a_well_defined_yield_point(self) -> 'bool':
        """bool: 'MaterialHasAWellDefinedYieldPoint' is the original name of this property."""

        temp = self.wrapped.MaterialHasAWellDefinedYieldPoint

        if temp is None:
            return False

        return temp

    @material_has_a_well_defined_yield_point.setter
    def material_has_a_well_defined_yield_point(self, value: 'bool'):
        self.wrapped.MaterialHasAWellDefinedYieldPoint = bool(value) if value is not None else False

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
    def proof_stress(self) -> 'float':
        """float: 'ProofStress' is the original name of this property."""

        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    def proof_stress(self, value: 'float'):
        self.wrapped.ProofStress = float(value) if value is not None else 0.0

    @property
    def quality_grade(self) -> '_276.QualityGrade':
        """QualityGrade: 'QualityGrade' is the original name of this property."""

        temp = self.wrapped.QualityGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.QualityGrade')
        return constructor.new_from_mastapy('mastapy.materials._276', 'QualityGrade')(value) if value is not None else None

    @quality_grade.setter
    def quality_grade(self, value: '_276.QualityGrade'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.QualityGrade')
        self.wrapped.QualityGrade = value

    @property
    def specify_allowable_stress_numbers(self) -> 'bool':
        """bool: 'SpecifyAllowableStressNumbers' is the original name of this property."""

        temp = self.wrapped.SpecifyAllowableStressNumbers

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_numbers.setter
    def specify_allowable_stress_numbers(self, value: 'bool'):
        self.wrapped.SpecifyAllowableStressNumbers = bool(value) if value is not None else False

    @property
    def use_iso633652003_material_definitions(self) -> 'bool':
        """bool: 'UseISO633652003MaterialDefinitions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UseISO633652003MaterialDefinitions

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'BevelGearISOMaterial._Cast_BevelGearISOMaterial':
        return self._Cast_BevelGearISOMaterial(self)
