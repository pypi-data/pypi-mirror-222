"""_407.py

KlingelnbergCycloPalloidHypoidGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical import _410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _974


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearRating',)


class KlingelnbergCycloPalloidHypoidGearRating(_410.KlingelnbergCycloPalloidConicalGearRating):
    """KlingelnbergCycloPalloidHypoidGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING

    class _Cast_KlingelnbergCycloPalloidHypoidGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearRating'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(self):
            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def conical_gear_rating(self):
            from mastapy.gears.rating.conical import _537
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(self) -> 'KlingelnbergCycloPalloidHypoidGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_974.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'KlingelnbergCycloPalloidHypoidGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearRating(self)
