﻿"""_438.py

HypoidGearSetRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.agma_gleason_conical import _564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid', 'HypoidGearSetRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _984
    from mastapy.gears.rating.hypoid import _437, _436


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetRating',)


class HypoidGearSetRating(_564.AGMAGleasonConicalGearSetRating):
    """HypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_RATING

    class _Cast_HypoidGearSetRating:
        """Special nested class for casting HypoidGearSetRating to subclasses."""

        def __init__(self, parent: 'HypoidGearSetRating'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_rating(self):
            return self._parent._cast(_564.AGMAGleasonConicalGearSetRating)

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
        def hypoid_gear_set_rating(self) -> 'HypoidGearSetRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def size_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def size_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def hypoid_gear_set(self) -> '_984.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'HypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_ratings(self) -> 'List[_437.HypoidGearRating]':
        """List[HypoidGearRating]: 'HypoidGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_mesh_ratings(self) -> 'List[_436.HypoidGearMeshRating]':
        """List[HypoidGearMeshRating]: 'HypoidMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetRating._Cast_HypoidGearSetRating':
        return self._Cast_HypoidGearSetRating(self)
