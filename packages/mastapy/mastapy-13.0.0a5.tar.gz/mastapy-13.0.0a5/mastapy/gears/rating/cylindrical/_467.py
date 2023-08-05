"""_467.py

CylindricalPlasticGearRatingSettingsDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.gears.rating.cylindrical import _468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalPlasticGearRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlasticGearRatingSettingsDatabase',)


class CylindricalPlasticGearRatingSettingsDatabase(_1817.NamedDatabase['_468.CylindricalPlasticGearRatingSettingsItem']):
    """CylindricalPlasticGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE

    class _Cast_CylindricalPlasticGearRatingSettingsDatabase:
        """Special nested class for casting CylindricalPlasticGearRatingSettingsDatabase to subclasses."""

        def __init__(self, parent: 'CylindricalPlasticGearRatingSettingsDatabase'):
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
        def cylindrical_plastic_gear_rating_settings_database(self) -> 'CylindricalPlasticGearRatingSettingsDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlasticGearRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalPlasticGearRatingSettingsDatabase._Cast_CylindricalPlasticGearRatingSettingsDatabase':
        return self._Cast_CylindricalPlasticGearRatingSettingsDatabase(self)
