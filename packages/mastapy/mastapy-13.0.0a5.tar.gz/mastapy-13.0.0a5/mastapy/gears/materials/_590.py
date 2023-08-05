"""_590.py

CylindricalGearPlasticMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _589, _600
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearPlasticMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlasticMaterialDatabase',)


class CylindricalGearPlasticMaterialDatabase(_589.CylindricalGearMaterialDatabase['_600.PlasticCylindricalGearMaterial']):
    """CylindricalGearPlasticMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE

    class _Cast_CylindricalGearPlasticMaterialDatabase:
        """Special nested class for casting CylindricalGearPlasticMaterialDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearPlasticMaterialDatabase'):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(self):
            return self._parent._cast(_589.CylindricalGearMaterialDatabase)

        @property
        def material_database(self):
            from mastapy.materials import _268
            
            return self._parent._cast(_268.MaterialDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1817
            
            return self._parent._cast(_1817.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1820, _1819
            
            return self._parent._cast(_1820.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1813, _1819
            
            return self._parent._cast(_1813.Database)

        @property
        def cylindrical_gear_plastic_material_database(self) -> 'CylindricalGearPlasticMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearPlasticMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase':
        return self._Cast_CylindricalGearPlasticMaterialDatabase(self)
