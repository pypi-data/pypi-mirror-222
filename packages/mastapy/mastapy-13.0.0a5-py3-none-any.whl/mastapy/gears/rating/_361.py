"""_361.py

GearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetRating')

if TYPE_CHECKING:
    from mastapy.materials import _265
    from mastapy.gears.rating import _359


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetRating',)


class GearSetRating(_353.AbstractGearSetRating):
    """GearSetRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_RATING

    class _Cast_GearSetRating:
        """Special nested class for casting GearSetRating to subclasses."""

        def __init__(self, parent: 'GearSetRating'):
            self._parent = parent

        @property
        def abstract_gear_set_rating(self):
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
        def worm_gear_set_rating(self):
            from mastapy.gears.rating.worm import _374
            
            return self._parent._cast(_374.WormGearSetRating)

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
        def face_gear_set_rating(self):
            from mastapy.gears.rating.face import _448
            
            return self._parent._cast(_448.FaceGearSetRating)

        @property
        def cylindrical_gear_set_rating(self):
            from mastapy.gears.rating.cylindrical import _462
            
            return self._parent._cast(_462.CylindricalGearSetRating)

        @property
        def conical_gear_set_rating(self):
            from mastapy.gears.rating.conical import _539
            
            return self._parent._cast(_539.ConicalGearSetRating)

        @property
        def concept_gear_set_rating(self):
            from mastapy.gears.rating.concept import _550
            
            return self._parent._cast(_550.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(self):
            from mastapy.gears.rating.bevel import _553
            
            return self._parent._cast(_553.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _564
            
            return self._parent._cast(_564.AGMAGleasonConicalGearSetRating)

        @property
        def gear_set_rating(self) -> 'GearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value is not None else ''

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
    def total_gear_set_reliability(self) -> 'float':
        """float: 'TotalGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_detail(self) -> '_265.LubricationDetail':
        """LubricationDetail: 'LubricationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_359.GearRating]':
        """List[GearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetRating._Cast_GearSetRating':
        return self._Cast_GearSetRating(self)
