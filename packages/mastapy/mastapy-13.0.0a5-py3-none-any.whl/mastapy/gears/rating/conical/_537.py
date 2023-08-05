"""_537.py

ConicalGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating import _359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearRating')

if TYPE_CHECKING:
    from mastapy.gears.rating import _357


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearRating',)


class ConicalGearRating(_359.GearRating):
    """ConicalGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_RATING

    class _Cast_ConicalGearRating:
        """Special nested class for casting ConicalGearRating to subclasses."""

        def __init__(self, parent: 'ConicalGearRating'):
            self._parent = parent

        @property
        def gear_rating(self):
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
        def straight_bevel_diff_gear_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _397
            
            return self._parent._cast(_397.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.spiral_bevel import _401
            
            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidSpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _407
            
            return self._parent._cast(_407.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _410
            
            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self):
            from mastapy.gears.rating.hypoid import _437
            
            return self._parent._cast(_437.HypoidGearRating)

        @property
        def bevel_gear_rating(self):
            from mastapy.gears.rating.bevel import _552
            
            return self._parent._cast(_552.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _563
            
            return self._parent._cast(_563.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(self) -> 'ConicalGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self) -> '_357.GearFlankRating':
        """GearFlankRating: 'ConcaveFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def convex_flank_rating(self) -> '_357.GearFlankRating':
        """GearFlankRating: 'ConvexFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearRating._Cast_ConicalGearRating':
        return self._Cast_ConicalGearRating(self)
