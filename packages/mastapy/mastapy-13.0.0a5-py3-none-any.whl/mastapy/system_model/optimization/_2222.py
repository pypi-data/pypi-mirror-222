"""_2222.py

OptimizationStrategy
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.system_model.optimization import _2223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_STRATEGY = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'OptimizationStrategy')

if TYPE_CHECKING:
    from mastapy.system_model.optimization import _2221


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationStrategy',)


TStep = TypeVar('TStep', bound='_2221.OptimizationStep')


class OptimizationStrategy(_2223.OptimizationStrategyBase, Generic[TStep]):
    """OptimizationStrategy

    This is a mastapy class.

    Generic Types:
        TStep
    """

    TYPE = _OPTIMIZATION_STRATEGY

    class _Cast_OptimizationStrategy:
        """Special nested class for casting OptimizationStrategy to subclasses."""

        def __init__(self, parent: 'OptimizationStrategy'):
            self._parent = parent

        @property
        def optimization_strategy_base(self):
            return self._parent._cast(_2223.OptimizationStrategyBase)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def conical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2213
            
            return self._parent._cast(_2213.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2216
            
            return self._parent._cast(_2216.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(self) -> 'OptimizationStrategy':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OptimizationStrategy.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OptimizationStrategy._Cast_OptimizationStrategy':
        return self._Cast_OptimizationStrategy(self)
