"""_1365.py

SpeedTorqueLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1347
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedTorqueLoadCase')

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1343, _1361, _1342


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedTorqueLoadCase',)


class SpeedTorqueLoadCase(_1347.ElectricMachineLoadCase):
    """SpeedTorqueLoadCase

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_LOAD_CASE

    class _Cast_SpeedTorqueLoadCase:
        """Special nested class for casting SpeedTorqueLoadCase to subclasses."""

        def __init__(self, parent: 'SpeedTorqueLoadCase'):
            self._parent = parent

        @property
        def electric_machine_load_case(self):
            return self._parent._cast(_1347.ElectricMachineLoadCase)

        @property
        def electric_machine_load_case_base(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1348
            
            return self._parent._cast(_1348.ElectricMachineLoadCaseBase)

        @property
        def speed_torque_load_case(self) -> 'SpeedTorqueLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpeedTorqueLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_strategy(self) -> '_1343.ElectricMachineControlStrategy':
        """ElectricMachineControlStrategy: 'ControlStrategy' is the original name of this property."""

        temp = self.wrapped.ControlStrategy

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.ElectricMachineControlStrategy')
        return constructor.new_from_mastapy('mastapy.electric_machines.load_cases_and_analyses._1343', 'ElectricMachineControlStrategy')(value) if value is not None else None

    @control_strategy.setter
    def control_strategy(self, value: '_1343.ElectricMachineControlStrategy'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.ElectricMachineControlStrategy')
        self.wrapped.ControlStrategy = value

    @property
    def include_resistive_voltages(self) -> 'bool':
        """bool: 'IncludeResistiveVoltages' is the original name of this property."""

        temp = self.wrapped.IncludeResistiveVoltages

        if temp is None:
            return False

        return temp

    @include_resistive_voltages.setter
    def include_resistive_voltages(self, value: 'bool'):
        self.wrapped.IncludeResistiveVoltages = bool(value) if value is not None else False

    @property
    def load_specification(self) -> '_1361.SpecifyTorqueOrCurrent':
        """SpecifyTorqueOrCurrent: 'LoadSpecification' is the original name of this property."""

        temp = self.wrapped.LoadSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpecifyTorqueOrCurrent')
        return constructor.new_from_mastapy('mastapy.electric_machines.load_cases_and_analyses._1361', 'SpecifyTorqueOrCurrent')(value) if value is not None else None

    @load_specification.setter
    def load_specification(self, value: '_1361.SpecifyTorqueOrCurrent'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.SpecifyTorqueOrCurrent')
        self.wrapped.LoadSpecification = value

    @property
    def target_torque(self) -> 'float':
        """float: 'TargetTorque' is the original name of this property."""

        temp = self.wrapped.TargetTorque

        if temp is None:
            return 0.0

        return temp

    @target_torque.setter
    def target_torque(self, value: 'float'):
        self.wrapped.TargetTorque = float(value) if value is not None else 0.0

    @property
    def basic_mechanical_loss_settings(self) -> '_1342.ElectricMachineBasicMechanicalLossSettings':
        """ElectricMachineBasicMechanicalLossSettings: 'BasicMechanicalLossSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicMechanicalLossSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpeedTorqueLoadCase._Cast_SpeedTorqueLoadCase':
        return self._Cast_SpeedTorqueLoadCase(self)
