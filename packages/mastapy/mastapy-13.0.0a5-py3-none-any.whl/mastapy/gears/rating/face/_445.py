"""_445.py

FaceGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearMeshRating')

if TYPE_CHECKING:
    from mastapy.gears import _324
    from mastapy.gears.gear_designs.face import _988
    from mastapy.gears.rating.face import _448, _446
    from mastapy.gears.load_case.face import _878
    from mastapy.gears.rating.cylindrical.iso6336 import _511


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshRating',)


class FaceGearMeshRating(_358.GearMeshRating):
    """FaceGearMeshRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_RATING

    class _Cast_FaceGearMeshRating:
        """Special nested class for casting FaceGearMeshRating to subclasses."""

        def __init__(self, parent: 'FaceGearMeshRating'):
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
        def face_gear_mesh_rating(self) -> 'FaceGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_324.GearFlanks':
        """GearFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearFlanks')
        return constructor.new_from_mastapy('mastapy.gears._324', 'GearFlanks')(value) if value is not None else None

    @property
    def face_gear_mesh(self) -> '_988.FaceGearMeshDesign':
        """FaceGearMeshDesign: 'FaceGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_rating(self) -> '_448.FaceGearSetRating':
        """FaceGearSetRating: 'GearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case(self) -> '_878.FaceMeshLoadCase':
        """FaceMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_single_flank_rating(self) -> '_511.ISO63362006MeshSingleFlankRating':
        """ISO63362006MeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear_ratings(self) -> 'List[_446.FaceGearRating]':
        """List[FaceGearRating]: 'FaceGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearMeshRating._Cast_FaceGearMeshRating':
        return self._Cast_FaceGearMeshRating(self)
