"""_1018.py

CylindricalGearMicroGeometrySettingsDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.gears.gear_designs.cylindrical import _1019
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMicroGeometrySettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometrySettingsDatabase',)


class CylindricalGearMicroGeometrySettingsDatabase(_1817.NamedDatabase['_1019.CylindricalGearMicroGeometrySettingsItem']):
    """CylindricalGearMicroGeometrySettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE

    class _Cast_CylindricalGearMicroGeometrySettingsDatabase:
        """Special nested class for casting CylindricalGearMicroGeometrySettingsDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometrySettingsDatabase'):
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
        def cylindrical_gear_micro_geometry_settings_database(self) -> 'CylindricalGearMicroGeometrySettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometrySettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometrySettingsDatabase._Cast_CylindricalGearMicroGeometrySettingsDatabase':
        return self._Cast_CylindricalGearMicroGeometrySettingsDatabase(self)
