﻿"""_597.py

KlingelnbergConicalGearMaterialDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.materials import _592, _598
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'KlingelnbergConicalGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalGearMaterialDatabase',)


class KlingelnbergConicalGearMaterialDatabase(_592.GearMaterialDatabase['_598.KlingelnbergCycloPalloidConicalGearMaterial']):
    """KlingelnbergConicalGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE

    class _Cast_KlingelnbergConicalGearMaterialDatabase:
        """Special nested class for casting KlingelnbergConicalGearMaterialDatabase to subclasses."""

        def __init__(self, parent: 'KlingelnbergConicalGearMaterialDatabase'):
            self._parent = parent

        @property
        def gear_material_database(self):
            return self._parent._cast(_592.GearMaterialDatabase)

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
        def klingelnberg_conical_gear_material_database(self) -> 'KlingelnbergConicalGearMaterialDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase':
        return self._Cast_KlingelnbergConicalGearMaterialDatabase(self)
