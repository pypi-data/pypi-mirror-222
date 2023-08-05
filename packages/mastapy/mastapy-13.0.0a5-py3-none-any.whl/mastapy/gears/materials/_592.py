"""_592.py

GearMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1817
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'GearMaterialDatabase')

if TYPE_CHECKING:
    from mastapy.gears.materials import _591


__docformat__ = 'restructuredtext en'
__all__ = ('GearMaterialDatabase',)


T = TypeVar('T', bound='_591.GearMaterial')


class GearMaterialDatabase(_1817.NamedDatabase[T]):
    """GearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_MATERIAL_DATABASE

    class _Cast_GearMaterialDatabase:
        """Special nested class for casting GearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'GearMaterialDatabase'):
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
        def bevel_gear_material_database(self):
            from mastapy.gears.materials import _585
            
            return self._parent._cast(_585.BevelGearMaterialDatabase)

        @property
        def klingelnberg_conical_gear_material_database(self):
            from mastapy.gears.materials import _597
            
            return self._parent._cast(_597.KlingelnbergConicalGearMaterialDatabase)

        @property
        def gear_material_database(self) -> 'GearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMaterialDatabase._Cast_GearMaterialDatabase':
        return self._Cast_GearMaterialDatabase(self)
