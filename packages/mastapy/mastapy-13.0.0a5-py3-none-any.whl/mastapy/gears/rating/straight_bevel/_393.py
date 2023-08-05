"""_393.py

StraightBevelGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearMeshRating')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _959
    from mastapy.gears.rating.straight_bevel import _394


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshRating',)


class StraightBevelGearMeshRating(_551.BevelGearMeshRating):
    """StraightBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_RATING

    class _Cast_StraightBevelGearMeshRating:
        """Special nested class for casting StraightBevelGearMeshRating to subclasses."""

        def __init__(self, parent: 'StraightBevelGearMeshRating'):
            self._parent = parent

        @property
        def bevel_gear_mesh_rating(self):
            return self._parent._cast(_551.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _562
            
            return self._parent._cast(_562.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _536
            
            return self._parent._cast(_536.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _358
            
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
        def straight_bevel_gear_mesh_rating(self) -> 'StraightBevelGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_mesh(self) -> '_959.StraightBevelGearMeshDesign':
        """StraightBevelGearMeshDesign: 'StraightBevelGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_394.StraightBevelGearRating]':
        """List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearMeshRating._Cast_StraightBevelGearMeshRating':
        return self._Cast_StraightBevelGearMeshRating(self)
