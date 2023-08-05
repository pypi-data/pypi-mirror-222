"""_951.py

ZerolBevelGearSetDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.bevel import _1178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearSetDesign')

if TYPE_CHECKING:
    from mastapy.gears import _350
    from mastapy.gears.gear_designs.zerol_bevel import _949, _950


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetDesign',)


class ZerolBevelGearSetDesign(_1178.BevelGearSetDesign):
    """ZerolBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_DESIGN

    class _Cast_ZerolBevelGearSetDesign:
        """Special nested class for casting ZerolBevelGearSetDesign to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetDesign'):
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
        def zerol_bevel_gear_set_design(self) -> 'ZerolBevelGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self) -> 'int':
        """int: 'MinimumNumberOfTeethForRecommendedToothProportions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions

        if temp is None:
            return 0

        return temp

    @property
    def tooth_taper_zerol(self) -> '_350.ZerolBevelGleasonToothTaperOption':
        """ZerolBevelGleasonToothTaperOption: 'ToothTaperZerol' is the original name of this property."""

        temp = self.wrapped.ToothTaperZerol

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.ZerolBevelGleasonToothTaperOption')
        return constructor.new_from_mastapy('mastapy.gears._350', 'ZerolBevelGleasonToothTaperOption')(value) if value is not None else None

    @tooth_taper_zerol.setter
    def tooth_taper_zerol(self, value: '_350.ZerolBevelGleasonToothTaperOption'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.ZerolBevelGleasonToothTaperOption')
        self.wrapped.ToothTaperZerol = value

    @property
    def gears(self) -> 'List[_949.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def zerol_bevel_meshes(self) -> 'List[_950.ZerolBevelGearMeshDesign]':
        """List[ZerolBevelGearMeshDesign]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetDesign._Cast_ZerolBevelGearSetDesign':
        return self._Cast_ZerolBevelGearSetDesign(self)
