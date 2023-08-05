"""_2126.py

AxialThrustNeedleRollerBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_designs.rolling import _2125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_THRUST_NEEDLE_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AxialThrustNeedleRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialThrustNeedleRollerBearing',)


class AxialThrustNeedleRollerBearing(_2125.AxialThrustCylindricalRollerBearing):
    """AxialThrustNeedleRollerBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_THRUST_NEEDLE_ROLLER_BEARING

    class _Cast_AxialThrustNeedleRollerBearing:
        """Special nested class for casting AxialThrustNeedleRollerBearing to subclasses."""

        def __init__(self, parent: 'AxialThrustNeedleRollerBearing'):
            self._parent = parent

        @property
        def axial_thrust_cylindrical_roller_bearing(self):
            return self._parent._cast(_2125.AxialThrustCylindricalRollerBearing)

        @property
        def non_barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2148
            
            return self._parent._cast(_2148.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2149
            
            return self._parent._cast(_2149.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2152
            
            return self._parent._cast(_2152.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2118
            
            return self._parent._cast(_2118.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2121
            
            return self._parent._cast(_2121.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2117
            
            return self._parent._cast(_2117.BearingDesign)

        @property
        def axial_thrust_needle_roller_bearing(self) -> 'AxialThrustNeedleRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AxialThrustNeedleRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing':
        return self._Cast_AxialThrustNeedleRollerBearing(self)
