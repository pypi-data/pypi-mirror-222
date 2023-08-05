"""_2216.py

CylindricalGearOptimisationStrategy
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.optimization import _2222, _2217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'CylindricalGearOptimisationStrategy')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearOptimisationStrategy',)


class CylindricalGearOptimisationStrategy(_2222.OptimizationStrategy['_2217.CylindricalGearOptimizationStep']):
    """CylindricalGearOptimisationStrategy

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_OPTIMISATION_STRATEGY

    class _Cast_CylindricalGearOptimisationStrategy:
        """Special nested class for casting CylindricalGearOptimisationStrategy to subclasses."""

        def __init__(self, parent: 'CylindricalGearOptimisationStrategy'):
            self._parent = parent

        @property
        def optimization_strategy(self):
            return self._parent._cast(_2222.OptimizationStrategy)

        @property
        def optimization_strategy_base(self):
            from mastapy.system_model.optimization import _2223
            
            return self._parent._cast(_2223.OptimizationStrategyBase)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def cylindrical_gear_optimisation_strategy(self) -> 'CylindricalGearOptimisationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearOptimisationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearOptimisationStrategy._Cast_CylindricalGearOptimisationStrategy':
        return self._Cast_CylindricalGearOptimisationStrategy(self)
