"""_551.py

BevelGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.agma_gleason_conical import _562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel', 'BevelGearMeshRating')

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel.standards import _555, _557
    from mastapy.gears.rating.iso_10300 import _423, _421
    from mastapy.gears.rating.conical import _542


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshRating',)


class BevelGearMeshRating(_562.AGMAGleasonConicalGearMeshRating):
    """BevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_RATING

    class _Cast_BevelGearMeshRating:
        """Special nested class for casting BevelGearMeshRating to subclasses."""

        def __init__(self, parent: 'BevelGearMeshRating'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
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
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _367
            
            return self._parent._cast(_367.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _393
            
            return self._parent._cast(_393.StraightBevelGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _400
            
            return self._parent._cast(_400.SpiralBevelGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self) -> 'BevelGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def agma_bevel_mesh_single_flank_rating(self) -> '_555.AGMASpiralBevelMeshSingleFlankRating':
        """AGMASpiralBevelMeshSingleFlankRating: 'AGMABevelMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMABevelMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gleason_bevel_mesh_single_flank_rating(self) -> '_557.GleasonSpiralBevelMeshSingleFlankRating':
        """GleasonSpiralBevelMeshSingleFlankRating: 'GleasonBevelMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonBevelMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso10300_bevel_mesh_single_flank_rating_method_b1(self) -> '_423.ISO10300MeshSingleFlankRatingMethodB1':
        """ISO10300MeshSingleFlankRatingMethodB1: 'ISO10300BevelMeshSingleFlankRatingMethodB1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO10300BevelMeshSingleFlankRatingMethodB1

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso10300_bevel_mesh_single_flank_rating_method_b2(self) -> '_421.ISO10300MeshSingleFlankRatingBevelMethodB2':
        """ISO10300MeshSingleFlankRatingBevelMethodB2: 'ISO10300BevelMeshSingleFlankRatingMethodB2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO10300BevelMeshSingleFlankRatingMethodB2

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_542.ConicalMeshedGearRating]':
        """List[ConicalMeshedGearRating]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_in_mesh(self) -> 'List[_542.ConicalMeshedGearRating]':
        """List[ConicalMeshedGearRating]: 'GearsInMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsInMesh

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearMeshRating._Cast_BevelGearMeshRating':
        return self._Cast_BevelGearMeshRating(self)
