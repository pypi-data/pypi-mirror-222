﻿"""_2508.py

CylindricalGearSet
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model.gears import _2514
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')

if TYPE_CHECKING:
    from mastapy.gears import _320
    from mastapy.gears.gear_designs.cylindrical import _1025
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2545
    from mastapy.system_model.part_model.gears import _2507
    from mastapy.system_model.connections_and_sockets.gears import _2292


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSet',)


class CylindricalGearSet(_2514.GearSet):
    """CylindricalGearSet

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET

    class _Cast_CylindricalGearSet:
        """Special nested class for casting CylindricalGearSet to subclasses."""

        def __init__(self, parent: 'CylindricalGearSet'):
            self._parent = parent

        @property
        def gear_set(self):
            return self._parent._cast(_2514.GearSet)

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
        def planetary_gear_set(self):
            from mastapy.system_model.part_model.gears import _2524
            
            return self._parent._cast(_2524.PlanetaryGearSet)

        @property
        def cylindrical_gear_set(self) -> 'CylindricalGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_requirement(self) -> 'overridable.Overridable_ContactRatioRequirements':
        """overridable.Overridable_ContactRatioRequirements: 'AxialContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @axial_contact_ratio_requirement.setter
    def axial_contact_ratio_requirement(self, value: 'overridable.Overridable_ContactRatioRequirements.implicit_type()'):
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def is_supercharger_rotor_set(self) -> 'bool':
        """bool: 'IsSuperchargerRotorSet' is the original name of this property."""

        temp = self.wrapped.IsSuperchargerRotorSet

        if temp is None:
            return False

        return temp

    @is_supercharger_rotor_set.setter
    def is_supercharger_rotor_set(self, value: 'bool'):
        self.wrapped.IsSuperchargerRotorSet = bool(value) if value is not None else False

    @property
    def maximum_acceptable_axial_contact_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_acceptable_axial_contact_ratio.setter
    def maximum_acceptable_axial_contact_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumAcceptableAxialContactRatio = value

    @property
    def maximum_acceptable_axial_contact_ratio_above_integer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumAcceptableAxialContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_acceptable_axial_contact_ratio_above_integer.setter
    def maximum_acceptable_axial_contact_ratio_above_integer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger = value

    @property
    def maximum_acceptable_transverse_contact_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_acceptable_transverse_contact_ratio.setter
    def maximum_acceptable_transverse_contact_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumAcceptableTransverseContactRatio = value

    @property
    def maximum_acceptable_transverse_contact_ratio_above_integer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumAcceptableTransverseContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_acceptable_transverse_contact_ratio_above_integer.setter
    def maximum_acceptable_transverse_contact_ratio_above_integer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger = value

    @property
    def maximum_helix_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumHelixAngle' is the original name of this property."""

        temp = self.wrapped.MaximumHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_helix_angle.setter
    def maximum_helix_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumHelixAngle = value

    @property
    def maximum_normal_module(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumNormalModule' is the original name of this property."""

        temp = self.wrapped.MaximumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @maximum_normal_module.setter
    def maximum_normal_module(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumNormalModule = value

    @property
    def minimum_acceptable_axial_contact_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_acceptable_axial_contact_ratio.setter
    def minimum_acceptable_axial_contact_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumAcceptableAxialContactRatio = value

    @property
    def minimum_acceptable_axial_contact_ratio_below_integer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumAcceptableAxialContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_acceptable_axial_contact_ratio_below_integer.setter
    def minimum_acceptable_axial_contact_ratio_below_integer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger = value

    @property
    def minimum_acceptable_transverse_contact_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_acceptable_transverse_contact_ratio.setter
    def minimum_acceptable_transverse_contact_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumAcceptableTransverseContactRatio = value

    @property
    def minimum_acceptable_transverse_contact_ratio_below_integer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumAcceptableTransverseContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_acceptable_transverse_contact_ratio_below_integer.setter
    def minimum_acceptable_transverse_contact_ratio_below_integer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger = value

    @property
    def minimum_normal_module(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumNormalModule' is the original name of this property."""

        temp = self.wrapped.MinimumNormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @minimum_normal_module.setter
    def minimum_normal_module(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumNormalModule = value

    @property
    def supercharger_rotor_set_database(self) -> 'str':
        """str: 'SuperchargerRotorSetDatabase' is the original name of this property."""

        temp = self.wrapped.SuperchargerRotorSetDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @supercharger_rotor_set_database.setter
    def supercharger_rotor_set_database(self, value: 'str'):
        self.wrapped.SuperchargerRotorSetDatabase.SetSelectedItem(str(value) if value is not None else '')

    @property
    def transverse_contact_ratio_requirement(self) -> 'overridable.Overridable_ContactRatioRequirements':
        """overridable.Overridable_ContactRatioRequirements: 'TransverseContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = overridable.Overridable_ContactRatioRequirements.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @transverse_contact_ratio_requirement.setter
    def transverse_contact_ratio_requirement(self, value: 'overridable.Overridable_ContactRatioRequirements.implicit_type()'):
        wrapper_type = overridable.Overridable_ContactRatioRequirements.wrapper_type()
        enclosed_type = overridable.Overridable_ContactRatioRequirements.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def active_gear_set_design(self) -> '_1025.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_design(self) -> '_1025.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_set(self) -> '_2545.SuperchargerRotorSet':
        """SuperchargerRotorSet: 'SuperchargerRotorSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears(self) -> 'List[_2507.CylindricalGear]':
        """List[CylindricalGear]: 'CylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes(self) -> 'List[_2292.CylindricalGearMesh]':
        """List[CylindricalGearMesh]: 'CylindricalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_designs(self) -> 'List[_1025.CylindricalGearSetDesign]':
        """List[CylindricalGearSetDesign]: 'GearSetDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_gear(self) -> '_2507.CylindricalGear':
        """ 'AddGear' is the original name of this method.

        Returns:
            mastapy.system_model.part_model.gears.CylindricalGear
        """

        method_result = self.wrapped.AddGear()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearSet._Cast_CylindricalGearSet':
        return self._Cast_CylindricalGearSet(self)
