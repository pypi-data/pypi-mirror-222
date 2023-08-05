"""_2078.py

MinimumLoad
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2083
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MINIMUM_LOAD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'MinimumLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('MinimumLoad',)


class MinimumLoad(_2083.SKFCalculationResult):
    """MinimumLoad

    This is a mastapy class.
    """

    TYPE = _MINIMUM_LOAD

    class _Cast_MinimumLoad:
        """Special nested class for casting MinimumLoad to subclasses."""

        def __init__(self, parent: 'MinimumLoad'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2083.SKFCalculationResult)

        @property
        def minimum_load(self) -> 'MinimumLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MinimumLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_axial_load(self) -> 'Optional[float]':
        """Optional[float]: 'MinimumAxialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumAxialLoad

        if temp is None:
            return None

        return temp

    @property
    def minimum_equivalent_load(self) -> 'Optional[float]':
        """Optional[float]: 'MinimumEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEquivalentLoad

        if temp is None:
            return None

        return temp

    @property
    def minimum_radial_load(self) -> 'Optional[float]':
        """Optional[float]: 'MinimumRadialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRadialLoad

        if temp is None:
            return None

        return temp

    @property
    def requirement_met(self) -> 'bool':
        """bool: 'RequirementMet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequirementMet

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'MinimumLoad._Cast_MinimumLoad':
        return self._Cast_MinimumLoad(self)
