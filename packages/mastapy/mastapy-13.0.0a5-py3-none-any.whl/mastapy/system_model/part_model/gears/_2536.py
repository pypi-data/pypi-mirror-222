"""_2536.py

ZerolBevelGearSet
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2502
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _951
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.connections_and_sockets.gears import _2314


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSet',)


class ZerolBevelGearSet(_2502.BevelGearSet):
    """ZerolBevelGearSet

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET

    class _Cast_ZerolBevelGearSet:
        """Special nested class for casting ZerolBevelGearSet to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSet'):
            self._parent = parent

        @property
        def bevel_gear_set(self):
            return self._parent._cast(_2502.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2496
            
            return self._parent._cast(_2496.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self):
            from mastapy.system_model.part_model.gears import _2506
            
            return self._parent._cast(_2506.ConicalGearSet)

        @property
        def gear_set(self):
            from mastapy.system_model.part_model.gears import _2514
            
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
        def zerol_bevel_gear_set(self) -> 'ZerolBevelGearSet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_951.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_set_design(self) -> '_951.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears(self) -> 'List[_2535.ZerolBevelGear]':
        """List[ZerolBevelGear]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes(self) -> 'List[_2314.ZerolBevelGearMesh]':
        """List[ZerolBevelGearMesh]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSet._Cast_ZerolBevelGearSet':
        return self._Cast_ZerolBevelGearSet(self)
