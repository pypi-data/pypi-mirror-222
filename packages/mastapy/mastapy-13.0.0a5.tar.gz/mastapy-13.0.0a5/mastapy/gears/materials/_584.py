"""_584.py

BevelGearMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.materials import _591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearMaterial')

if TYPE_CHECKING:
    from mastapy.gears.materials import _605


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMaterial',)


class BevelGearMaterial(_591.GearMaterial):
    """BevelGearMaterial

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL

    class _Cast_BevelGearMaterial:
        """Special nested class for casting BevelGearMaterial to subclasses."""

        def __init__(self, parent: 'BevelGearMaterial'):
            self._parent = parent

        @property
        def gear_material(self):
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
        def bevel_gear_iso_material(self):
            from mastapy.gears.materials import _582
            
            return self._parent._cast(_582.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self) -> 'BevelGearMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMaterial.TYPE'):
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
    def sn_curve_definition(self) -> '_605.SNCurveDefinition':
        """SNCurveDefinition: 'SNCurveDefinition' is the original name of this property."""

        temp = self.wrapped.SNCurveDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Materials.SNCurveDefinition')
        return constructor.new_from_mastapy('mastapy.gears.materials._605', 'SNCurveDefinition')(value) if value is not None else None

    @sn_curve_definition.setter
    def sn_curve_definition(self, value: '_605.SNCurveDefinition'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Materials.SNCurveDefinition')
        self.wrapped.SNCurveDefinition = value

    @property
    def thermal_constant(self) -> 'float':
        """float: 'ThermalConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermalConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BevelGearMaterial._Cast_BevelGearMaterial':
        return self._Cast_BevelGearMaterial(self)
