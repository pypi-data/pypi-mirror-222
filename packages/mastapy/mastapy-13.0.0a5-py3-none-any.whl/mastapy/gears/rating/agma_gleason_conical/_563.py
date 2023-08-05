"""_563.py

AGMAGleasonConicalGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating.conical import _537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.AGMAGleasonConical', 'AGMAGleasonConicalGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearRating',)


class AGMAGleasonConicalGearRating(_537.ConicalGearRating):
    """AGMAGleasonConicalGearRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_RATING

    class _Cast_AGMAGleasonConicalGearRating:
        """Special nested class for casting AGMAGleasonConicalGearRating to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearRating'):
            self._parent = parent

        @property
        def conical_gear_rating(self):
            return self._parent._cast(_537.ConicalGearRating)

        @property
        def gear_rating(self):
            from mastapy.gears.rating import _359
            
            return self._parent._cast(_359.GearRating)

        @property
        def abstract_gear_rating(self):
            from mastapy.gears.rating import _352
            
            return self._parent._cast(_352.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(self):
            from mastapy.gears.rating.zerol_bevel import _368
            
            return self._parent._cast(_368.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(self):
            from mastapy.gears.rating.straight_bevel import _394
            
            return self._parent._cast(_394.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.spiral_bevel import _401
            
            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def hypoid_gear_rating(self):
            from mastapy.gears.rating.hypoid import _437
            
            return self._parent._cast(_437.HypoidGearRating)

        @property
        def bevel_gear_rating(self):
            from mastapy.gears.rating.bevel import _552
            
            return self._parent._cast(_552.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self) -> 'AGMAGleasonConicalGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating':
        return self._Cast_AGMAGleasonConicalGearRating(self)
