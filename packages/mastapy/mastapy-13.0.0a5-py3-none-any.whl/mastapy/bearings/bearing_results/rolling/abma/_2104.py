﻿"""_2104.py

ANSIABMAResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANSIABMA_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.ABMA', 'ANSIABMAResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ANSIABMAResults',)


class ANSIABMAResults(_2092.ISOResults):
    """ANSIABMAResults

    This is a mastapy class.
    """

    TYPE = _ANSIABMA_RESULTS

    class _Cast_ANSIABMAResults:
        """Special nested class for casting ANSIABMAResults to subclasses."""

        def __init__(self, parent: 'ANSIABMAResults'):
            self._parent = parent

        @property
        def iso_results(self):
            return self._parent._cast(_2092.ISOResults)

        @property
        def ansiabma112014_results(self):
            from mastapy.bearings.bearing_results.rolling.abma import _2102
            
            return self._parent._cast(_2102.ANSIABMA112014Results)

        @property
        def ansiabma92015_results(self):
            from mastapy.bearings.bearing_results.rolling.abma import _2103
            
            return self._parent._cast(_2103.ANSIABMA92015Results)

        @property
        def ansiabma_results(self) -> 'ANSIABMAResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ANSIABMAResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def e_limiting_value_for_dynamic_equivalent_load(self) -> 'float':
        """float: 'ELimitingValueForDynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ELimitingValueForDynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_cycles(self) -> 'float':
        """float: 'AdjustedRatingLifeCycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_damage(self) -> 'float':
        """float: 'AdjustedRatingLifeDamage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_damage_rate(self) -> 'float':
        """float: 'AdjustedRatingLifeDamageRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_reliability(self) -> 'float':
        """float: 'AdjustedRatingLifeReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_safety_factor(self) -> 'float':
        """float: 'AdjustedRatingLifeSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_time(self) -> 'float':
        """float: 'AdjustedRatingLifeTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def adjusted_rating_life_unreliability(self) -> 'float':
        """float: 'AdjustedRatingLifeUnreliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjustedRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_to_radial_load_ratio(self) -> 'float':
        """float: 'AxialToRadialLoadRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialToRadialLoadRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_cycles(self) -> 'float':
        """float: 'BasicRatingLifeCycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_damage(self) -> 'float':
        """float: 'BasicRatingLifeDamage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_damage_rate(self) -> 'float':
        """float: 'BasicRatingLifeDamageRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeDamageRate

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_reliability(self) -> 'float':
        """float: 'BasicRatingLifeReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_safety_factor(self) -> 'float':
        """float: 'BasicRatingLifeSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_time(self) -> 'float':
        """float: 'BasicRatingLifeTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeTime

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_rating_life_unreliability(self) -> 'float':
        """float: 'BasicRatingLifeUnreliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicRatingLifeUnreliability

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(self) -> 'float':
        """float: 'BearingLifeAdjustmentFactorForOperatingConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions

        if temp is None:
            return 0.0

        return temp

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(self) -> 'float':
        """float: 'BearingLifeAdjustmentFactorForSpecialBearingProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_axial_load_factor(self) -> 'float':
        """float: 'DynamicAxialLoadFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAxialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load(self) -> 'float':
        """float: 'DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_radial_load_factor(self) -> 'float':
        """float: 'DynamicRadialLoadFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicRadialLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor(self) -> 'float':
        """float: 'StaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ANSIABMAResults._Cast_ANSIABMAResults':
        return self._Cast_ANSIABMAResults(self)
