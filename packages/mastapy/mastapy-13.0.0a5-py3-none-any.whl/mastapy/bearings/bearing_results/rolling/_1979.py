﻿"""_1979.py

LoadedAxialThrustCylindricalRollerBearingDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_results.rolling import _2010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAxialThrustCylindricalRollerBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAxialThrustCylindricalRollerBearingDutyCycle',)


class LoadedAxialThrustCylindricalRollerBearingDutyCycle(_2010.LoadedNonBarrelRollerBearingDutyCycle):
    """LoadedAxialThrustCylindricalRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_DUTY_CYCLE

    class _Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedAxialThrustCylindricalRollerBearingDutyCycle'):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(self):
            return self._parent._cast(_2010.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results import _1946
            
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
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(self) -> 'LoadedAxialThrustCylindricalRollerBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAxialThrustCylindricalRollerBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAxialThrustCylindricalRollerBearingDutyCycle._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle':
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingDutyCycle(self)
