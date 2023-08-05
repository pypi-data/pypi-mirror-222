"""_405.py

KlingelnbergCycloPalloidSpiralBevelGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelGearSetRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _972
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _404, _403


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetRating',)


class KlingelnbergCycloPalloidSpiralBevelGearSetRating(_411.KlingelnbergCycloPalloidConicalGearSetRating):
    """KlingelnbergCycloPalloidSpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSetRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(self):
            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_972.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergCycloPalloidSpiralBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_ratings(self) -> 'List[_404.KlingelnbergCycloPalloidSpiralBevelGearRating]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearRating]: 'KlingelnbergCycloPalloidSpiralBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_mesh_ratings(self) -> 'List[_403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshRating]: 'KlingelnbergCycloPalloidSpiralBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating(self)
