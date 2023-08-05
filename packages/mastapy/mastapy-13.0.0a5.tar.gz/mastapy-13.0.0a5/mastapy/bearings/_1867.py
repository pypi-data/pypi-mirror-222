"""_1867.py

BearingSettingsDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.bearings import _1868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettingsDatabase',)


class BearingSettingsDatabase(_1817.NamedDatabase['_1868.BearingSettingsItem']):
    """BearingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_DATABASE

    class _Cast_BearingSettingsDatabase:
        """Special nested class for casting BearingSettingsDatabase to subclasses."""

        def __init__(self, parent: 'BearingSettingsDatabase'):
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
        def bearing_settings_database(self) -> 'BearingSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BearingSettingsDatabase._Cast_BearingSettingsDatabase':
        return self._Cast_BearingSettingsDatabase(self)
