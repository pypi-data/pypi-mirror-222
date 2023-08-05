﻿"""_2124.py

AsymmetricSphericalRollerBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASYMMETRIC_SPHERICAL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'AsymmetricSphericalRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('AsymmetricSphericalRollerBearing',)


class AsymmetricSphericalRollerBearing(_2149.RollerBearing):
    """AsymmetricSphericalRollerBearing

    This is a mastapy class.
    """

    TYPE = _ASYMMETRIC_SPHERICAL_ROLLER_BEARING

    class _Cast_AsymmetricSphericalRollerBearing:
        """Special nested class for casting AsymmetricSphericalRollerBearing to subclasses."""

        def __init__(self, parent: 'AsymmetricSphericalRollerBearing'):
            self._parent = parent

        @property
        def roller_bearing(self):
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
        def asymmetric_spherical_roller_bearing(self) -> 'AsymmetricSphericalRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AsymmetricSphericalRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_profile_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementProfileRadius' is the original name of this property."""

        temp = self.wrapped.ElementProfileRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_profile_radius.setter
    def element_profile_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementProfileRadius = value

    @property
    def inner_race_groove_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRaceGrooveRadius' is the original name of this property."""

        temp = self.wrapped.InnerRaceGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_race_groove_radius.setter
    def inner_race_groove_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRaceGrooveRadius = value

    @property
    def inner_rib_chamfer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRibChamfer' is the original name of this property."""

        temp = self.wrapped.InnerRibChamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_rib_chamfer.setter
    def inner_rib_chamfer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRibChamfer = value

    @property
    def inner_rib_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRibDiameter' is the original name of this property."""

        temp = self.wrapped.InnerRibDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @inner_rib_diameter.setter
    def inner_rib_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRibDiameter = value

    @property
    def major_diameter_offset_from_roller_centre(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MajorDiameterOffsetFromRollerCentre' is the original name of this property."""

        temp = self.wrapped.MajorDiameterOffsetFromRollerCentre

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @major_diameter_offset_from_roller_centre.setter
    def major_diameter_offset_from_roller_centre(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MajorDiameterOffsetFromRollerCentre = value

    @property
    def outer_race_groove_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRaceGrooveRadius' is the original name of this property."""

        temp = self.wrapped.OuterRaceGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @outer_race_groove_radius.setter
    def outer_race_groove_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRaceGrooveRadius = value

    @property
    def cast_to(self) -> 'AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing':
        return self._Cast_AsymmetricSphericalRollerBearing(self)
