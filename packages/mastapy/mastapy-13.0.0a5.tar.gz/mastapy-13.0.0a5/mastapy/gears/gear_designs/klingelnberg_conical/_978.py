"""_978.py

KlingelnbergConicalGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs.conical import _1150
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_KLINGELNBERG_CONICAL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical', 'KlingelnbergConicalGearDesign')

if TYPE_CHECKING:
    from mastapy.gears.materials import _598


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalGearDesign',)


class KlingelnbergConicalGearDesign(_1150.ConicalGearDesign):
    """KlingelnbergConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_DESIGN

    class _Cast_KlingelnbergConicalGearDesign:
        """Special nested class for casting KlingelnbergConicalGearDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergConicalGearDesign'):
            self._parent = parent

        @property
        def conical_gear_design(self):
            return self._parent._cast(_1150.ConicalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _944
            
            return self._parent._cast(_944.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _970
            
            return self._parent._cast(_970.KlingelnbergCycloPalloidSpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _974
            
            return self._parent._cast(_974.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(self) -> 'KlingelnbergConicalGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self) -> 'float':
        """float: 'Addendum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_edge_radius(self) -> 'float':
        """float: 'CutterEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness_rz(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankRoughnessRZ' is the original name of this property."""

        temp = self.wrapped.FlankRoughnessRZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @flank_roughness_rz.setter
    def flank_roughness_rz(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FlankRoughnessRZ = value

    @property
    def material(self) -> 'str':
        """str: 'Material' is the original name of this property."""

        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ''

        return temp

    @material.setter
    def material(self, value: 'str'):
        self.wrapped.Material.SetSelectedItem(str(value) if value is not None else '')

    @property
    def pitch_cone_angle(self) -> 'float':
        """float: 'PitchConeAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchConeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_sensitivity_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RelativeSensitivityFactor' is the original name of this property."""

        temp = self.wrapped.RelativeSensitivityFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @relative_sensitivity_factor.setter
    def relative_sensitivity_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RelativeSensitivityFactor = value

    @property
    def stress_correction_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StressCorrectionFactor' is the original name of this property."""

        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @stress_correction_factor.setter
    def stress_correction_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StressCorrectionFactor = value

    @property
    def tooth_form_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ToothFormFactor' is the original name of this property."""

        temp = self.wrapped.ToothFormFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @tooth_form_factor.setter
    def tooth_form_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ToothFormFactor = value

    @property
    def klingelnberg_cyclo_palloid_gear_material(self) -> '_598.KlingelnbergCycloPalloidConicalGearMaterial':
        """KlingelnbergCycloPalloidConicalGearMaterial: 'KlingelnbergCycloPalloidGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidGearMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergConicalGearDesign._Cast_KlingelnbergConicalGearDesign':
        return self._Cast_KlingelnbergConicalGearDesign(self)
