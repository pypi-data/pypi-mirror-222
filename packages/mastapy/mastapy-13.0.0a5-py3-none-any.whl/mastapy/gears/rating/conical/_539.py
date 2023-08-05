"""_539.py

ConicalGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearSetRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _940


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetRating',)


class ConicalGearSetRating(_361.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING

    class _Cast_ConicalGearSetRating:
        """Special nested class for casting ConicalGearSetRating to subclasses."""

        def __init__(self, parent: 'ConicalGearSetRating'):
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
        def zerol_bevel_gear_set_rating(self):
            from mastapy.gears.rating.zerol_bevel import _369
            
            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel import _395
            
            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _398
            
            return self._parent._cast(_398.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.spiral_bevel import _402
            
            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405
            
            return self._parent._cast(_405.KlingelnbergCycloPalloidSpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _408
            
            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _411
            
            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(self):
            from mastapy.gears.rating.hypoid import _438
            
            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _553
            
            return self._parent._cast(_553.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _564
            
            return self._parent._cast(_564.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(self) -> 'ConicalGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self) -> '_940.BevelHypoidGearRatingSettingsItem':
        """BevelHypoidGearRatingSettingsItem: 'RatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetRating._Cast_ConicalGearSetRating':
        return self._Cast_ConicalGearSetRating(self)
