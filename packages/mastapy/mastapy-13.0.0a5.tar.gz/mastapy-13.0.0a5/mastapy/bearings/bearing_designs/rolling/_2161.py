"""_2161.py

ToroidalRollerBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2129
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOROIDAL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'ToroidalRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('ToroidalRollerBearing',)


class ToroidalRollerBearing(_2129.BarrelRollerBearing):
    """ToroidalRollerBearing

    This is a mastapy class.
    """

    TYPE = _TOROIDAL_ROLLER_BEARING

    class _Cast_ToroidalRollerBearing:
        """Special nested class for casting ToroidalRollerBearing to subclasses."""

        def __init__(self, parent: 'ToroidalRollerBearing'):
            self._parent = parent

        @property
        def barrel_roller_bearing(self):
            return self._parent._cast(_2129.BarrelRollerBearing)

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
        def toroidal_roller_bearing(self) -> 'ToroidalRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ToroidalRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_capability(self) -> 'float':
        """float: 'AxialDisplacementCapability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialDisplacementCapability

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_capability_towards_snap_ring(self) -> 'float':
        """float: 'AxialDisplacementCapabilityTowardsSnapRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialDisplacementCapabilityTowardsSnapRing

        if temp is None:
            return 0.0

        return temp

    @property
    def snap_ring_offset_from_element(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SnapRingOffsetFromElement' is the original name of this property."""

        temp = self.wrapped.SnapRingOffsetFromElement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @snap_ring_offset_from_element.setter
    def snap_ring_offset_from_element(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SnapRingOffsetFromElement = value

    @property
    def snap_ring_width(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SnapRingWidth' is the original name of this property."""

        temp = self.wrapped.SnapRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @snap_ring_width.setter
    def snap_ring_width(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SnapRingWidth = value

    @property
    def cast_to(self) -> 'ToroidalRollerBearing._Cast_ToroidalRollerBearing':
        return self._Cast_ToroidalRollerBearing(self)
