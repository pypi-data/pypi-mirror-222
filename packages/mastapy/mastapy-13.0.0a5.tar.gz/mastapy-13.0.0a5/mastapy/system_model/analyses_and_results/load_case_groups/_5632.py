﻿"""_5632.py

AbstractLoadCaseGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'AbstractLoadCaseGroup')

if TYPE_CHECKING:
    from mastapy.system_model import _2187
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4367
    from mastapy.system_model.analyses_and_results.static_loads import _6916, _6771
    from mastapy import _7525


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractLoadCaseGroup',)


class AbstractLoadCaseGroup(_0.APIBase):
    """AbstractLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_LOAD_CASE_GROUP

    class _Cast_AbstractLoadCaseGroup:
        """Special nested class for casting AbstractLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'AbstractLoadCaseGroup'):
            self._parent = parent

        @property
        def abstract_design_state_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5631
            
            return self._parent._cast(_5631.AbstractDesignStateLoadCaseGroup)

        @property
        def abstract_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5633
            
            return self._parent._cast(_5633.AbstractStaticLoadCaseGroup)

        @property
        def design_state(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5636
            
            return self._parent._cast(_5636.DesignState)

        @property
        def duty_cycle(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5637
            
            return self._parent._cast(_5637.DutyCycle)

        @property
        def sub_group_in_single_design_state(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5640
            
            return self._parent._cast(_5640.SubGroupInSingleDesignState)

        @property
        def time_series_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5644
            
            return self._parent._cast(_5644.TimeSeriesLoadCaseGroup)

        @property
        def abstract_load_case_group(self) -> 'AbstractLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def number_of_load_cases(self) -> 'float':
        """float: 'NumberOfLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfLoadCases

        if temp is None:
            return 0.0

        return temp

    @property
    def total_duration(self) -> 'float':
        """float: 'TotalDuration' is the original name of this property."""

        temp = self.wrapped.TotalDuration

        if temp is None:
            return 0.0

        return temp

    @total_duration.setter
    def total_duration(self, value: 'float'):
        self.wrapped.TotalDuration = float(value) if value is not None else 0.0

    @property
    def model(self) -> '_2187.Design':
        """Design: 'Model' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Model

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_analysis_options(self) -> '_4367.ParametricStudyToolOptions':
        """ParametricStudyToolOptions: 'ParametricAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case_root_assemblies(self) -> 'List[_6916.RootAssemblyLoadCase]':
        """List[RootAssemblyLoadCase]: 'LoadCaseRootAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseRootAssemblies

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

    def create_load_cases(self, number_of_load_cases: 'int', token: '_7525.TaskProgress') -> 'List[_6771.LoadCase]':
        """ 'CreateLoadCases' is the original name of this method.

        Args:
            number_of_load_cases (int)
            token (mastapy.TaskProgress)

        Returns:
            List[mastapy.system_model.analyses_and_results.static_loads.LoadCase]
        """

        number_of_load_cases = int(number_of_load_cases)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.CreateLoadCases(number_of_load_cases if number_of_load_cases else 0, token.wrapped if token else None))

    def perform_pst(self):
        """ 'PerformPst' is the original name of this method."""

        self.wrapped.PerformPst()

    def perform_pst_with_progress(self, progress: '_7525.TaskProgress'):
        """ 'PerformPstWithProgress' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)
        """

        self.wrapped.PerformPstWithProgress(progress.wrapped if progress else None)

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
    def cast_to(self) -> 'AbstractLoadCaseGroup._Cast_AbstractLoadCaseGroup':
        return self._Cast_AbstractLoadCaseGroup(self)
