"""_2141.py

FourPointContactBallBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FOUR_POINT_CONTACT_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'FourPointContactBallBearing')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2140


__docformat__ = 'restructuredtext en'
__all__ = ('FourPointContactBallBearing',)


class FourPointContactBallBearing(_2146.MultiPointContactBallBearing):
    """FourPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _FOUR_POINT_CONTACT_BALL_BEARING

    class _Cast_FourPointContactBallBearing:
        """Special nested class for casting FourPointContactBallBearing to subclasses."""

        def __init__(self, parent: 'FourPointContactBallBearing'):
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
        def four_point_contact_ball_bearing(self) -> 'FourPointContactBallBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FourPointContactBallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_axial_internal_clearance(self) -> 'float':
        """float: 'AssemblyAxialInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_under_axial_load(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ContactAngleUnderAxialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleUnderAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def contact_angle_under_radial_load(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ContactAngleUnderRadialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleUnderRadialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def contact_angle_and_internal_clearance_definition(self) -> '_2140.FourPointContactAngleDefinition':
        """FourPointContactAngleDefinition: 'ContactAngleAndInternalClearanceDefinition' is the original name of this property."""

        temp = self.wrapped.ContactAngleAndInternalClearanceDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_designs.rolling._2140', 'FourPointContactAngleDefinition')(value) if value is not None else None

    @contact_angle_and_internal_clearance_definition.setter
    def contact_angle_and_internal_clearance_definition(self, value: '_2140.FourPointContactAngleDefinition'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingDesigns.Rolling.FourPointContactAngleDefinition')
        self.wrapped.ContactAngleAndInternalClearanceDefinition = value

    @property
    def nominal_radial_internal_clearance(self) -> 'float':
        """float: 'NominalRadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.NominalRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @nominal_radial_internal_clearance.setter
    def nominal_radial_internal_clearance(self, value: 'float'):
        self.wrapped.NominalRadialInternalClearance = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'FourPointContactBallBearing._Cast_FourPointContactBallBearing':
        return self._Cast_FourPointContactBallBearing(self)
