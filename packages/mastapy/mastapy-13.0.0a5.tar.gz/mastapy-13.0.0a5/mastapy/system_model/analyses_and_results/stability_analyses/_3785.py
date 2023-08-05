﻿"""_3785.py

CriticalSpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CriticalSpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CriticalSpeed',)


class CriticalSpeed(_0.APIBase):
    """CriticalSpeed

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED

    class _Cast_CriticalSpeed:
        """Special nested class for casting CriticalSpeed to subclasses."""

        def __init__(self, parent: 'CriticalSpeed'):
            self._parent = parent

        @property
        def critical_speed(self) -> 'CriticalSpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CriticalSpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_speed_as_frequency(self) -> 'float':
        """float: 'CriticalSpeedAsFrequency' is the original name of this property."""

        temp = self.wrapped.CriticalSpeedAsFrequency

        if temp is None:
            return 0.0

        return temp

    @critical_speed_as_frequency.setter
    def critical_speed_as_frequency(self, value: 'float'):
        self.wrapped.CriticalSpeedAsFrequency = float(value) if value is not None else 0.0

    @property
    def critical_speed_as_shaft_speed(self) -> 'float':
        """float: 'CriticalSpeedAsShaftSpeed' is the original name of this property."""

        temp = self.wrapped.CriticalSpeedAsShaftSpeed

        if temp is None:
            return 0.0

        return temp

    @critical_speed_as_shaft_speed.setter
    def critical_speed_as_shaft_speed(self, value: 'float'):
        self.wrapped.CriticalSpeedAsShaftSpeed = float(value) if value is not None else 0.0

    @property
    def mode_index(self) -> 'int':
        """int: 'ModeIndex' is the original name of this property."""

        temp = self.wrapped.ModeIndex

        if temp is None:
            return 0

        return temp

    @mode_index.setter
    def mode_index(self, value: 'int'):
        self.wrapped.ModeIndex = int(value) if value is not None else 0

    @property
    def shaft_harmonic_index(self) -> 'int':
        """int: 'ShaftHarmonicIndex' is the original name of this property."""

        temp = self.wrapped.ShaftHarmonicIndex

        if temp is None:
            return 0

        return temp

    @shaft_harmonic_index.setter
    def shaft_harmonic_index(self, value: 'int'):
        self.wrapped.ShaftHarmonicIndex = int(value) if value is not None else 0

    @property
    def cast_to(self) -> 'CriticalSpeed._Cast_CriticalSpeed':
        return self._Cast_CriticalSpeed(self)
