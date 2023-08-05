﻿"""_983.py

HypoidGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.agma_gleason_conical import _1190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Hypoid', 'HypoidGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _984, _982, _985


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshDesign',)


class HypoidGearMeshDesign(_1190.AGMAGleasonConicalGearMeshDesign):
    """HypoidGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_DESIGN

    class _Cast_HypoidGearMeshDesign:
        """Special nested class for casting HypoidGearMeshDesign to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshDesign'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_design(self):
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
        def hypoid_gear_mesh_design(self) -> 'HypoidGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hypoid_gear_set(self) -> '_984.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'HypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears(self) -> 'List[_982.HypoidGearDesign]':
        """List[HypoidGearDesign]: 'HypoidGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshed_gears(self) -> 'List[_985.HypoidMeshedGearDesign]':
        """List[HypoidMeshedGearDesign]: 'HypoidMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearMeshDesign._Cast_HypoidGearMeshDesign':
        return self._Cast_HypoidGearMeshDesign(self)
