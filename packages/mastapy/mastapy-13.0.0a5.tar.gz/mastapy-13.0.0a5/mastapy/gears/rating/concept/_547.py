﻿"""_547.py

ConceptGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearMeshRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1173
    from mastapy.gears.rating.concept import _548


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshRating',)


class ConceptGearMeshRating(_358.GearMeshRating):
    """ConceptGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_RATING

    class _Cast_ConceptGearMeshRating:
        """Special nested class for casting ConceptGearMeshRating to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshRating'):
            self._parent = parent

        @property
        def gear_mesh_rating(self):
            return self._parent._cast(_358.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def concept_gear_mesh_rating(self) -> 'ConceptGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concept_gear_mesh(self) -> '_1173.ConceptGearMeshDesign':
        """ConceptGearMeshDesign: 'ConceptGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_ratings(self) -> 'List[_548.ConceptGearRating]':
        """List[ConceptGearRating]: 'ConceptGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshRating._Cast_ConceptGearMeshRating':
        return self._Cast_ConceptGearMeshRating(self)
