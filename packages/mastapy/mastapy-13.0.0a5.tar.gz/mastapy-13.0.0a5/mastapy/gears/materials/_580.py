"""_580.py

AGMACylindricalGearMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.materials import _588
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_CYLINDRICAL_GEAR_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'AGMACylindricalGearMaterial')

if TYPE_CHECKING:
    from mastapy.materials import _240, _238, _239


__docformat__ = 'restructuredtext en'
__all__ = ('AGMACylindricalGearMaterial',)


class AGMACylindricalGearMaterial(_588.CylindricalGearMaterial):
    """AGMACylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE = _AGMA_CYLINDRICAL_GEAR_MATERIAL

    class _Cast_AGMACylindricalGearMaterial:
        """Special nested class for casting AGMACylindricalGearMaterial to subclasses."""

        def __init__(self, parent: 'AGMACylindricalGearMaterial'):
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
        def agma_cylindrical_gear_material(self) -> 'AGMACylindricalGearMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMACylindricalGearMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self) -> 'float':
        """float: 'AllowableStressNumberBending' is the original name of this property."""

        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @allowable_stress_number_bending.setter
    def allowable_stress_number_bending(self, value: 'float'):
        self.wrapped.AllowableStressNumberBending = float(value) if value is not None else 0.0

    @property
    def grade(self) -> '_240.AGMAMaterialGrade':
        """AGMAMaterialGrade: 'Grade' is the original name of this property."""

        temp = self.wrapped.Grade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.AGMAMaterialGrade')
        return constructor.new_from_mastapy('mastapy.materials._240', 'AGMAMaterialGrade')(value) if value is not None else None

    @grade.setter
    def grade(self, value: '_240.AGMAMaterialGrade'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.AGMAMaterialGrade')
        self.wrapped.Grade = value

    @property
    def material_application(self) -> '_238.AGMAMaterialApplications':
        """AGMAMaterialApplications: 'MaterialApplication' is the original name of this property."""

        temp = self.wrapped.MaterialApplication

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.AGMAMaterialApplications')
        return constructor.new_from_mastapy('mastapy.materials._238', 'AGMAMaterialApplications')(value) if value is not None else None

    @material_application.setter
    def material_application(self, value: '_238.AGMAMaterialApplications'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.AGMAMaterialApplications')
        self.wrapped.MaterialApplication = value

    @property
    def material_class(self) -> '_239.AGMAMaterialClasses':
        """AGMAMaterialClasses: 'MaterialClass' is the original name of this property."""

        temp = self.wrapped.MaterialClass

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.AGMAMaterialClasses')
        return constructor.new_from_mastapy('mastapy.materials._239', 'AGMAMaterialClasses')(value) if value is not None else None

    @material_class.setter
    def material_class(self, value: '_239.AGMAMaterialClasses'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.AGMAMaterialClasses')
        self.wrapped.MaterialClass = value

    @property
    def stress_cycle_factor_at_1e10_cycles_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StressCycleFactorAt1E10CyclesBending' is the original name of this property."""

        temp = self.wrapped.StressCycleFactorAt1E10CyclesBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @stress_cycle_factor_at_1e10_cycles_bending.setter
    def stress_cycle_factor_at_1e10_cycles_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StressCycleFactorAt1E10CyclesBending = value

    @property
    def stress_cycle_factor_at_1e10_cycles_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StressCycleFactorAt1E10CyclesContact' is the original name of this property."""

        temp = self.wrapped.StressCycleFactorAt1E10CyclesContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @stress_cycle_factor_at_1e10_cycles_contact.setter
    def stress_cycle_factor_at_1e10_cycles_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StressCycleFactorAt1E10CyclesContact = value

    @property
    def cast_to(self) -> 'AGMACylindricalGearMaterial._Cast_AGMACylindricalGearMaterial':
        return self._Cast_AGMACylindricalGearMaterial(self)
