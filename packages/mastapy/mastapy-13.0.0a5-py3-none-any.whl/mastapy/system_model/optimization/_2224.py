"""_2224.py

OptimizationStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.databases import _1817
from mastapy.system_model.optimization import _2216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategyDatabase',)


class OptimizationStrategyDatabase(_1817.NamedDatabase['_2216.CylindricalGearOptimisationStrategy']):
    """OptimizationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_STRATEGY_DATABASE

    class _Cast_OptimizationStrategyDatabase:
        """Special nested class for casting OptimizationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'OptimizationStrategyDatabase'):
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
        def optimization_strategy_database(self) -> 'OptimizationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationStrategyDatabase._Cast_OptimizationStrategyDatabase':
        return self._Cast_OptimizationStrategyDatabase(self)
