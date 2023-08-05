﻿"""_356.py

GearDutyCycleRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _352
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearDutyCycleRating')

if TYPE_CHECKING:
    from mastapy.gears.rating import _360, _357, _359


__docformat__ = 'restructuredtext en'
__all__ = ('GearDutyCycleRating',)


class GearDutyCycleRating(_352.AbstractGearRating):
    """GearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_DUTY_CYCLE_RATING

    class _Cast_GearDutyCycleRating:
        """Special nested class for casting GearDutyCycleRating to subclasses."""

        def __init__(self, parent: 'GearDutyCycleRating'):
            self._parent = parent

        @property
        def abstract_gear_rating(self):
            return self._parent._cast(_352.AbstractGearRating)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def worm_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _370
            
            return self._parent._cast(_370.WormGearDutyCycleRating)

        @property
        def face_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _443
            
            return self._parent._cast(_443.FaceGearDutyCycleRating)

        @property
        def cylindrical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _453
            
            return self._parent._cast(_453.CylindricalGearDutyCycleRating)

        @property
        def conical_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _535
            
            return self._parent._cast(_535.ConicalGearDutyCycleRating)

        @property
        def concept_gear_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _545
            
            return self._parent._cast(_545.ConceptGearDutyCycleRating)

        @property
        def gear_duty_cycle_rating(self) -> 'GearDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_bending_stress(self) -> 'float':
        """float: 'MaximumBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design_duty_cycle(self) -> '_360.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_rating(self) -> '_357.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_357.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating

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
    def cast_to(self) -> 'GearDutyCycleRating._Cast_GearDutyCycleRating':
        return self._Cast_GearDutyCycleRating(self)
