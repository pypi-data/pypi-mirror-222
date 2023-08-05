"""_2546.py

SuperchargerRotorSetDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2545
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'SuperchargerRotorSetDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('SuperchargerRotorSetDatabase',)


class SuperchargerRotorSetDatabase(_1817.NamedDatabase['_2545.SuperchargerRotorSet']):
    """SuperchargerRotorSetDatabase

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET_DATABASE

    class _Cast_SuperchargerRotorSetDatabase:
        """Special nested class for casting SuperchargerRotorSetDatabase to subclasses."""

        def __init__(self, parent: 'SuperchargerRotorSetDatabase'):
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
        def supercharger_rotor_set_database(self) -> 'SuperchargerRotorSetDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SuperchargerRotorSetDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SuperchargerRotorSetDatabase._Cast_SuperchargerRotorSetDatabase':
        return self._Cast_SuperchargerRotorSetDatabase(self)
