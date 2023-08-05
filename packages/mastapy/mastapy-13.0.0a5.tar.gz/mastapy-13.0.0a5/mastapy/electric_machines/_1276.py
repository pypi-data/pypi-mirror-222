"""_1276.py

MagnetMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.materials import _268
from mastapy.electric_machines import _1275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetMaterialDatabase',)


class MagnetMaterialDatabase(_268.MaterialDatabase['_1275.MagnetMaterial']):
    """MagnetMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL_DATABASE

    class _Cast_MagnetMaterialDatabase:
        """Special nested class for casting MagnetMaterialDatabase to subclasses."""

        def __init__(self, parent: 'MagnetMaterialDatabase'):
            self._parent = parent

        @property
        def material_database(self):
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
        def magnet_material_database(self) -> 'MagnetMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagnetMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MagnetMaterialDatabase._Cast_MagnetMaterialDatabase':
        return self._Cast_MagnetMaterialDatabase(self)
