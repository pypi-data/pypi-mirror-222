"""_2148.py

NonBarrelRollerBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.bearing_designs.rolling import _2149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_BARREL_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'NonBarrelRollerBearing')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2150, _2151


__docformat__ = 'restructuredtext en'
__all__ = ('NonBarrelRollerBearing',)


class NonBarrelRollerBearing(_2149.RollerBearing):
    """NonBarrelRollerBearing

    This is a mastapy class.
    """

    TYPE = _NON_BARREL_ROLLER_BEARING

    class _Cast_NonBarrelRollerBearing:
        """Special nested class for casting NonBarrelRollerBearing to subclasses."""

        def __init__(self, parent: 'NonBarrelRollerBearing'):
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
        def axial_thrust_cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2125
            
            return self._parent._cast(_2125.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2126
            
            return self._parent._cast(_2126.AxialThrustNeedleRollerBearing)

        @property
        def cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2136
            
            return self._parent._cast(_2136.CylindricalRollerBearing)

        @property
        def needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.NeedleRollerBearing)

        @property
        def taper_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2158
            
            return self._parent._cast(_2158.TaperRollerBearing)

        @property
        def non_barrel_roller_bearing(self) -> 'NonBarrelRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NonBarrelRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def roller_end_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RollerEndRadius' is the original name of this property."""

        temp = self.wrapped.RollerEndRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @roller_end_radius.setter
    def roller_end_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RollerEndRadius = value

    @property
    def roller_end_shape(self) -> '_2150.RollerEndShape':
        """RollerEndShape: 'RollerEndShape' is the original name of this property."""

        temp = self.wrapped.RollerEndShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.RollerEndShape')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_designs.rolling._2150', 'RollerEndShape')(value) if value is not None else None

    @roller_end_shape.setter
    def roller_end_shape(self, value: '_2150.RollerEndShape'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.RollerEndShape')
        self.wrapped.RollerEndShape = value

    @property
    def ribs(self) -> 'List[_2151.RollerRibDetail]':
        """List[RollerRibDetail]: 'Ribs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Ribs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'NonBarrelRollerBearing._Cast_NonBarrelRollerBearing':
        return self._Cast_NonBarrelRollerBearing(self)
