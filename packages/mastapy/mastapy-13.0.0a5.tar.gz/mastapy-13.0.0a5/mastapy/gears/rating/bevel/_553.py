"""_553.py

BevelGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.agma_gleason_conical import _564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel', 'BevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetRating',)


class BevelGearSetRating(_564.AGMAGleasonConicalGearSetRating):
    """BevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_RATING

    class _Cast_BevelGearSetRating:
        """Special nested class for casting BevelGearSetRating to subclasses."""

        def __init__(self, parent: 'BevelGearSetRating'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_rating(self):
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
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _369
            
            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel import _395
            
            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _402
            
            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def bevel_gear_set_rating(self) -> 'BevelGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetRating.TYPE'):
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
    def cast_to(self) -> 'BevelGearSetRating._Cast_BevelGearSetRating':
        return self._Cast_BevelGearSetRating(self)
