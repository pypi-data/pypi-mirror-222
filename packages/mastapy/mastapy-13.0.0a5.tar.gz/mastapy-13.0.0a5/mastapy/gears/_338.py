﻿"""_338.py

PlanetaryDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_DETAIL = python_net_import('SMT.MastaAPI.Gears', 'PlanetaryDetail')

if TYPE_CHECKING:
    from mastapy.gears import _337


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryDetail',)


class PlanetaryDetail(_0.APIBase):
    """PlanetaryDetail

    This is a mastapy class.
    """

    TYPE = _PLANETARY_DETAIL

    class _Cast_PlanetaryDetail:
        """Special nested class for casting PlanetaryDetail to subclasses."""

        def __init__(self, parent: 'PlanetaryDetail'):
            self._parent = parent

        @property
        def planetary_detail(self) -> 'PlanetaryDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_planet_angle(self) -> 'float':
        """float: 'FirstPlanetAngle' is the original name of this property."""

        temp = self.wrapped.FirstPlanetAngle

        if temp is None:
            return 0.0

        return temp

    @first_planet_angle.setter
    def first_planet_angle(self, value: 'float'):
        self.wrapped.FirstPlanetAngle = float(value) if value is not None else 0.0

    @property
    def number_of_planets(self) -> 'int':
        """int: 'NumberOfPlanets' is the original name of this property."""

        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @number_of_planets.setter
    def number_of_planets(self, value: 'int'):
        self.wrapped.NumberOfPlanets = int(value) if value is not None else 0

    @property
    def planet_diameter(self) -> 'float':
        """float: 'PlanetDiameter' is the original name of this property."""

        temp = self.wrapped.PlanetDiameter

        if temp is None:
            return 0.0

        return temp

    @planet_diameter.setter
    def planet_diameter(self, value: 'float'):
        self.wrapped.PlanetDiameter = float(value) if value is not None else 0.0

    @property
    def regularly_spaced_planets(self) -> 'bool':
        """bool: 'RegularlySpacedPlanets' is the original name of this property."""

        temp = self.wrapped.RegularlySpacedPlanets

        if temp is None:
            return False

        return temp

    @regularly_spaced_planets.setter
    def regularly_spaced_planets(self, value: 'bool'):
        self.wrapped.RegularlySpacedPlanets = bool(value) if value is not None else False

    @property
    def planet_delta_angles(self) -> 'List[_337.NamedPlanetAngle]':
        """List[NamedPlanetAngle]: 'PlanetDeltaAngles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetDeltaAngles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryDetail._Cast_PlanetaryDetail':
        return self._Cast_PlanetaryDetail(self)
