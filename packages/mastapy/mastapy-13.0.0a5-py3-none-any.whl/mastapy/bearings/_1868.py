﻿"""_1868.py

BearingSettingsItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettingsItem')

if TYPE_CHECKING:
    from mastapy.bearings import _1877, _1870, _1871


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettingsItem',)


class BearingSettingsItem(_1818.NamedDatabaseItem):
    """BearingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_ITEM

    class _Cast_BearingSettingsItem:
        """Special nested class for casting BearingSettingsItem to subclasses."""

        def __init__(self, parent: 'BearingSettingsItem'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def bearing_settings_item(self) -> 'BearingSettingsItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_bearing_weibull_reliability_slope(self) -> 'float':
        """float: 'BallBearingWeibullReliabilitySlope' is the original name of this property."""

        temp = self.wrapped.BallBearingWeibullReliabilitySlope

        if temp is None:
            return 0.0

        return temp

    @ball_bearing_weibull_reliability_slope.setter
    def ball_bearing_weibull_reliability_slope(self, value: 'float'):
        self.wrapped.BallBearingWeibullReliabilitySlope = float(value) if value is not None else 0.0

    @property
    def failure_probability_for_rating_life_percent(self) -> '_1877.RatingLife':
        """RatingLife: 'FailureProbabilityForRatingLifePercent' is the original name of this property."""

        temp = self.wrapped.FailureProbabilityForRatingLifePercent

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.RatingLife')
        return constructor.new_from_mastapy('mastapy.bearings._1877', 'RatingLife')(value) if value is not None else None

    @failure_probability_for_rating_life_percent.setter
    def failure_probability_for_rating_life_percent(self, value: '_1877.RatingLife'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.RatingLife')
        self.wrapped.FailureProbabilityForRatingLifePercent = value

    @property
    def include_exponent_and_reduction_factors_in_isots162812008(self) -> '_1870.ExponentAndReductionFactorsInISO16281Calculation':
        """ExponentAndReductionFactorsInISO16281Calculation: 'IncludeExponentAndReductionFactorsInISOTS162812008' is the original name of this property."""

        temp = self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.ExponentAndReductionFactorsInISO16281Calculation')
        return constructor.new_from_mastapy('mastapy.bearings._1870', 'ExponentAndReductionFactorsInISO16281Calculation')(value) if value is not None else None

    @include_exponent_and_reduction_factors_in_isots162812008.setter
    def include_exponent_and_reduction_factors_in_isots162812008(self, value: '_1870.ExponentAndReductionFactorsInISO16281Calculation'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.ExponentAndReductionFactorsInISO16281Calculation')
        self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008 = value

    @property
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions':
        """enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions: 'LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings' is the original name of this property."""

        temp = self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings.setter
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings = value

    @property
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions':
        """enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions: 'LubricantFilmTemperatureCalculationSplashedSubmergedBearings' is the original name of this property."""

        temp = self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_film_temperature_calculation_splashed_submerged_bearings.setter
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings = value

    @property
    def number_of_strips_for_roller_calculation(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfStripsForRollerCalculation' is the original name of this property."""

        temp = self.wrapped.NumberOfStripsForRollerCalculation

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_int')(temp) if temp is not None else 0

    @number_of_strips_for_roller_calculation.setter
    def number_of_strips_for_roller_calculation(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def roller_bearing_weibull_reliability_slope(self) -> 'float':
        """float: 'RollerBearingWeibullReliabilitySlope' is the original name of this property."""

        temp = self.wrapped.RollerBearingWeibullReliabilitySlope

        if temp is None:
            return 0.0

        return temp

    @roller_bearing_weibull_reliability_slope.setter
    def roller_bearing_weibull_reliability_slope(self, value: 'float'):
        self.wrapped.RollerBearingWeibullReliabilitySlope = float(value) if value is not None else 0.0

    @property
    def third_weibull_parameter(self) -> 'float':
        """float: 'ThirdWeibullParameter' is the original name of this property."""

        temp = self.wrapped.ThirdWeibullParameter

        if temp is None:
            return 0.0

        return temp

    @third_weibull_parameter.setter
    def third_weibull_parameter(self, value: 'float'):
        self.wrapped.ThirdWeibullParameter = float(value) if value is not None else 0.0

    @property
    def tolerance_used_for_diameter_warnings_and_database_filter(self) -> 'float':
        """float: 'ToleranceUsedForDiameterWarningsAndDatabaseFilter' is the original name of this property."""

        temp = self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter

        if temp is None:
            return 0.0

        return temp

    @tolerance_used_for_diameter_warnings_and_database_filter.setter
    def tolerance_used_for_diameter_warnings_and_database_filter(self, value: 'float'):
        self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter = float(value) if value is not None else 0.0

    @property
    def use_plain_journal_bearing_misalignment_factors(self) -> 'bool':
        """bool: 'UsePlainJournalBearingMisalignmentFactors' is the original name of this property."""

        temp = self.wrapped.UsePlainJournalBearingMisalignmentFactors

        if temp is None:
            return False

        return temp

    @use_plain_journal_bearing_misalignment_factors.setter
    def use_plain_journal_bearing_misalignment_factors(self, value: 'bool'):
        self.wrapped.UsePlainJournalBearingMisalignmentFactors = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'BearingSettingsItem._Cast_BearingSettingsItem':
        return self._Cast_BearingSettingsItem(self)
