"""_933.py

ParetoStraightBevelGearSetOptimisationStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_set_pareto_optimiser import _920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_STRAIGHT_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoStraightBevelGearSetOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoStraightBevelGearSetOptimisationStrategyDatabase',)


class ParetoStraightBevelGearSetOptimisationStrategyDatabase(_920.ParetoConicalRatingOptimisationStrategyDatabase):
    """ParetoStraightBevelGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_STRAIGHT_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoStraightBevelGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase'):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(self):
            return self._parent._cast(_920.ParetoConicalRatingOptimisationStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(self):
            from mastapy.math_utility.optimisation import _1543
            
            return self._parent._cast(_1543.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1530
            
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
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> 'ParetoStraightBevelGearSetOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoStraightBevelGearSetOptimisationStrategyDatabase._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        return self._Cast_ParetoStraightBevelGearSetOptimisationStrategyDatabase(self)
