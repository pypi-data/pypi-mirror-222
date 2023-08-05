﻿"""_771.py

ConicalFlankDeviationsData
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_FLANK_DEVIATIONS_DATA = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalFlankDeviationsData')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalFlankDeviationsData',)


class ConicalFlankDeviationsData(_0.APIBase):
    """ConicalFlankDeviationsData

    This is a mastapy class.
    """

    TYPE = _CONICAL_FLANK_DEVIATIONS_DATA

    class _Cast_ConicalFlankDeviationsData:
        """Special nested class for casting ConicalFlankDeviationsData to subclasses."""

        def __init__(self, parent: 'ConicalFlankDeviationsData'):
            self._parent = parent

        @property
        def conical_flank_deviations_data(self) -> 'ConicalFlankDeviationsData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalFlankDeviationsData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_crowning_deviation(self) -> 'float':
        """float: 'AverageCrowningDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageCrowningDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_pressure_angle_deviation(self) -> 'float':
        """float: 'AveragePressureAngleDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePressureAngleDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_profile_curvature_deviation(self) -> 'float':
        """float: 'AverageProfileCurvatureDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageProfileCurvatureDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def average_spiral_angle_deviation(self) -> 'float':
        """float: 'AverageSpiralAngleDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageSpiralAngleDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def bias_deviation(self) -> 'float':
        """float: 'BiasDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BiasDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ConicalFlankDeviationsData._Cast_ConicalFlankDeviationsData':
        return self._Cast_ConicalFlankDeviationsData(self)
