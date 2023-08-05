﻿"""_2455.py

PowerLoad
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2462
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')

if TYPE_CHECKING:
    from mastapy.electric_machines import _1256
    from mastapy.system_model.part_model import _2432, _2464
    from mastapy.math_utility.measured_data import _1556
    from mastapy.system_model import _2206
    from mastapy.materials.efficiency import _296


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoad',)


class PowerLoad(_2462.VirtualComponent):
    """PowerLoad

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD

    class _Cast_PowerLoad:
        """Special nested class for casting PowerLoad to subclasses."""

        def __init__(self, parent: 'PowerLoad'):
            self._parent = parent

        @property
        def virtual_component(self):
            return self._parent._cast(_2462.VirtualComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def power_load(self) -> 'PowerLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_length_of_stator(self) -> 'float':
        """float: 'EffectiveLengthOfStator' is the original name of this property."""

        temp = self.wrapped.EffectiveLengthOfStator

        if temp is None:
            return 0.0

        return temp

    @effective_length_of_stator.setter
    def effective_length_of_stator(self, value: 'float'):
        self.wrapped.EffectiveLengthOfStator = float(value) if value is not None else 0.0

    @property
    def electric_machine_detail_selector(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail: 'ElectricMachineDetailSelector' is the original name of this property."""

        temp = self.wrapped.ElectricMachineDetailSelector

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_ElectricMachineDetail')(temp) if temp is not None else None

    @electric_machine_detail_selector.setter
    def electric_machine_detail_selector(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ElectricMachineDetailSelector = value

    @property
    def electric_machine_search_region_specification_method(self) -> '_2432.ElectricMachineSearchRegionSpecificationMethod':
        """ElectricMachineSearchRegionSpecificationMethod: 'ElectricMachineSearchRegionSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.ElectricMachineSearchRegionSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod')
        return constructor.new_from_mastapy('mastapy.system_model.part_model._2432', 'ElectricMachineSearchRegionSpecificationMethod')(value) if value is not None else None

    @electric_machine_search_region_specification_method.setter
    def electric_machine_search_region_specification_method(self, value: '_2432.ElectricMachineSearchRegionSpecificationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.ElectricMachineSearchRegionSpecificationMethod')
        self.wrapped.ElectricMachineSearchRegionSpecificationMethod = value

    @property
    def engine_fuel_consumption_grid(self) -> '_1556.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'EngineFuelConsumptionGrid' is the original name of this property."""

        temp = self.wrapped.EngineFuelConsumptionGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @engine_fuel_consumption_grid.setter
    def engine_fuel_consumption_grid(self, value: '_1556.GriddedSurfaceAccessor'):
        self.wrapped.EngineFuelConsumptionGrid = value

    @property
    def engine_torque_grid(self) -> '_1556.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'EngineTorqueGrid' is the original name of this property."""

        temp = self.wrapped.EngineTorqueGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @engine_torque_grid.setter
    def engine_torque_grid(self, value: '_1556.GriddedSurfaceAccessor'):
        self.wrapped.EngineTorqueGrid = value

    @property
    def include_in_torsional_stiffness_calculation(self) -> 'bool':
        """bool: 'IncludeInTorsionalStiffnessCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation

        if temp is None:
            return False

        return temp

    @include_in_torsional_stiffness_calculation.setter
    def include_in_torsional_stiffness_calculation(self, value: 'bool'):
        self.wrapped.IncludeInTorsionalStiffnessCalculation = bool(value) if value is not None else False

    @property
    def inner_diameter_of_stator_teeth(self) -> 'float':
        """float: 'InnerDiameterOfStatorTeeth' is the original name of this property."""

        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    def inner_diameter_of_stator_teeth(self, value: 'float'):
        self.wrapped.InnerDiameterOfStatorTeeth = float(value) if value is not None else 0.0

    @property
    def number_of_wheels(self) -> 'int':
        """int: 'NumberOfWheels' is the original name of this property."""

        temp = self.wrapped.NumberOfWheels

        if temp is None:
            return 0

        return temp

    @number_of_wheels.setter
    def number_of_wheels(self, value: 'int'):
        self.wrapped.NumberOfWheels = int(value) if value is not None else 0

    @property
    def number_of_blades(self) -> 'int':
        """int: 'NumberOfBlades' is the original name of this property."""

        temp = self.wrapped.NumberOfBlades

        if temp is None:
            return 0

        return temp

    @number_of_blades.setter
    def number_of_blades(self, value: 'int'):
        self.wrapped.NumberOfBlades = int(value) if value is not None else 0

    @property
    def number_of_slots(self) -> 'int':
        """int: 'NumberOfSlots' is the original name of this property."""

        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    def number_of_slots(self, value: 'int'):
        self.wrapped.NumberOfSlots = int(value) if value is not None else 0

    @property
    def positive_is_forwards(self) -> 'bool':
        """bool: 'PositiveIsForwards' is the original name of this property."""

        temp = self.wrapped.PositiveIsForwards

        if temp is None:
            return False

        return temp

    @positive_is_forwards.setter
    def positive_is_forwards(self, value: 'bool'):
        self.wrapped.PositiveIsForwards = bool(value) if value is not None else False

    @property
    def power_load_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadType':
        """enum_with_selected_value.EnumWithSelectedValue_PowerLoadType: 'PowerLoadType' is the original name of this property."""

        temp = self.wrapped.PowerLoadType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @power_load_type.setter
    def power_load_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PowerLoadType = value

    @property
    def torsional_stiffness(self) -> 'float':
        """float: 'TorsionalStiffness' is the original name of this property."""

        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'float'):
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def tyre_rolling_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TyreRollingRadius' is the original name of this property."""

        temp = self.wrapped.TyreRollingRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @tyre_rolling_radius.setter
    def tyre_rolling_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TyreRollingRadius = value

    @property
    def width_for_drawing(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WidthForDrawing' is the original name of this property."""

        temp = self.wrapped.WidthForDrawing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @width_for_drawing.setter
    def width_for_drawing(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WidthForDrawing = value

    @property
    def electric_machine_detail(self) -> '_1256.ElectricMachineDetail':
        """ElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def oil_pump_detail(self) -> '_296.OilPumpDetail':
        """OilPumpDetail: 'OilPumpDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilPumpDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_blade_details(self) -> '_2464.WindTurbineSingleBladeDetails':
        """WindTurbineSingleBladeDetails: 'SingleBladeDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleBladeDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PowerLoad._Cast_PowerLoad':
        return self._Cast_PowerLoad(self)
