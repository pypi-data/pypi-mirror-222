﻿"""_399.py

StraightBevelDiffMeshedGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_MESHED_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevelDiff', 'StraightBevelDiffMeshedGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffMeshedGearRating',)


class StraightBevelDiffMeshedGearRating(_542.ConicalMeshedGearRating):
    """StraightBevelDiffMeshedGearRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_MESHED_GEAR_RATING

    class _Cast_StraightBevelDiffMeshedGearRating:
        """Special nested class for casting StraightBevelDiffMeshedGearRating to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffMeshedGearRating'):
            self._parent = parent

        @property
        def conical_meshed_gear_rating(self):
            return self._parent._cast(_542.ConicalMeshedGearRating)

        @property
        def straight_bevel_diff_meshed_gear_rating(self) -> 'StraightBevelDiffMeshedGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffMeshedGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress_for_peak_torque(self) -> 'float':
        """float: 'AllowableBendingStressForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStressForPeakTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_bending_stress_for_performance_torque(self) -> 'float':
        """float: 'AllowableBendingStressForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStressForPerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_bending_stress_for_peak_torque(self) -> 'float':
        """float: 'CalculatedBendingStressForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStressForPeakTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_bending_stress_for_performance_torque(self) -> 'float':
        """float: 'CalculatedBendingStressForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStressForPerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_torque(self) -> 'float':
        """float: 'PeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def performance_torque(self) -> 'float':
        """float: 'PerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_result(self) -> 'str':
        """str: 'RatingResult' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingResult

        if temp is None:
            return ''

        return temp

    @property
    def safety_factor_for_peak_torque(self) -> 'float':
        """float: 'SafetyFactorForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForPeakTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_performance_torque(self) -> 'float':
        """float: 'SafetyFactorForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForPerformanceTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor(self) -> 'float':
        """float: 'StrengthFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def total_torque_transmitted(self) -> 'float':
        """float: 'TotalTorqueTransmitted' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTorqueTransmitted

        if temp is None:
            return 0.0

        return temp

    @property
    def total_transmitted_peak_torque(self) -> 'float':
        """float: 'TotalTransmittedPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTransmittedPeakTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'StraightBevelDiffMeshedGearRating._Cast_StraightBevelDiffMeshedGearRating':
        return self._Cast_StraightBevelDiffMeshedGearRating(self)
