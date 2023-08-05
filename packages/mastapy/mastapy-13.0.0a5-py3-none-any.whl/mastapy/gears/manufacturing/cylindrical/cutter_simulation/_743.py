﻿"""_743.py

ShavingSimulationCalculator
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_SIMULATION_CALCULATOR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'ShavingSimulationCalculator')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingSimulationCalculator',)


class ShavingSimulationCalculator(_728.CutterSimulationCalc):
    """ShavingSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _SHAVING_SIMULATION_CALCULATOR

    class _Cast_ShavingSimulationCalculator:
        """Special nested class for casting ShavingSimulationCalculator to subclasses."""

        def __init__(self, parent: 'ShavingSimulationCalculator'):
            self._parent = parent

        @property
        def cutter_simulation_calc(self):
            return self._parent._cast(_728.CutterSimulationCalc)

        @property
        def shaving_simulation_calculator(self) -> 'ShavingSimulationCalculator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingSimulationCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cross_angle(self) -> 'float':
        """float: 'CrossAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrossAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_normal_shaving_pitch_pressure_angle(self) -> 'float':
        """float: 'GearNormalShavingPitchPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearNormalShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_transverse_shaving_pitch_pressure_angle(self) -> 'float':
        """float: 'GearTransverseShavingPitchPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearTransverseShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def least_centre_distance_cross_angle(self) -> 'float':
        """float: 'LeastCentreDistanceCrossAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeastCentreDistanceCrossAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_centre_distance(self) -> 'float':
        """float: 'MinimumCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def shaver_transverse_shaving_pitch_pressure_angle(self) -> 'float':
        """float: 'ShaverTransverseShavingPitchPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaverTransverseShavingPitchPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaving_centre_distance(self) -> 'float':
        """float: 'ShavingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShavingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_shaving_contact_ratio(self) -> 'float':
        """float: 'TheoreticalShavingContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TheoreticalShavingContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ShavingSimulationCalculator._Cast_ShavingSimulationCalculator':
        return self._Cast_ShavingSimulationCalculator(self)
