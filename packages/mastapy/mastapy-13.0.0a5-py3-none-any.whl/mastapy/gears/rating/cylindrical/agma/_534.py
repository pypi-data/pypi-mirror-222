﻿"""_534.py

ThermalReductionFactorFactorsAndExponents
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA', 'ThermalReductionFactorFactorsAndExponents')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalReductionFactorFactorsAndExponents',)


class ThermalReductionFactorFactorsAndExponents(_0.APIBase):
    """ThermalReductionFactorFactorsAndExponents

    This is a mastapy class.
    """

    TYPE = _THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS

    class _Cast_ThermalReductionFactorFactorsAndExponents:
        """Special nested class for casting ThermalReductionFactorFactorsAndExponents to subclasses."""

        def __init__(self, parent: 'ThermalReductionFactorFactorsAndExponents'):
            self._parent = parent

        @property
        def thermal_reduction_factor_factors_and_exponents(self) -> 'ThermalReductionFactorFactorsAndExponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThermalReductionFactorFactorsAndExponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_exponent(self) -> 'float':
        """float: 'FirstExponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstExponent

        if temp is None:
            return 0.0

        return temp

    @property
    def first_factor(self) -> 'float':
        """float: 'FirstFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def second_exponent(self) -> 'float':
        """float: 'SecondExponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondExponent

        if temp is None:
            return 0.0

        return temp

    @property
    def second_factor(self) -> 'float':
        """float: 'SecondFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ThermalReductionFactorFactorsAndExponents._Cast_ThermalReductionFactorFactorsAndExponents':
        return self._Cast_ThermalReductionFactorFactorsAndExponents(self)
