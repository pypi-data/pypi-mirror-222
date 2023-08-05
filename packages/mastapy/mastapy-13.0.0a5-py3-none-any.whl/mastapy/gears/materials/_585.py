"""_585.py

BevelGearMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _592, _584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMaterialDatabase',)


class BevelGearMaterialDatabase(_592.GearMaterialDatabase['_584.BevelGearMaterial']):
    """BevelGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL_DATABASE

    class _Cast_BevelGearMaterialDatabase:
        """Special nested class for casting BevelGearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BevelGearMaterialDatabase'):
            self._parent = parent

        @property
        def gear_material_database(self):
            return self._parent._cast(_592.GearMaterialDatabase)

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
        def bevel_gear_material_database(self) -> 'BevelGearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase':
        return self._Cast_BevelGearMaterialDatabase(self)
