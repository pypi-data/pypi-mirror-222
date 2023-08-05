﻿"""_538.py

ConicalGearSetDutyCycleRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearSetDutyCycleRating')

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _541


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetDutyCycleRating',)


class ConicalGearSetDutyCycleRating(_360.GearSetDutyCycleRating):
    """ConicalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_DUTY_CYCLE_RATING

    class _Cast_ConicalGearSetDutyCycleRating:
        """Special nested class for casting ConicalGearSetDutyCycleRating to subclasses."""

        def __init__(self, parent: 'ConicalGearSetDutyCycleRating'):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(self):
            return self._parent._cast(_360.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(self):
            from mastapy.gears.rating import _353
            
            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def conical_gear_set_duty_cycle_rating(self) -> 'ConicalGearSetDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_541.ConicalMeshDutyCycleRating]':
        """List[ConicalMeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def conical_mesh_duty_cycle_ratings(self) -> 'List[_541.ConicalMeshDutyCycleRating]':
        """List[ConicalMeshDutyCycleRating]: 'ConicalMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSetDutyCycleRating._Cast_ConicalGearSetDutyCycleRating':
        return self._Cast_ConicalGearSetDutyCycleRating(self)
