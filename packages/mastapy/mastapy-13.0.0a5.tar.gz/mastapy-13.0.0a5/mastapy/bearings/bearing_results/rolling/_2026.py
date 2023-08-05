"""_2026.py

LoadedSphericalRollerBearingElement
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_results.rolling import _2015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSphericalRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSphericalRollerBearingElement',)


class LoadedSphericalRollerBearingElement(_2015.LoadedRollerBearingElement):
    """LoadedSphericalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedSphericalRollerBearingElement:
        """Special nested class for casting LoadedSphericalRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedSphericalRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(self):
            return self._parent._cast(_2015.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _2001
            
            return self._parent._cast(_2001.LoadedElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2025
            
            return self._parent._cast(_2025.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2032
            
            return self._parent._cast(_2032.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(self) -> 'LoadedSphericalRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSphericalRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement':
        return self._Cast_LoadedSphericalRollerBearingElement(self)
