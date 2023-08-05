"""_247.py

ComponentMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.materials import _267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'ComponentMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentMaterialDatabase',)


class ComponentMaterialDatabase(_1817.NamedDatabase['_267.Material']):
    """ComponentMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MATERIAL_DATABASE

    class _Cast_ComponentMaterialDatabase:
        """Special nested class for casting ComponentMaterialDatabase to subclasses."""

        def __init__(self, parent: 'ComponentMaterialDatabase'):
            self._parent = parent

        @property
        def named_database(self):
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
        def component_material_database(self) -> 'ComponentMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ComponentMaterialDatabase._Cast_ComponentMaterialDatabase':
        return self._Cast_ComponentMaterialDatabase(self)
