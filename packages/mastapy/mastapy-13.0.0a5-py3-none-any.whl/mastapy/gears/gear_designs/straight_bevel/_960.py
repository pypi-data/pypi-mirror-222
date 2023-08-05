"""_960.py

StraightBevelGearSetDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelGearSetDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _958, _959


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetDesign',)


class StraightBevelGearSetDesign(_1178.BevelGearSetDesign):
    """StraightBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_DESIGN

    class _Cast_StraightBevelGearSetDesign:
        """Special nested class for casting StraightBevelGearSetDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelGearSetDesign'):
            self._parent = parent

        @property
        def bevel_gear_set_design(self):
            return self._parent._cast(_1178.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1191
            
            return self._parent._cast(_1191.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(self):
            from mastapy.gears.gear_designs.conical import _1152
            
            return self._parent._cast(_1152.ConicalGearSetDesign)

        @property
        def gear_set_design(self):
            from mastapy.gears.gear_designs import _947
            
            return self._parent._cast(_947.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def straight_bevel_gear_set_design(self) -> 'StraightBevelGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self) -> 'List[_958.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears(self) -> 'List[_958.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes(self) -> 'List[_959.StraightBevelGearMeshDesign]':
        """List[StraightBevelGearMeshDesign]: 'StraightBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearSetDesign._Cast_StraightBevelGearSetDesign':
        return self._Cast_StraightBevelGearSetDesign(self)
