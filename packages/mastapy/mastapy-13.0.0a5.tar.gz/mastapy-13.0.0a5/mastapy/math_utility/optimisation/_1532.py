"""_1532.py

MicroGeometryDesignSpaceSearchStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility.optimisation import _1530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'MicroGeometryDesignSpaceSearchStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearchStrategyDatabase',)


class MicroGeometryDesignSpaceSearchStrategyDatabase(_1530.DesignSpaceSearchStrategyDatabase):
    """MicroGeometryDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE

    class _Cast_MicroGeometryDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(self, parent: 'MicroGeometryDesignSpaceSearchStrategyDatabase'):
            self._parent = parent

        @property
        def design_space_search_strategy_database(self):
            return self._parent._cast(_1530.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1817
            from mastapy.math_utility.optimisation import _1540
            
            return self._parent._cast(_1817.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1820, _1819
            from mastapy.math_utility.optimisation import _1540
            
            return self._parent._cast(_1820.SQLDatabase)

        @property
        def database(self):
            from mastapy.utility.databases import _1813, _1819
            from mastapy.math_utility.optimisation import _1540
            
            return self._parent._cast(_1813.Database)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _917
            
            return self._parent._cast(_917.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _918
            
            return self._parent._cast(_918.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(self) -> 'MicroGeometryDesignSpaceSearchStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearchStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase':
        return self._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase(self)
