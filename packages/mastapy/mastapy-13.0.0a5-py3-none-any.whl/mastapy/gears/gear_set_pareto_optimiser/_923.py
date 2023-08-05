"""_923.py

ParetoCylindricalRatingOptimisationStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility.optimisation import _1543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_RATING_OPTIMISATION_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoCylindricalRatingOptimisationStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoCylindricalRatingOptimisationStrategyDatabase',)


class ParetoCylindricalRatingOptimisationStrategyDatabase(_1543.ParetoOptimisationStrategyDatabase):
    """ParetoCylindricalRatingOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_RATING_OPTIMISATION_STRATEGY_DATABASE

    class _Cast_ParetoCylindricalRatingOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalRatingOptimisationStrategyDatabase to subclasses."""

        def __init__(self, parent: 'ParetoCylindricalRatingOptimisationStrategyDatabase'):
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
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _921
            
            return self._parent._cast(_921.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _922
            
            return self._parent._cast(_922.ParetoCylindricalGearSetOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(self) -> 'ParetoCylindricalRatingOptimisationStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParetoCylindricalRatingOptimisationStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParetoCylindricalRatingOptimisationStrategyDatabase._Cast_ParetoCylindricalRatingOptimisationStrategyDatabase':
        return self._Cast_ParetoCylindricalRatingOptimisationStrategyDatabase(self)
