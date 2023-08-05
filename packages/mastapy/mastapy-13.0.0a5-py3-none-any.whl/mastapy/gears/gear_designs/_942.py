﻿"""_942.py

DesignConstraintCollectionDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.gears.gear_designs import _943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_CONSTRAINT_COLLECTION_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'DesignConstraintCollectionDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignConstraintCollectionDatabase',)


class DesignConstraintCollectionDatabase(_1817.NamedDatabase['_943.DesignConstraintsCollection']):
    """DesignConstraintCollectionDatabase

    This is a mastapy class.
    """

    TYPE = _DESIGN_CONSTRAINT_COLLECTION_DATABASE

    class _Cast_DesignConstraintCollectionDatabase:
        """Special nested class for casting DesignConstraintCollectionDatabase to subclasses."""

        def __init__(self, parent: 'DesignConstraintCollectionDatabase'):
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
        def design_constraint_collection_database(self) -> 'DesignConstraintCollectionDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignConstraintCollectionDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'DesignConstraintCollectionDatabase._Cast_DesignConstraintCollectionDatabase':
        return self._Cast_DesignConstraintCollectionDatabase(self)
