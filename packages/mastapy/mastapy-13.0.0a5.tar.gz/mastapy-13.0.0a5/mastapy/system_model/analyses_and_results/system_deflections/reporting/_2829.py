﻿"""_2829.py

PlanetPinWindup
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_PIN_WINDUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting', 'PlanetPinWindup')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetPinWindup',)


class PlanetPinWindup(_0.APIBase):
    """PlanetPinWindup

    This is a mastapy class.
    """

    TYPE = _PLANET_PIN_WINDUP

    class _Cast_PlanetPinWindup:
        """Special nested class for casting PlanetPinWindup to subclasses."""

        def __init__(self, parent: 'PlanetPinWindup'):
            self._parent = parent

        @property
        def planet_pin_windup(self) -> 'PlanetPinWindup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetPinWindup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_tilt(self) -> 'float':
        """float: 'RadialTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_deflection(self) -> 'float':
        """float: 'RelativeAxialDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAxialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_deflection(self) -> 'float':
        """float: 'RelativeRadialDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeRadialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_tangential_deflection(self) -> 'float':
        """float: 'RelativeTangentialDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeTangentialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_tilt(self) -> 'float':
        """float: 'TangentialTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialTilt

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_wind_up(self) -> 'float':
        """float: 'TorsionalWindUp' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalWindUp

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'PlanetPinWindup._Cast_PlanetPinWindup':
        return self._Cast_PlanetPinWindup(self)
