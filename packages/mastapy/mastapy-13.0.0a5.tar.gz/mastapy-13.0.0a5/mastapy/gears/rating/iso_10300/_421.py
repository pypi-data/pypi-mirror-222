﻿"""_421.py

ISO10300MeshSingleFlankRatingBevelMethodB2
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.iso_10300 import _424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_BEVEL_METHOD_B2 = python_net_import('SMT.MastaAPI.Gears.Rating.Iso10300', 'ISO10300MeshSingleFlankRatingBevelMethodB2')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO10300MeshSingleFlankRatingBevelMethodB2',)


class ISO10300MeshSingleFlankRatingBevelMethodB2(_424.ISO10300MeshSingleFlankRatingMethodB2):
    """ISO10300MeshSingleFlankRatingBevelMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING_BEVEL_METHOD_B2

    class _Cast_ISO10300MeshSingleFlankRatingBevelMethodB2:
        """Special nested class for casting ISO10300MeshSingleFlankRatingBevelMethodB2 to subclasses."""

        def __init__(self, parent: 'ISO10300MeshSingleFlankRatingBevelMethodB2'):
            self._parent = parent

        @property
        def iso10300_mesh_single_flank_rating_method_b2(self):
            return self._parent._cast(_424.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def iso10300_mesh_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _420
            from mastapy.gears.rating.virtual_cylindrical_gears import _389
            
            return self._parent._cast(_420.ISO10300MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.conical import _543
            
            return self._parent._cast(_543.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self):
            from mastapy.gears.rating import _364
            
            return self._parent._cast(_364.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(self) -> 'ISO10300MeshSingleFlankRatingBevelMethodB2':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO10300MeshSingleFlankRatingBevelMethodB2.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_sharing_ratio_for_bending_method_b2_for_none_statically_loaded_bevel_gear(self) -> 'float':
        """float: 'LoadSharingRatioForBendingMethodB2ForNoneStaticallyLoadedBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingRatioForBendingMethodB2ForNoneStaticallyLoadedBevelGear

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_ratio_for_bending_method_b2_statically_loaded_straight_and_zerol_bevel_gears(self) -> 'float':
        """float: 'LoadSharingRatioForBendingMethodB2StaticallyLoadedStraightAndZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingRatioForBendingMethodB2StaticallyLoadedStraightAndZerolBevelGears

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action(self) -> 'float':
        """float: 'LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_non_statically_loaded_with_modified_contact_ratio_larger_than_2(self) -> 'float':
        """float: 'LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLargerThan2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLargerThan2

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_non_statically_loaded_with_modified_contact_ratio_less_or_equal_than_2(self) -> 'float':
        """float: 'LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLessOrEqualThan2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLessOrEqualThan2

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_statically_loaded_straight_bevel_and_zerol_bevel_gear(self) -> 'float':
        """float: 'LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForStaticallyLoadedStraightBevelAndZerolBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForStaticallyLoadedStraightBevelAndZerolBevelGear

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_to_point_of_load_application_method_b2(self) -> 'float':
        """float: 'RelativeLengthOfActionToPointOfLoadApplicationMethodB2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeLengthOfActionToPointOfLoadApplicationMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def gj(self) -> 'float':
        """float: 'GJ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GJ

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2':
        return self._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2(self)
