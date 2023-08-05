"""_918.py

MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.math_utility.optimisation import _1532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_GEAR_SET_DUTY_CYCLE_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase',)


class MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase(_1532.MicroGeometryDesignSpaceSearchStrategyDatabase):
    """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DUTY_CYCLE_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE

    class _Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(self, parent: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase'):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_strategy_database(self):
            return self._parent._cast(_1532.MicroGeometryDesignSpaceSearchStrategyDatabase)

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
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        return self._Cast_MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase(self)
