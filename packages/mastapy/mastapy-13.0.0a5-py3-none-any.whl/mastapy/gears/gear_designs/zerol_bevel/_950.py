"""_950.py

ZerolBevelGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _951, _949, _952


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshDesign',)


class ZerolBevelGearMeshDesign(_1177.BevelGearMeshDesign):
    """ZerolBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_DESIGN

    class _Cast_ZerolBevelGearMeshDesign:
        """Special nested class for casting ZerolBevelGearMeshDesign to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshDesign'):
            self._parent = parent

        @property
        def bevel_gear_mesh_design(self):
            return self._parent._cast(_1177.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1190
            
            return self._parent._cast(_1190.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.conical import _1151
            
            return self._parent._cast(_1151.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(self):
            from mastapy.gears.gear_designs import _946
            
            return self._parent._cast(_946.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(self) -> 'ZerolBevelGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self) -> '_951.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears(self) -> 'List[_949.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshed_gears(self) -> 'List[_952.ZerolBevelMeshedGearDesign]':
        """List[ZerolBevelMeshedGearDesign]: 'ZerolBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearMeshDesign._Cast_ZerolBevelGearMeshDesign':
        return self._Cast_ZerolBevelGearMeshDesign(self)
