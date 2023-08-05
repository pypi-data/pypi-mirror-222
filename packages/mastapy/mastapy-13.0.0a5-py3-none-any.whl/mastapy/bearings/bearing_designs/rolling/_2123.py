"""_2123.py

AngularContactThrustBallBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2122
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_THRUST_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AngularContactThrustBallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AngularContactThrustBallBearing',)


class AngularContactThrustBallBearing(_2122.AngularContactBallBearing):
    """AngularContactThrustBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_THRUST_BALL_BEARING

    class _Cast_AngularContactThrustBallBearing:
        """Special nested class for casting AngularContactThrustBallBearing to subclasses."""

        def __init__(self, parent: 'AngularContactThrustBallBearing'):
            self._parent = parent

        @property
        def angular_contact_ball_bearing(self):
            return self._parent._cast(_2122.AngularContactBallBearing)

        @property
        def ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2127
            
            return self._parent._cast(_2127.BallBearing)

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
        def angular_contact_thrust_ball_bearing(self) -> 'AngularContactThrustBallBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngularContactThrustBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'AngularContactThrustBallBearing._Cast_AngularContactThrustBallBearing':
        return self._Cast_AngularContactThrustBallBearing(self)
