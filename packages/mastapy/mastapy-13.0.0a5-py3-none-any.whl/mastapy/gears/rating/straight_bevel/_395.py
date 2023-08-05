"""_395.py

StraightBevelGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _553
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearSetRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _960
    from mastapy.gears.rating.straight_bevel import _394, _393


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetRating',)


class StraightBevelGearSetRating(_553.BevelGearSetRating):
    """StraightBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_RATING

    class _Cast_StraightBevelGearSetRating:
        """Special nested class for casting StraightBevelGearSetRating to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetRating'):
            self._parent = parent

        @property
        def bevel_gear_set_rating(self):
            return self._parent._cast(_553.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _564
            
            return self._parent._cast(_564.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _539
            
            return self._parent._cast(_539.ConicalGearSetRating)

        @property
        def gear_set_rating(self):
            from mastapy.gears.rating import _361
            
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
        def straight_bevel_gear_set_rating(self) -> 'StraightBevelGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self) -> '_960.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'StraightBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_394.StraightBevelGearRating]':
        """List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_mesh_ratings(self) -> 'List[_393.StraightBevelGearMeshRating]':
        """List[StraightBevelGearMeshRating]: 'StraightBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetRating._Cast_StraightBevelGearSetRating':
        return self._Cast_StraightBevelGearSetRating(self)
