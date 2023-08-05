"""_1151.py

ConicalGearMeshDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs import _946
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearMeshDesign')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1183, _1180, _1184


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshDesign',)


class ConicalGearMeshDesign(_946.GearMeshDesign):
    """ConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_DESIGN

    class _Cast_ConicalGearMeshDesign:
        """Special nested class for casting ConicalGearMeshDesign to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshDesign'):
            self._parent = parent

        @property
        def gear_mesh_design(self):
            return self._parent._cast(_946.GearMeshDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _950
            
            return self._parent._cast(_950.ZerolBevelGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _959
            
            return self._parent._cast(_959.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _963
            
            return self._parent._cast(_963.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _967
            
            return self._parent._cast(_967.SpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _971
            
            return self._parent._cast(_971.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _975
            
            return self._parent._cast(_975.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _979
            
            return self._parent._cast(_979.KlingelnbergConicalGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.hypoid import _983
            
            return self._parent._cast(_983.HypoidGearMeshDesign)

        @property
        def bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.bevel import _1177
            
            return self._parent._cast(_1177.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1190
            
            return self._parent._cast(_1190.AGMAGleasonConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(self) -> 'ConicalGearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driven_machine_characteristic(self) -> '_1183.MachineCharacteristicAGMAKlingelnberg':
        """MachineCharacteristicAGMAKlingelnberg: 'DrivenMachineCharacteristic' is the original name of this property."""

        temp = self.wrapped.DrivenMachineCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.bevel._1183', 'MachineCharacteristicAGMAKlingelnberg')(value) if value is not None else None

    @driven_machine_characteristic.setter
    def driven_machine_characteristic(self, value: '_1183.MachineCharacteristicAGMAKlingelnberg'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg')
        self.wrapped.DrivenMachineCharacteristic = value

    @property
    def driven_machine_characteristic_gleason(self) -> '_1180.DrivenMachineCharacteristicGleason':
        """DrivenMachineCharacteristicGleason: 'DrivenMachineCharacteristicGleason' is the original name of this property."""

        temp = self.wrapped.DrivenMachineCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.bevel._1180', 'DrivenMachineCharacteristicGleason')(value) if value is not None else None

    @driven_machine_characteristic_gleason.setter
    def driven_machine_characteristic_gleason(self, value: '_1180.DrivenMachineCharacteristicGleason'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.DrivenMachineCharacteristicGleason')
        self.wrapped.DrivenMachineCharacteristicGleason = value

    @property
    def maximum_normal_backlash(self) -> 'float':
        """float: 'MaximumNormalBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_normal_backlash(self) -> 'float':
        """float: 'MinimumNormalBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNormalBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactor' is the original name of this property."""

        temp = self.wrapped.OverloadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @overload_factor.setter
    def overload_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OverloadFactor = value

    @property
    def pinion_full_circle_edge_radius(self) -> 'float':
        """float: 'PinionFullCircleEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionFullCircleEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def prime_mover_characteristic(self) -> '_1183.MachineCharacteristicAGMAKlingelnberg':
        """MachineCharacteristicAGMAKlingelnberg: 'PrimeMoverCharacteristic' is the original name of this property."""

        temp = self.wrapped.PrimeMoverCharacteristic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.bevel._1183', 'MachineCharacteristicAGMAKlingelnberg')(value) if value is not None else None

    @prime_mover_characteristic.setter
    def prime_mover_characteristic(self, value: '_1183.MachineCharacteristicAGMAKlingelnberg'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.MachineCharacteristicAGMAKlingelnberg')
        self.wrapped.PrimeMoverCharacteristic = value

    @property
    def prime_mover_characteristic_gleason(self) -> '_1184.PrimeMoverCharacteristicGleason':
        """PrimeMoverCharacteristicGleason: 'PrimeMoverCharacteristicGleason' is the original name of this property."""

        temp = self.wrapped.PrimeMoverCharacteristicGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason')
        return constructor.new_from_mastapy('mastapy.gears.gear_designs.bevel._1184', 'PrimeMoverCharacteristicGleason')(value) if value is not None else None

    @prime_mover_characteristic_gleason.setter
    def prime_mover_characteristic_gleason(self, value: '_1184.PrimeMoverCharacteristicGleason'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.GearDesigns.Bevel.PrimeMoverCharacteristicGleason')
        self.wrapped.PrimeMoverCharacteristicGleason = value

    @property
    def shaft_angle(self) -> 'float':
        """float: 'ShaftAngle' is the original name of this property."""

        temp = self.wrapped.ShaftAngle

        if temp is None:
            return 0.0

        return temp

    @shaft_angle.setter
    def shaft_angle(self, value: 'float'):
        self.wrapped.ShaftAngle = float(value) if value is not None else 0.0

    @property
    def specified_backlash_range_max(self) -> 'float':
        """float: 'SpecifiedBacklashRangeMax' is the original name of this property."""

        temp = self.wrapped.SpecifiedBacklashRangeMax

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_max.setter
    def specified_backlash_range_max(self, value: 'float'):
        self.wrapped.SpecifiedBacklashRangeMax = float(value) if value is not None else 0.0

    @property
    def specified_backlash_range_min(self) -> 'float':
        """float: 'SpecifiedBacklashRangeMin' is the original name of this property."""

        temp = self.wrapped.SpecifiedBacklashRangeMin

        if temp is None:
            return 0.0

        return temp

    @specified_backlash_range_min.setter
    def specified_backlash_range_min(self, value: 'float'):
        self.wrapped.SpecifiedBacklashRangeMin = float(value) if value is not None else 0.0

    @property
    def specify_backlash(self) -> 'bool':
        """bool: 'SpecifyBacklash' is the original name of this property."""

        temp = self.wrapped.SpecifyBacklash

        if temp is None:
            return False

        return temp

    @specify_backlash.setter
    def specify_backlash(self, value: 'bool'):
        self.wrapped.SpecifyBacklash = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'ConicalGearMeshDesign._Cast_ConicalGearMeshDesign':
        return self._Cast_ConicalGearMeshDesign(self)
