"""_623.py

CylindricalShaperDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical import _607
from mastapy.gears.manufacturing.cylindrical.cutters import _711
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SHAPER_DATABASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalShaperDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalShaperDatabase',)


class CylindricalShaperDatabase(_607.CylindricalCutterDatabase['_711.CylindricalGearShaper']):
    """CylindricalShaperDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SHAPER_DATABASE

    class _Cast_CylindricalShaperDatabase:
        """Special nested class for casting CylindricalShaperDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalShaperDatabase'):
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
        def cylindrical_shaper_database(self) -> 'CylindricalShaperDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalShaperDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalShaperDatabase._Cast_CylindricalShaperDatabase':
        return self._Cast_CylindricalShaperDatabase(self)
