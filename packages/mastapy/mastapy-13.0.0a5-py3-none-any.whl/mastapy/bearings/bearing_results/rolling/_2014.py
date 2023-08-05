﻿"""_2014.py

LoadedNonBarrelRollerElement
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerElement',)


class LoadedNonBarrelRollerElement(_2015.LoadedRollerBearingElement):
    """LoadedNonBarrelRollerElement

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_ELEMENT

    class _Cast_LoadedNonBarrelRollerElement:
        """Special nested class for casting LoadedNonBarrelRollerElement to subclasses."""

        def __init__(self, parent: 'LoadedNonBarrelRollerElement'):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(self):
            return self._parent._cast(_2015.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _2001
            
            return self._parent._cast(_2001.LoadedElement)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1980
            
            return self._parent._cast(_1980.LoadedAxialThrustCylindricalRollerBearingElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1983
            
            return self._parent._cast(_1983.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1995
            
            return self._parent._cast(_1995.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2007
            
            return self._parent._cast(_2007.LoadedNeedleRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2034
            
            return self._parent._cast(_2034.LoadedTaperRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(self) -> 'LoadedNonBarrelRollerElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_smt_rib_stress_safety_factor(self) -> 'float':
        """float: 'MinimumSMTRibStressSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSMTRibStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement':
        return self._Cast_LoadedNonBarrelRollerElement(self)
