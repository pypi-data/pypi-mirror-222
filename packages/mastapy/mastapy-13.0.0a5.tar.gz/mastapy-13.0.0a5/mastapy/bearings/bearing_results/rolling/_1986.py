﻿"""_1986.py

LoadedBallBearingDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingDutyCycle')

if TYPE_CHECKING:
    from mastapy.utility.property import _1828
    from mastapy.bearings.bearing_results.rolling import _1989


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingDutyCycle',)


class LoadedBallBearingDutyCycle(_1946.LoadedRollingBearingDutyCycle):
    """LoadedBallBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_DUTY_CYCLE

    class _Cast_LoadedBallBearingDutyCycle:
        """Special nested class for casting LoadedBallBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedBallBearingDutyCycle'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_duty_cycle(self):
            return self._parent._cast(_1946.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(self):
            from mastapy.bearings.bearing_results import _1943
            
            return self._parent._cast(_1943.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1935
            
            return self._parent._cast(_1935.LoadedBearingDutyCycle)

        @property
        def loaded_ball_bearing_duty_cycle(self) -> 'LoadedBallBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def track_truncation_safety_factor(self) -> 'float':
        """float: 'TrackTruncationSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_inner_summary(self) -> '_1828.DutyCyclePropertySummaryPercentage[_1989.LoadedBallBearingResults]':
        """DutyCyclePropertySummaryPercentage[LoadedBallBearingResults]: 'TrackTruncationInnerSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationInnerSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1989.LoadedBallBearingResults](temp) if temp is not None else None

    @property
    def track_truncation_outer_summary(self) -> '_1828.DutyCyclePropertySummaryPercentage[_1989.LoadedBallBearingResults]':
        """DutyCyclePropertySummaryPercentage[LoadedBallBearingResults]: 'TrackTruncationOuterSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationOuterSummary

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1989.LoadedBallBearingResults](temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedBallBearingDutyCycle._Cast_LoadedBallBearingDutyCycle':
        return self._Cast_LoadedBallBearingDutyCycle(self)
