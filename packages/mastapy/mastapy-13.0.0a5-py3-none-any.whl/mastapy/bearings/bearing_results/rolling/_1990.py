"""_1990.py

LoadedBallBearingRow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2021
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingRow')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1989, _1988


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingRow',)


class LoadedBallBearingRow(_2021.LoadedRollingBearingRow):
    """LoadedBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_ROW

    class _Cast_LoadedBallBearingRow:
        """Special nested class for casting LoadedBallBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedBallBearingRow'):
            self._parent = parent

        @property
        def loaded_rolling_bearing_row(self):
            return self._parent._cast(_2021.LoadedRollingBearingRow)

        @property
        def loaded_angular_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1971
            
            return self._parent._cast(_1971.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1974
            
            return self._parent._cast(_1974.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2000
            
            return self._parent._cast(_2000.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2005
            
            return self._parent._cast(_2005.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2024
            
            return self._parent._cast(_2024.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2039
            
            return self._parent._cast(_2039.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2042
            
            return self._parent._cast(_2042.LoadedThrustBallBearingRow)

        @property
        def loaded_ball_bearing_row(self) -> 'LoadedBallBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_ball_movement(self) -> 'float':
        """float: 'AxialBallMovement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialBallMovement

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_inner(self) -> 'float':
        """float: 'DynamicEquivalentLoadInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_equivalent_load_outer(self) -> 'float':
        """float: 'DynamicEquivalentLoadOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_with_worst_track_truncation(self) -> 'str':
        """str: 'ElementWithWorstTrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementWithWorstTrackTruncation

        if temp is None:
            return ''

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_inner(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionHighestLoadInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_highest_load_outer(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionHighestLoadOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_inner(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionHighestLoadInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_highest_load_outer(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionHighestLoadOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionHighestLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(self) -> 'float':
        """float: 'SmallestArcDistanceOfRacewayEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact

        if temp is None:
            return 0.0

        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self) -> 'bool':
        """bool: 'TrackTruncationOccurringBeyondPermissibleLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit

        if temp is None:
            return False

        return temp

    @property
    def truncation_warning(self) -> 'str':
        """str: 'TruncationWarning' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TruncationWarning

        if temp is None:
            return ''

        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self) -> 'float':
        """float: 'WorstHertzianEllipseMajor2bTrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_bearing(self) -> '_1989.LoadedBallBearingResults':
        """LoadedBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def race_results(self) -> 'List[_1988.LoadedBallBearingRaceResults]':
        """List[LoadedBallBearingRaceResults]: 'RaceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedBallBearingRow._Cast_LoadedBallBearingRow':
        return self._Cast_LoadedBallBearingRow(self)
