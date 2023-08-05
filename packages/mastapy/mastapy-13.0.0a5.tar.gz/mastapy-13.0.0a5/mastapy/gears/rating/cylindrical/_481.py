﻿"""_481.py

ScuffingResultsRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING_RESULTS_ROW = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'ScuffingResultsRow')

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _482


__docformat__ = 'restructuredtext en'
__all__ = ('ScuffingResultsRow',)


class ScuffingResultsRow(_0.APIBase):
    """ScuffingResultsRow

    This is a mastapy class.
    """

    TYPE = _SCUFFING_RESULTS_ROW

    class _Cast_ScuffingResultsRow:
        """Special nested class for casting ScuffingResultsRow to subclasses."""

        def __init__(self, parent: 'ScuffingResultsRow'):
            self._parent = parent

        @property
        def agma_scuffing_results_row(self):
            from mastapy.gears.rating.cylindrical import _449
            
            return self._parent._cast(_449.AGMAScuffingResultsRow)

        @property
        def iso_scuffing_results_row(self):
            from mastapy.gears.rating.cylindrical import _472
            
            return self._parent._cast(_472.ISOScuffingResultsRow)

        @property
        def scuffing_results_row(self) -> 'ScuffingResultsRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ScuffingResultsRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_temperature(self) -> 'float':
        """float: 'ContactTemperature' is the original name of this property."""

        temp = self.wrapped.ContactTemperature

        if temp is None:
            return 0.0

        return temp

    @contact_temperature.setter
    def contact_temperature(self, value: 'float'):
        self.wrapped.ContactTemperature = float(value) if value is not None else 0.0

    @property
    def flash_temperature(self) -> 'float':
        """float: 'FlashTemperature' is the original name of this property."""

        temp = self.wrapped.FlashTemperature

        if temp is None:
            return 0.0

        return temp

    @flash_temperature.setter
    def flash_temperature(self, value: 'float'):
        self.wrapped.FlashTemperature = float(value) if value is not None else 0.0

    @property
    def index_label(self) -> 'str':
        """str: 'IndexLabel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IndexLabel

        if temp is None:
            return ''

        return temp

    @property
    def line_of_action_parameter(self) -> 'float':
        """float: 'LineOfActionParameter' is the original name of this property."""

        temp = self.wrapped.LineOfActionParameter

        if temp is None:
            return 0.0

        return temp

    @line_of_action_parameter.setter
    def line_of_action_parameter(self, value: 'float'):
        self.wrapped.LineOfActionParameter = float(value) if value is not None else 0.0

    @property
    def load_sharing_factor(self) -> 'float':
        """float: 'LoadSharingFactor' is the original name of this property."""

        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @load_sharing_factor.setter
    def load_sharing_factor(self, value: 'float'):
        self.wrapped.LoadSharingFactor = float(value) if value is not None else 0.0

    @property
    def normal_relative_radius_of_curvature(self) -> 'float':
        """float: 'NormalRelativeRadiusOfCurvature' is the original name of this property."""

        temp = self.wrapped.NormalRelativeRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @normal_relative_radius_of_curvature.setter
    def normal_relative_radius_of_curvature(self, value: 'float'):
        self.wrapped.NormalRelativeRadiusOfCurvature = float(value) if value is not None else 0.0

    @property
    def pinion_flank_transverse_radius_of_curvature(self) -> 'float':
        """float: 'PinionFlankTransverseRadiusOfCurvature' is the original name of this property."""

        temp = self.wrapped.PinionFlankTransverseRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @pinion_flank_transverse_radius_of_curvature.setter
    def pinion_flank_transverse_radius_of_curvature(self, value: 'float'):
        self.wrapped.PinionFlankTransverseRadiusOfCurvature = float(value) if value is not None else 0.0

    @property
    def pinion_rolling_velocity(self) -> 'float':
        """float: 'PinionRollingVelocity' is the original name of this property."""

        temp = self.wrapped.PinionRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @pinion_rolling_velocity.setter
    def pinion_rolling_velocity(self, value: 'float'):
        self.wrapped.PinionRollingVelocity = float(value) if value is not None else 0.0

    @property
    def sliding_velocity(self) -> 'float':
        """float: 'SlidingVelocity' is the original name of this property."""

        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @sliding_velocity.setter
    def sliding_velocity(self, value: 'float'):
        self.wrapped.SlidingVelocity = float(value) if value is not None else 0.0

    @property
    def wheel_flank_transverse_radius_of_curvature(self) -> 'float':
        """float: 'WheelFlankTransverseRadiusOfCurvature' is the original name of this property."""

        temp = self.wrapped.WheelFlankTransverseRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @wheel_flank_transverse_radius_of_curvature.setter
    def wheel_flank_transverse_radius_of_curvature(self, value: 'float'):
        self.wrapped.WheelFlankTransverseRadiusOfCurvature = float(value) if value is not None else 0.0

    @property
    def wheel_rolling_velocity(self) -> 'float':
        """float: 'WheelRollingVelocity' is the original name of this property."""

        temp = self.wrapped.WheelRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @wheel_rolling_velocity.setter
    def wheel_rolling_velocity(self, value: 'float'):
        self.wrapped.WheelRollingVelocity = float(value) if value is not None else 0.0

    @property
    def pinion(self) -> '_482.ScuffingResultsRowGear':
        """ScuffingResultsRowGear: 'Pinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Pinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ScuffingResultsRow._Cast_ScuffingResultsRow':
        return self._Cast_ScuffingResultsRow(self)
