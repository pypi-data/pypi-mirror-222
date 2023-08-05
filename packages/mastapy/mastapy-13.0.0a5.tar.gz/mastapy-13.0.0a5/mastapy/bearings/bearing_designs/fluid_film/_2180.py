"""_2180.py

PlainOilFedJournalBearing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.fluid_film import _2178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainOilFedJournalBearing')

if TYPE_CHECKING:
    from mastapy.bearings import _1874
    from mastapy.bearings.bearing_designs.fluid_film import _2169, _2170, _2171


__docformat__ = 'restructuredtext en'
__all__ = ('PlainOilFedJournalBearing',)


class PlainOilFedJournalBearing(_2178.PlainJournalBearing):
    """PlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_OIL_FED_JOURNAL_BEARING

    class _Cast_PlainOilFedJournalBearing:
        """Special nested class for casting PlainOilFedJournalBearing to subclasses."""

        def __init__(self, parent: 'PlainOilFedJournalBearing'):
            self._parent = parent

        @property
        def plain_journal_bearing(self):
            return self._parent._cast(_2178.PlainJournalBearing)

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
        def plain_oil_fed_journal_bearing(self) -> 'PlainOilFedJournalBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlainOilFedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def feed_type(self) -> '_1874.JournalOilFeedType':
        """JournalOilFeedType: 'FeedType' is the original name of this property."""

        temp = self.wrapped.FeedType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.JournalOilFeedType')
        return constructor.new_from_mastapy('mastapy.bearings._1874', 'JournalOilFeedType')(value) if value is not None else None

    @feed_type.setter
    def feed_type(self, value: '_1874.JournalOilFeedType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.JournalOilFeedType')
        self.wrapped.FeedType = value

    @property
    def land_width(self) -> 'float':
        """float: 'LandWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LandWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_axial_points_for_pressure_distribution(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfAxialPointsForPressureDistribution' is the original name of this property."""

        temp = self.wrapped.NumberOfAxialPointsForPressureDistribution

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_int')(temp) if temp is not None else 0

    @number_of_axial_points_for_pressure_distribution.setter
    def number_of_axial_points_for_pressure_distribution(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfAxialPointsForPressureDistribution = value

    @property
    def number_of_circumferential_points_for_pressure_distribution(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfCircumferentialPointsForPressureDistribution' is the original name of this property."""

        temp = self.wrapped.NumberOfCircumferentialPointsForPressureDistribution

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_int')(temp) if temp is not None else 0

    @number_of_circumferential_points_for_pressure_distribution.setter
    def number_of_circumferential_points_for_pressure_distribution(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfCircumferentialPointsForPressureDistribution = value

    @property
    def axial_groove_oil_feed(self) -> '_2169.AxialGrooveJournalBearing':
        """AxialGrooveJournalBearing: 'AxialGrooveOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialGrooveOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def axial_hole_oil_feed(self) -> '_2170.AxialHoleJournalBearing':
        """AxialHoleJournalBearing: 'AxialHoleOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialHoleOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def circumferential_groove_oil_feed(self) -> '_2171.CircumferentialFeedJournalBearing':
        """CircumferentialFeedJournalBearing: 'CircumferentialGrooveOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircumferentialGrooveOilFeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlainOilFedJournalBearing._Cast_PlainOilFedJournalBearing':
        return self._Cast_PlainOilFedJournalBearing(self)
