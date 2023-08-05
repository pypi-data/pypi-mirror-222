"""_548.py

ConceptGearRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.rating import _359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearRating')

if TYPE_CHECKING:
    from mastapy.gears.rating import _357
    from mastapy.gears.gear_designs.concept import _1172


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearRating',)


class ConceptGearRating(_359.GearRating):
    """ConceptGearRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_RATING

    class _Cast_ConceptGearRating:
        """Special nested class for casting ConceptGearRating to subclasses."""

        def __init__(self, parent: 'ConceptGearRating'):
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
        def concept_gear_rating(self) -> 'ConceptGearRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearRating.TYPE'):
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
    def concept_gear(self) -> '_1172.ConceptGearDesign':
        """ConceptGearDesign: 'ConceptGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGear

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
    def cast_to(self) -> 'ConceptGearRating._Cast_ConceptGearRating':
        return self._Cast_ConceptGearRating(self)
