﻿"""_441.py

GleasonHypoidMeshSingleFlankRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.conical import _543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GLEASON_HYPOID_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid.Standards', 'GleasonHypoidMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GleasonHypoidMeshSingleFlankRating',)


class GleasonHypoidMeshSingleFlankRating(_543.ConicalMeshSingleFlankRating):
    """GleasonHypoidMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_HYPOID_MESH_SINGLE_FLANK_RATING

    class _Cast_GleasonHypoidMeshSingleFlankRating:
        """Special nested class for casting GleasonHypoidMeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'GleasonHypoidMeshSingleFlankRating'):
            self._parent = parent

        @property
        def conical_mesh_single_flank_rating(self):
            return self._parent._cast(_543.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self):
            from mastapy.gears.rating import _364
            
            return self._parent._cast(_364.MeshSingleFlankRating)

        @property
        def gleason_hypoid_mesh_single_flank_rating(self) -> 'GleasonHypoidMeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GleasonHypoidMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_contact_stress(self) -> 'float':
        """float: 'CalculatedContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def dynamic_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def elastic_coefficient(self) -> 'float':
        """float: 'ElasticCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_i(self) -> 'float':
        """float: 'GeometryFactorI' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorI

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_bending(self) -> 'float':
        """float: 'LoadDistributionFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_contact(self) -> 'float':
        """float: 'LoadDistributionFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverloadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def overload_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverloadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

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
    def surface_condition_factor(self) -> 'float':
        """float: 'SurfaceConditionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TemperatureFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def temperature_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TemperatureFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def transmitted_tangential_load_at_large_end(self) -> 'float':
        """float: 'TransmittedTangentialLoadAtLargeEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmittedTangentialLoadAtLargeEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'GleasonHypoidMeshSingleFlankRating._Cast_GleasonHypoidMeshSingleFlankRating':
        return self._Cast_GleasonHypoidMeshSingleFlankRating(self)
