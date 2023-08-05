﻿"""_300.py

PowerLoss
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOSS = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'PowerLoss')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoss',)


class PowerLoss(_0.APIBase):
    """PowerLoss

    This is a mastapy class.
    """

    TYPE = _POWER_LOSS

    class _Cast_PowerLoss:
        """Special nested class for casting PowerLoss to subclasses."""

        def __init__(self, parent: 'PowerLoss'):
            self._parent = parent

        @property
        def independent_power_loss(self):
            from mastapy.materials.efficiency import _293
            
            return self._parent._cast(_293.IndependentPowerLoss)

        @property
        def load_and_speed_combined_power_loss(self):
            from mastapy.materials.efficiency import _295
            
            return self._parent._cast(_295.LoadAndSpeedCombinedPowerLoss)

        @property
        def power_loss(self) -> 'PowerLoss':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerLoss.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss_calculation_details(self) -> 'str':
        """str: 'PowerLossCalculationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossCalculationDetails

        if temp is None:
            return ''

        return temp

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'PowerLoss._Cast_PowerLoss':
        return self._Cast_PowerLoss(self)
