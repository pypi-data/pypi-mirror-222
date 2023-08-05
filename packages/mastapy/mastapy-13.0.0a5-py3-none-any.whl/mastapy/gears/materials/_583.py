"""_583.py

BevelGearISOMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _581, _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ISO_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearISOMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearISOMaterialDatabase',)


class BevelGearISOMaterialDatabase(_581.BevelGearAbstractMaterialDatabase['_582.BevelGearISOMaterial']):
    """BevelGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ISO_MATERIAL_DATABASE

    class _Cast_BevelGearISOMaterialDatabase:
        """Special nested class for casting BevelGearISOMaterialDatabase to subclasses."""

        def __init__(self, parent: 'BevelGearISOMaterialDatabase'):
            self._parent = parent

        @property
        def bevel_gear_abstract_material_database(self):
            return self._parent._cast(_581.BevelGearAbstractMaterialDatabase)

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
        def bevel_gear_iso_material_database(self) -> 'BevelGearISOMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearISOMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearISOMaterialDatabase._Cast_BevelGearISOMaterialDatabase':
        return self._Cast_BevelGearISOMaterialDatabase(self)
