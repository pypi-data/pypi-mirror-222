"""_988.py

FaceGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _992, _986


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshDesign',)


class FaceGearMeshDesign(_946.GearMeshDesign):
    """FaceGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_DESIGN

    class _Cast_FaceGearMeshDesign:
        """Special nested class for casting FaceGearMeshDesign to subclasses."""

        def __init__(self, parent: 'FaceGearMeshDesign'):
            self._parent = parent

        @property
        def gear_mesh_design(self):
            return self._parent._cast(_946.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def face_gear_mesh_design(self) -> 'FaceGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def working_normal_pressure_angle(self) -> 'float':
        """float: 'WorkingNormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_gear_set(self) -> '_992.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears(self) -> 'List[_986.FaceGearDesign]':
        """List[FaceGearDesign]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearMeshDesign._Cast_FaceGearMeshDesign':
        return self._Cast_FaceGearMeshDesign(self)
