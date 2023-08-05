﻿"""_1359.py

SingleOperatingPointAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1341
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_OPERATING_POINT_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SingleOperatingPointAnalysis')

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1321
    from mastapy.electric_machines.load_cases_and_analyses import _1347, _1360


__docformat__ = 'restructuredtext en'
__all__ = ('SingleOperatingPointAnalysis',)


class SingleOperatingPointAnalysis(_1341.ElectricMachineAnalysis):
    """SingleOperatingPointAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_OPERATING_POINT_ANALYSIS

    class _Cast_SingleOperatingPointAnalysis:
        """Special nested class for casting SingleOperatingPointAnalysis to subclasses."""

        def __init__(self, parent: 'SingleOperatingPointAnalysis'):
            self._parent = parent

        @property
        def electric_machine_analysis(self):
            return self._parent._cast(_1341.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_analysis(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1345
            
            return self._parent._cast(_1345.ElectricMachineFEAnalysis)

        @property
        def single_operating_point_analysis(self) -> 'SingleOperatingPointAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingleOperatingPointAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self) -> 'float':
        """float: 'CurrentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_current(self) -> 'float':
        """float: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_frequency(self) -> 'float':
        """float: 'ElectricalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_period(self) -> 'float':
        """float: 'ElectricalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def mechanical_period(self) -> 'float':
        """float: 'MechanicalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_line_current(self) -> 'float':
        """float: 'PeakLineCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_current(self) -> 'float':
        """float: 'PeakPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_drms(self) -> 'float':
        """float: 'PhaseCurrentDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_qrms(self) -> 'float':
        """float: 'PhaseCurrentQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentQRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current(self) -> 'float':
        """float: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_phase_current(self) -> 'float':
        """float: 'RMSPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RMSPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def slot_passing_period(self) -> 'float':
        """float: 'SlotPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def time_step_increment(self) -> 'float':
        """float: 'TimeStepIncrement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeStepIncrement

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_results(self) -> '_1321.ElectricMachineResultsForOpenCircuitAndOnLoad':
        """ElectricMachineResultsForOpenCircuitAndOnLoad: 'ElectricMachineResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1347.ElectricMachineLoadCase':
        """ElectricMachineLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def slot_section_details_for_analysis(self) -> 'List[_1360.SlotDetailForAnalysis]':
        """List[SlotDetailForAnalysis]: 'SlotSectionDetailsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotSectionDetailsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis':
        return self._Cast_SingleOperatingPointAnalysis(self)
