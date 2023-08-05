﻿"""_2437.py

FlexiblePinAssembly
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_FLEXIBLE_PIN_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2507


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssembly',)


class FlexiblePinAssembly(_2459.SpecialisedAssembly):
    """FlexiblePinAssembly

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY

    class _Cast_FlexiblePinAssembly:
        """Special nested class for casting FlexiblePinAssembly to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssembly'):
            self._parent = parent

        @property
        def specialised_assembly(self):
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
        def flexible_pin_assembly(self) -> 'FlexiblePinAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_to_diameter_ratio(self) -> 'float':
        """float: 'LengthToDiameterRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

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
    def maximum_pin_diameter_from_planet_bore(self) -> 'float':
        """float: 'MaximumPinDiameterFromPlanetBore' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPinDiameterFromPlanetBore

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_fatigue_safety_factor(self) -> 'float':
        """float: 'MinimumFatigueSafetyFactor' is the original name of this property."""

        temp = self.wrapped.MinimumFatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @minimum_fatigue_safety_factor.setter
    def minimum_fatigue_safety_factor(self, value: 'float'):
        self.wrapped.MinimumFatigueSafetyFactor = float(value) if value is not None else 0.0

    @property
    def pin_diameter(self) -> 'float':
        """float: 'PinDiameter' is the original name of this property."""

        temp = self.wrapped.PinDiameter

        if temp is None:
            return 0.0

        return temp

    @pin_diameter.setter
    def pin_diameter(self, value: 'float'):
        self.wrapped.PinDiameter = float(value) if value is not None else 0.0

    @property
    def pin_position_tolerance(self) -> 'float':
        """float: 'PinPositionTolerance' is the original name of this property."""

        temp = self.wrapped.PinPositionTolerance

        if temp is None:
            return 0.0

        return temp

    @pin_position_tolerance.setter
    def pin_position_tolerance(self, value: 'float'):
        self.wrapped.PinPositionTolerance = float(value) if value is not None else 0.0

    @property
    def pitch_iso_quality_grade(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'PitchISOQualityGrade' is the original name of this property."""

        temp = self.wrapped.PitchISOQualityGrade

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_int')(temp) if temp is not None else 0

    @pitch_iso_quality_grade.setter
    def pitch_iso_quality_grade(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.PitchISOQualityGrade = value

    @property
    def planet_gear_bore_diameter(self) -> 'float':
        """float: 'PlanetGearBoreDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearBoreDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def spindle_outer_diameter(self) -> 'float':
        """float: 'SpindleOuterDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpindleOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def total_pin_length(self) -> 'float':
        """float: 'TotalPinLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPinLength

        if temp is None:
            return 0.0

        return temp

    @property
    def unsupported_pin_length(self) -> 'float':
        """float: 'UnsupportedPinLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnsupportedPinLength

        if temp is None:
            return 0.0

        return temp

    @property
    def planet_gear(self) -> '_2507.CylindricalGear':
        """CylindricalGear: 'PlanetGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FlexiblePinAssembly._Cast_FlexiblePinAssembly':
        return self._Cast_FlexiblePinAssembly(self)
