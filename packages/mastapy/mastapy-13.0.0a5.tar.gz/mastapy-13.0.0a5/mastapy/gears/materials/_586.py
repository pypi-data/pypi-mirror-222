"""_586.py

CylindricalGearAGMAMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _589, _580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_AGMA_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearAGMAMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAGMAMaterialDatabase',)


class CylindricalGearAGMAMaterialDatabase(_589.CylindricalGearMaterialDatabase['_580.AGMACylindricalGearMaterial']):
    """CylindricalGearAGMAMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_AGMA_MATERIAL_DATABASE

    class _Cast_CylindricalGearAGMAMaterialDatabase:
        """Special nested class for casting CylindricalGearAGMAMaterialDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearAGMAMaterialDatabase'):
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
        def cylindrical_gear_agma_material_database(self) -> 'CylindricalGearAGMAMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearAGMAMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearAGMAMaterialDatabase._Cast_CylindricalGearAGMAMaterialDatabase':
        return self._Cast_CylindricalGearAGMAMaterialDatabase(self)
