"""_714.py

CylindricalWormGrinderDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical import _607
from mastapy.gears.manufacturing.cylindrical.cutters import _705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_WORM_GRINDER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalWormGrinderDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalWormGrinderDatabase',)


class CylindricalWormGrinderDatabase(_607.CylindricalCutterDatabase['_705.CylindricalGearGrindingWorm']):
    """CylindricalWormGrinderDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_WORM_GRINDER_DATABASE

    class _Cast_CylindricalWormGrinderDatabase:
        """Special nested class for casting CylindricalWormGrinderDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalWormGrinderDatabase'):
            self._parent = parent

        @property
        def cylindrical_cutter_database(self):
            return self._parent._cast(_607.CylindricalCutterDatabase)

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
        def cylindrical_worm_grinder_database(self) -> 'CylindricalWormGrinderDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalWormGrinderDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalWormGrinderDatabase._Cast_CylindricalWormGrinderDatabase':
        return self._Cast_CylindricalWormGrinderDatabase(self)
