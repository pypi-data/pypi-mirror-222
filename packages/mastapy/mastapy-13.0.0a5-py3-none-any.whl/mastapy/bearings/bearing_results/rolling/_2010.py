"""_2010.py

LoadedNonBarrelRollerBearingDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingDutyCycle',)


class LoadedNonBarrelRollerBearingDutyCycle(_1946.LoadedRollingBearingDutyCycle):
    """LoadedNonBarrelRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_DUTY_CYCLE

    class _Cast_LoadedNonBarrelRollerBearingDutyCycle:
        """Special nested class for casting LoadedNonBarrelRollerBearingDutyCycle to subclasses."""

        def __init__(self, parent: 'LoadedNonBarrelRollerBearingDutyCycle'):
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
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(self) -> 'LoadedNonBarrelRollerBearingDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def smt_rib_stress_safety_factor(self) -> 'float':
        """float: 'SMTRibStressSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SMTRibStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle':
        return self._Cast_LoadedNonBarrelRollerBearingDutyCycle(self)
