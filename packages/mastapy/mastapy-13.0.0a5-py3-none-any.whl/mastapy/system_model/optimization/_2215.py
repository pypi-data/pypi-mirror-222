"""_2215.py

ConicalGearOptimizationStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.system_model.optimization import _2213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_OPTIMIZATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'ConicalGearOptimizationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearOptimizationStrategyDatabase',)


class ConicalGearOptimizationStrategyDatabase(_1817.NamedDatabase['_2213.ConicalGearOptimisationStrategy']):
    """ConicalGearOptimizationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_OPTIMIZATION_STRATEGY_DATABASE

    class _Cast_ConicalGearOptimizationStrategyDatabase:
        """Special nested class for casting ConicalGearOptimizationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ConicalGearOptimizationStrategyDatabase'):
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
        def conical_gear_optimization_strategy_database(self) -> 'ConicalGearOptimizationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearOptimizationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearOptimizationStrategyDatabase._Cast_ConicalGearOptimizationStrategyDatabase':
        return self._Cast_ConicalGearOptimizationStrategyDatabase(self)
