"""_956.py

WormGearSetDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs import _947
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Worm', 'WormGearSetDesign')

if TYPE_CHECKING:
    from mastapy.gears import _349
    from mastapy.gears.gear_designs.worm import _954, _955


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetDesign',)


class WormGearSetDesign(_947.GearSetDesign):
    """WormGearSetDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DESIGN

    class _Cast_WormGearSetDesign:
        """Special nested class for casting WormGearSetDesign to subclasses."""

        def __init__(self, parent: 'WormGearSetDesign'):
            self._parent = parent

        @property
        def gear_set_design(self):
            return self._parent._cast(_947.GearSetDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def worm_gear_set_design(self) -> 'WormGearSetDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_module(self) -> 'float':
        """float: 'AxialModule' is the original name of this property."""

        temp = self.wrapped.AxialModule

        if temp is None:
            return 0.0

        return temp

    @axial_module.setter
    def axial_module(self, value: 'float'):
        self.wrapped.AxialModule = float(value) if value is not None else 0.0

    @property
    def axial_pressure_angle(self) -> 'float':
        """float: 'AxialPressureAngle' is the original name of this property."""

        temp = self.wrapped.AxialPressureAngle

        if temp is None:
            return 0.0

        return temp

    @axial_pressure_angle.setter
    def axial_pressure_angle(self, value: 'float'):
        self.wrapped.AxialPressureAngle = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    def normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def worm_type(self) -> '_349.WormType':
        """WormType: 'WormType' is the original name of this property."""

        temp = self.wrapped.WormType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.WormType')
        return constructor.new_from_mastapy('mastapy.gears._349', 'WormType')(value) if value is not None else None

    @worm_type.setter
    def worm_type(self, value: '_349.WormType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.WormType')
        self.wrapped.WormType = value

    @property
    def gears(self) -> 'List[_954.WormGearDesign]':
        """List[WormGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears(self) -> 'List[_954.WormGearDesign]':
        """List[WormGearDesign]: 'WormGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes(self) -> 'List[_955.WormGearMeshDesign]':
        """List[WormGearMeshDesign]: 'WormMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetDesign._Cast_WormGearSetDesign':
        return self._Cast_WormGearSetDesign(self)
