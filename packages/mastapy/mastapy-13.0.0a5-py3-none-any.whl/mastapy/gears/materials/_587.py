"""_587.py

CylindricalGearISOMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _589, _594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearISOMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearISOMaterialDatabase',)


class CylindricalGearISOMaterialDatabase(_589.CylindricalGearMaterialDatabase['_594.ISOCylindricalGearMaterial']):
    """CylindricalGearISOMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE

    class _Cast_CylindricalGearISOMaterialDatabase:
        """Special nested class for casting CylindricalGearISOMaterialDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearISOMaterialDatabase'):
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
        def cylindrical_gear_iso_material_database(self) -> 'CylindricalGearISOMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearISOMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearISOMaterialDatabase._Cast_CylindricalGearISOMaterialDatabase':
        return self._Cast_CylindricalGearISOMaterialDatabase(self)
