"""_926.py

ParetoFaceRatingOptimisationStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility.optimisation import _1543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoFaceRatingOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoFaceRatingOptimisationStrategyDatabase',)


class ParetoFaceRatingOptimisationStrategyDatabase(_1543.ParetoOptimisationStrategyDatabase):
    """ParetoFaceRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_FACE_RATING_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoFaceRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoFaceRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoFaceRatingOptimisationStrategyDatabase'):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_database(self):
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
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _924
            
            return self._parent._cast(_924.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _925
            
            return self._parent._cast(_925.ParetoFaceGearSetOptimisationStrategyDatabase)

        @property
        def pareto_face_rating_optimisation_strategy_database(self) -> 'ParetoFaceRatingOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoFaceRatingOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoFaceRatingOptimisationStrategyDatabase._Cast_ParetoFaceRatingOptimisationStrategyDatabase':
        return self._Cast_ParetoFaceRatingOptimisationStrategyDatabase(self)
