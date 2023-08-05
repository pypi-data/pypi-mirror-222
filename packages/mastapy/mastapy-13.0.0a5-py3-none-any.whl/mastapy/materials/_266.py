"""_266.py

LubricationDetailDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LUBRICATION_DETAIL_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'LubricationDetailDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('LubricationDetailDatabase',)


class LubricationDetailDatabase(_1817.NamedDatabase['_265.LubricationDetail']):
    """LubricationDetailDatabase

    This is a mastapy class.
    """

    TYPE = _LUBRICATION_DETAIL_DATABASE

    class _Cast_LubricationDetailDatabase:
        """Special nested class for casting LubricationDetailDatabase to subclasses."""

        def __init__(self, parent: 'LubricationDetailDatabase'):
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
        def lubrication_detail_database(self) -> 'LubricationDetailDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LubricationDetailDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LubricationDetailDatabase._Cast_LubricationDetailDatabase':
        return self._Cast_LubricationDetailDatabase(self)
