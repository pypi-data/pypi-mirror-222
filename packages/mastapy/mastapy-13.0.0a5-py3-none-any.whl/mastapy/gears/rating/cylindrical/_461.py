﻿"""_461.py

CylindricalGearSetDutyCycleRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSetDutyCycleRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1025
    from mastapy.gears.rating.cylindrical.optimisation import _498
    from mastapy.gears.rating.cylindrical import _464


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetDutyCycleRating',)


class CylindricalGearSetDutyCycleRating(_360.GearSetDutyCycleRating):
    """CylindricalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING

    class _Cast_CylindricalGearSetDutyCycleRating:
        """Special nested class for casting CylindricalGearSetDutyCycleRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetDutyCycleRating'):
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
        def cylindrical_gear_set_duty_cycle_rating(self) -> 'CylindricalGearSetDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set(self) -> '_1025.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimisations(self) -> '_498.CylindricalGearSetRatingOptimisationHelper':
        """CylindricalGearSetRatingOptimisationHelper: 'Optimisations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimisations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_464.CylindricalMeshDutyCycleRating]':
        """List[CylindricalMeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_duty_cycle_ratings(self) -> 'List[_464.CylindricalMeshDutyCycleRating]':
        """List[CylindricalMeshDutyCycleRating]: 'CylindricalMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_profile_shift_to_maximum_safety_factor_fatigue_and_static(self):
        """ 'SetProfileShiftToMaximumSafetyFactorFatigueAndStatic' is the original name of this method."""

        self.wrapped.SetProfileShiftToMaximumSafetyFactorFatigueAndStatic()

    @property
    def cast_to(self) -> 'CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating':
        return self._Cast_CylindricalGearSetDutyCycleRating(self)
