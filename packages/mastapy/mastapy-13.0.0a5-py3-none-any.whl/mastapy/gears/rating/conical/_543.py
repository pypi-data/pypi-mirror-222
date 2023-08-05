﻿"""_543.py

ConicalMeshSingleFlankRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshSingleFlankRating',)


class ConicalMeshSingleFlankRating(_364.MeshSingleFlankRating):
    """ConicalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_SINGLE_FLANK_RATING

    class _Cast_ConicalMeshSingleFlankRating:
        """Special nested class for casting ConicalMeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ConicalMeshSingleFlankRating'):
            self._parent = parent

        @property
        def mesh_single_flank_rating(self):
            return self._parent._cast(_364.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _420
            
            return self._parent._cast(_420.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _421
            
            return self._parent._cast(_421.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _422
            
            return self._parent._cast(_422.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _423
            
            return self._parent._cast(_423.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _424
            
            return self._parent._cast(_424.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _441
            
            return self._parent._cast(_441.GleasonHypoidMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _555
            
            return self._parent._cast(_555.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _557
            
            return self._parent._cast(_557.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _559
            
            return self._parent._cast(_559.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(self) -> 'ConicalMeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating':
        return self._Cast_ConicalMeshSingleFlankRating(self)
