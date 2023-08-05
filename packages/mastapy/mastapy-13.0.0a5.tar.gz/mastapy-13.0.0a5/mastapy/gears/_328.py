"""_328.py

GearSetOptimisationResult
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISATION_RESULT = python_net_import('SMT.MastaAPI.Gears', 'GearSetOptimisationResult')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _947
    from mastapy.math_utility.optimisation import _1534
    from mastapy.gears.rating import _353


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimisationResult',)


class GearSetOptimisationResult(_0.APIBase):
    """GearSetOptimisationResult

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISATION_RESULT

    class _Cast_GearSetOptimisationResult:
        """Special nested class for casting GearSetOptimisationResult to subclasses."""

        def __init__(self, parent: 'GearSetOptimisationResult'):
            self._parent = parent

        @property
        def gear_set_optimisation_result(self) -> 'GearSetOptimisationResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetOptimisationResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set(self) -> '_947.GearSetDesign':
        """GearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def is_optimized(self) -> 'bool':
        """bool: 'IsOptimized' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsOptimized

        if temp is None:
            return False

        return temp

    @property
    def optimisation_history(self) -> '_1534.OptimisationHistory':
        """OptimisationHistory: 'OptimisationHistory' is the original name of this property."""

        temp = self.wrapped.OptimisationHistory

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @optimisation_history.setter
    def optimisation_history(self, value: '_1534.OptimisationHistory'):
        self.wrapped.OptimisationHistory = value

    @property
    def rating(self) -> '_353.AbstractGearSetRating':
        """AbstractGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetOptimisationResult._Cast_GearSetOptimisationResult':
        return self._Cast_GearSetOptimisationResult(self)
