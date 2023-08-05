"""_2511.py

FaceGearSet
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _992
    from mastapy.system_model.part_model.gears import _2510
    from mastapy.system_model.connections_and_sockets.gears import _2294


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSet',)


class FaceGearSet(_2514.GearSet):
    """FaceGearSet

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET

    class _Cast_FaceGearSet:
        """Special nested class for casting FaceGearSet to subclasses."""

        def __init__(self, parent: 'FaceGearSet'):
            self._parent = parent

        @property
        def gear_set(self):
            return self._parent._cast(_2514.GearSet)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def face_gear_set(self) -> 'FaceGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_992.FaceGearSetDesign':
        """FaceGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear_set_design(self) -> '_992.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears(self) -> 'List[_2510.FaceGear]':
        """List[FaceGear]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes(self) -> 'List[_2294.FaceGearMesh]':
        """List[FaceGearMesh]: 'FaceMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSet._Cast_FaceGearSet':
        return self._Cast_FaceGearSet(self)
