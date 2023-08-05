"""_437.py

HypoidGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.agma_gleason_conical import _563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid', 'HypoidGearRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _982


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearRating',)


class HypoidGearRating(_563.AGMAGleasonConicalGearRating):
    """HypoidGearRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_RATING

    class _Cast_HypoidGearRating:
        """Special nested class for casting HypoidGearRating to subclasses."""

        def __init__(self, parent: 'HypoidGearRating'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_rating(self):
            return self._parent._cast(_563.AGMAGleasonConicalGearRating)

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
        def hypoid_gear_rating(self) -> 'HypoidGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hypoid_gear(self) -> '_982.HypoidGearDesign':
        """HypoidGearDesign: 'HypoidGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HypoidGearRating._Cast_HypoidGearRating':
        return self._Cast_HypoidGearRating(self)
