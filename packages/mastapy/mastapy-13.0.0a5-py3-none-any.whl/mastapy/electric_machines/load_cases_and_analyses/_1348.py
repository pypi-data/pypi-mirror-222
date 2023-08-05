"""_1348.py

ElectricMachineLoadCaseBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE_BASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCaseBase')

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1367, _1341, _1349
    from mastapy.electric_machines import _1261


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCaseBase',)


class ElectricMachineLoadCaseBase(_0.APIBase):
    """ElectricMachineLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE_BASE

    class _Cast_ElectricMachineLoadCaseBase:
        """Special nested class for casting ElectricMachineLoadCaseBase to subclasses."""

        def __init__(self, parent: 'ElectricMachineLoadCaseBase'):
            self._parent = parent

        @property
        def dynamic_force_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1338
            
            return self._parent._cast(_1338.DynamicForceLoadCase)

        @property
        def efficiency_map_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1340
            
            return self._parent._cast(_1340.EfficiencyMapLoadCase)

        @property
        def electric_machine_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1347
            
            return self._parent._cast(_1347.ElectricMachineLoadCase)

        @property
        def electric_machine_mechanical_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1350
            
            return self._parent._cast(_1350.ElectricMachineMechanicalLoadCase)

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1356
            
            return self._parent._cast(_1356.NonLinearDQModelMultipleOperatingPointsLoadCase)

        @property
        def speed_torque_curve_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1364
            
            return self._parent._cast(_1364.SpeedTorqueCurveLoadCase)

        @property
        def speed_torque_load_case(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1365
            
            return self._parent._cast(_1365.SpeedTorqueLoadCase)

        @property
        def electric_machine_load_case_base(self) -> 'ElectricMachineLoadCaseBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCaseBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def folder_path(self) -> 'str':
        """str: 'FolderPath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FolderPath

        if temp is None:
            return ''

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value is not None else ''

    @property
    def temperatures(self) -> '_1367.Temperatures':
        """Temperatures: 'Temperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Temperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analyses(self) -> 'List[_1341.ElectricMachineAnalysis]':
        """List[ElectricMachineAnalysis]: 'Analyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Analyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def edit_folder_path(self):
        """ 'EditFolderPath' is the original name of this method."""

        self.wrapped.EditFolderPath()

    def analysis_for(self, setup: '_1261.ElectricMachineSetup') -> '_1341.ElectricMachineAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def copy_to(self, another_group: '_1349.ElectricMachineLoadCaseGroup') -> 'ElectricMachineLoadCaseBase':
        """ 'CopyTo' is the original name of this method.

        Args:
            another_group (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase
        """

        method_result = self.wrapped.CopyTo(another_group.wrapped if another_group else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_analysis(self, electric_machine_analysis: '_1341.ElectricMachineAnalysis'):
        """ 'RemoveAnalysis' is the original name of this method.

        Args:
            electric_machine_analysis (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis)
        """

        self.wrapped.RemoveAnalysis(electric_machine_analysis.wrapped if electric_machine_analysis else None)

    def remove_analysis_for(self, setup: '_1261.ElectricMachineSetup'):
        """ 'RemoveAnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """

        self.wrapped.RemoveAnalysisFor(setup.wrapped if setup else None)

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'ElectricMachineLoadCaseBase._Cast_ElectricMachineLoadCaseBase':
        return self._Cast_ElectricMachineLoadCaseBase(self)
