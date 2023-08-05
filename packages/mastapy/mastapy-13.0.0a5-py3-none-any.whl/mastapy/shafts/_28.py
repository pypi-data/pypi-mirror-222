﻿"""_28.py

ShaftPointStressCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POINT_STRESS_CYCLE = python_net_import('SMT.MastaAPI.Shafts', 'ShaftPointStressCycle')

if TYPE_CHECKING:
    from mastapy.shafts import _44, _27


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftPointStressCycle',)


class ShaftPointStressCycle(_0.APIBase):
    """ShaftPointStressCycle

    This is a mastapy class.
    """

    TYPE = _SHAFT_POINT_STRESS_CYCLE

    class _Cast_ShaftPointStressCycle:
        """Special nested class for casting ShaftPointStressCycle to subclasses."""

        def __init__(self, parent: 'ShaftPointStressCycle'):
            self._parent = parent

        @property
        def shaft_point_stress_cycle(self) -> 'ShaftPointStressCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftPointStressCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def din743201212_comparative_mean_stress(self) -> '_44.StressMeasurementShaftAxialBendingTorsionalComponentValues':
        """StressMeasurementShaftAxialBendingTorsionalComponentValues: 'DIN743201212ComparativeMeanStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DIN743201212ComparativeMeanStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stress_amplitude(self) -> '_27.ShaftPointStress':
        """ShaftPointStress: 'StressAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressAmplitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stress_mean(self) -> '_27.ShaftPointStress':
        """ShaftPointStress: 'StressMean' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressMean

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stress_total(self) -> '_27.ShaftPointStress':
        """ShaftPointStress: 'StressTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftPointStressCycle._Cast_ShaftPointStressCycle':
        return self._Cast_ShaftPointStressCycle(self)
