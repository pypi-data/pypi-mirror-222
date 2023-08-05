﻿"""_1335.py

OnLoadElectricMachineResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines.results import _1317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ON_LOAD_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'OnLoadElectricMachineResults')

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1355, _1352
    from mastapy.electric_machines import _1307


__docformat__ = 'restructuredtext en'
__all__ = ('OnLoadElectricMachineResults',)


class OnLoadElectricMachineResults(_1317.ElectricMachineResults):
    """OnLoadElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _ON_LOAD_ELECTRIC_MACHINE_RESULTS

    class _Cast_OnLoadElectricMachineResults:
        """Special nested class for casting OnLoadElectricMachineResults to subclasses."""

        def __init__(self, parent: 'OnLoadElectricMachineResults'):
            self._parent = parent

        @property
        def electric_machine_results(self):
            return self._parent._cast(_1317.ElectricMachineResults)

        @property
        def on_load_electric_machine_results(self) -> 'OnLoadElectricMachineResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OnLoadElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_power_factor(self) -> 'float':
        """float: 'AveragePowerFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def average_power_factor_angle(self) -> 'float':
        """float: 'AveragePowerFactorAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactorAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def average_power_factor_with_harmonic_distortion_adjustment(self) -> 'float':
        """float: 'AveragePowerFactorWithHarmonicDistortionAdjustment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactorWithHarmonicDistortionAdjustment

        if temp is None:
            return 0.0

        return temp

    @property
    def average_torque_dq(self) -> 'float':
        """float: 'AverageTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def dc_winding_losses(self) -> 'float':
        """float: 'DCWindingLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DCWindingLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self) -> 'float':
        """float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_loading(self) -> 'float':
        """float: 'ElectricalLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def input_power(self) -> 'float':
        """float: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def line_resistance(self) -> 'float':
        """float: 'LineResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_peak(self) -> 'float':
        """float: 'LineToLineTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_rms(self) -> 'float':
        """float: 'LineToLineTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        """float: 'LineToLineTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageTotalHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def motor_constant(self) -> 'float':
        """float: 'MotorConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MotorConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def motoring_or_generating(self) -> '_1355.MotoringOrGenerating':
        """MotoringOrGenerating: 'MotoringOrGenerating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MotoringOrGenerating

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.MotoringOrGenerating')
        return constructor.new_from_mastapy('mastapy.electric_machines.load_cases_and_analyses._1355', 'MotoringOrGenerating')(value) if value is not None else None

    @property
    def output_power(self) -> 'float':
        """float: 'OutputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OutputPower

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance(self) -> 'float':
        """float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_peak(self) -> 'float':
        """float: 'PhaseResistiveVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_rms(self) -> 'float':
        """float: 'PhaseResistiveVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_drms(self) -> 'float':
        """float: 'PhaseResistiveVoltageDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistive_voltage_qrms(self) -> 'float':
        """float: 'PhaseResistiveVoltageQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageQRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_peak(self) -> 'float':
        """float: 'PhaseTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_rms(self) -> 'float':
        """float: 'PhaseTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        """float: 'PhaseTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltageTotalHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def power_factor_direction(self) -> '_1352.LeadingOrLagging':
        """LeadingOrLagging: 'PowerFactorDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFactorDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses.LeadingOrLagging')
        return constructor.new_from_mastapy('mastapy.electric_machines.load_cases_and_analyses._1352', 'LeadingOrLagging')(value) if value is not None else None

    @property
    def power_from_electromagnetic_analysis(self) -> 'float':
        """float: 'PowerFromElectromagneticAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFromElectromagneticAnalysis

        if temp is None:
            return 0.0

        return temp

    @property
    def stall_current(self) -> 'float':
        """float: 'StallCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StallCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def stall_torque(self) -> 'float':
        """float: 'StallTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StallTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_constant(self) -> 'float':
        """float: 'TorqueConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ripple_percentage_mst(self) -> 'float':
        """float: 'TorqueRipplePercentageMST' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRipplePercentageMST

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_resistivity(self) -> 'float':
        """float: 'WindingMaterialResistivity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialResistivity

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_skin_depth(self) -> 'float':
        """float: 'WindingSkinDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingSkinDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def windings(self) -> '_1307.Windings':
        """Windings: 'Windings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Windings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'OnLoadElectricMachineResults._Cast_OnLoadElectricMachineResults':
        return self._Cast_OnLoadElectricMachineResults(self)
