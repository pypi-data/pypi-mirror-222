"""_1962.py

ISO14179SettingsDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.bearings.bearing_results.rolling import _1961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO14179_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISO14179SettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO14179SettingsDatabase',)


class ISO14179SettingsDatabase(_1817.NamedDatabase['_1961.ISO14179Settings']):
    """ISO14179SettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS_DATABASE

    class _Cast_ISO14179SettingsDatabase:
        """Special nested class for casting ISO14179SettingsDatabase to subclasses."""

        def __init__(self, parent: 'ISO14179SettingsDatabase'):
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
        def iso14179_settings_database(self) -> 'ISO14179SettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO14179SettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase':
        return self._Cast_ISO14179SettingsDatabase(self)
