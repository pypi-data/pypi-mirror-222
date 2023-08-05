﻿"""_2159.py

ThreePointContactBallBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THREE_POINT_CONTACT_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'ThreePointContactBallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('ThreePointContactBallBearing',)


class ThreePointContactBallBearing(_2146.MultiPointContactBallBearing):
    """ThreePointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _THREE_POINT_CONTACT_BALL_BEARING

    class _Cast_ThreePointContactBallBearing:
        """Special nested class for casting ThreePointContactBallBearing to subclasses."""

        def __init__(self, parent: 'ThreePointContactBallBearing'):
            self._parent = parent

        @property
        def multi_point_contact_ball_bearing(self):
            return self._parent._cast(_2146.MultiPointContactBallBearing)

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
        def three_point_contact_ball_bearing(self) -> 'ThreePointContactBallBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ThreePointContactBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_radial_internal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AssemblyRadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.AssemblyRadialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @assembly_radial_internal_clearance.setter
    def assembly_radial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AssemblyRadialInternalClearance = value

    @property
    def inner_shim_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerShimAngle' is the original name of this property."""

        temp = self.wrapped.InnerShimAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_shim_angle.setter
    def inner_shim_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerShimAngle = value

    @property
    def inner_shim_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerShimWidth' is the original name of this property."""

        temp = self.wrapped.InnerShimWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_shim_width.setter
    def inner_shim_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerShimWidth = value

    @property
    def cast_to(self) -> 'ThreePointContactBallBearing._Cast_ThreePointContactBallBearing':
        return self._Cast_ThreePointContactBallBearing(self)
