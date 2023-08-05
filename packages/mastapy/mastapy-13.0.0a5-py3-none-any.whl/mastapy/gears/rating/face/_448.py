"""_448.py

FaceGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearSetRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _992
    from mastapy.gears.rating.face import _446, _445


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetRating',)


class FaceGearSetRating(_361.GearSetRating):
    """FaceGearSetRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_RATING

    class _Cast_FaceGearSetRating:
        """Special nested class for casting FaceGearSetRating to subclasses."""

        def __init__(self, parent: 'FaceGearSetRating'):
            self._parent = parent

        @property
        def gear_set_rating(self):
            return self._parent._cast(_361.GearSetRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _353
            
            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def face_gear_set_rating(self) -> 'FaceGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return ''

        return temp

    @property
    def face_gear_set(self) -> '_992.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_446.FaceGearRating]':
        """List[FaceGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_ratings(self) -> 'List[_446.FaceGearRating]':
        """List[FaceGearRating]: 'FaceGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_mesh_ratings(self) -> 'List[_445.FaceGearMeshRating]':
        """List[FaceGearMeshRating]: 'FaceMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetRating._Cast_FaceGearSetRating':
        return self._Cast_FaceGearSetRating(self)
