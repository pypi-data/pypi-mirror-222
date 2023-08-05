"""_967.py

SpiralBevelGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.SpiralBevel', 'SpiralBevelGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _968, _966, _969


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMeshDesign',)


class SpiralBevelGearMeshDesign(_1177.BevelGearMeshDesign):
    """SpiralBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_DESIGN

    class _Cast_SpiralBevelGearMeshDesign:
        """Special nested class for casting SpiralBevelGearMeshDesign to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearMeshDesign'):
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
        def spiral_bevel_gear_mesh_design(self) -> 'SpiralBevelGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def wheel_inner_blade_angle_convex(self) -> 'float':
        """float: 'WheelInnerBladeAngleConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelInnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_blade_angle_concave(self) -> 'float':
        """float: 'WheelOuterBladeAngleConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelOuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def spiral_bevel_gear_set(self) -> '_968.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'SpiralBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gears(self) -> 'List[_966.SpiralBevelGearDesign]':
        """List[SpiralBevelGearDesign]: 'SpiralBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshed_gears(self) -> 'List[_969.SpiralBevelMeshedGearDesign]':
        """List[SpiralBevelMeshedGearDesign]: 'SpiralBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearMeshDesign._Cast_SpiralBevelGearMeshDesign':
        return self._Cast_SpiralBevelGearMeshDesign(self)
