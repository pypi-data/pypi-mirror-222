"""_39.py

ShaftSettingsDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.shafts import _40
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Shafts', 'ShaftSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSettingsDatabase',)


class ShaftSettingsDatabase(_1817.NamedDatabase['_40.ShaftSettingsItem']):
    """ShaftSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS_DATABASE

    class _Cast_ShaftSettingsDatabase:
        """Special nested class for casting ShaftSettingsDatabase to subclasses."""

        def __init__(self, parent: 'ShaftSettingsDatabase'):
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
        def shaft_settings_database(self) -> 'ShaftSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftSettingsDatabase._Cast_ShaftSettingsDatabase':
        return self._Cast_ShaftSettingsDatabase(self)
