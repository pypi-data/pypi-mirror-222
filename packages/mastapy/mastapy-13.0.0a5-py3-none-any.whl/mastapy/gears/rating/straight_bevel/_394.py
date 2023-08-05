"""_394.py

StraightBevelGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _958


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearRating',)


class StraightBevelGearRating(_552.BevelGearRating):
    """StraightBevelGearRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_RATING

    class _Cast_StraightBevelGearRating:
        """Special nested class for casting StraightBevelGearRating to subclasses."""

        def __init__(self, parent: 'StraightBevelGearRating'):
            self._parent = parent

        @property
        def bevel_gear_rating(self):
            return self._parent._cast(_552.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _563
            
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
        def straight_bevel_gear_rating(self) -> 'StraightBevelGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear(self) -> '_958.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'StraightBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelGearRating._Cast_StraightBevelGearRating':
        return self._Cast_StraightBevelGearRating(self)
