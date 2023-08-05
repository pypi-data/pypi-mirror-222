﻿"""_5734.py

HarmonicAnalysisExportOptions
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_EXPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisExportOptions')

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1601
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717, _5736
    from mastapy.system_model.analyses_and_results.modal_analyses import _4604
    from mastapy.system_model.part_model import _2451


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisExportOptions',)


TPartAnalysis = TypeVar('TPartAnalysis')
TPart = TypeVar('TPart', bound='_2451.Part')


class HarmonicAnalysisExportOptions(_0.APIBase, Generic[TPartAnalysis, TPart]):
    """HarmonicAnalysisExportOptions

    This is a mastapy class.

    Generic Types:
        TPartAnalysis
        TPart
    """

    TYPE = _HARMONIC_ANALYSIS_EXPORT_OPTIONS

    class _Cast_HarmonicAnalysisExportOptions:
        """Special nested class for casting HarmonicAnalysisExportOptions to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisExportOptions'):
            self._parent = parent

        @property
        def harmonic_analysis_fe_export_options(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5735
            
            return self._parent._cast(_5735.HarmonicAnalysisFEExportOptions)

        @property
        def harmonic_analysis_root_assembly_export_options(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5737
            
            return self._parent._cast(_5737.HarmonicAnalysisRootAssemblyExportOptions)

        @property
        def harmonic_analysis_shaft_export_options(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
            
            return self._parent._cast(_5738.HarmonicAnalysisShaftExportOptions)

        @property
        def harmonic_analysis_export_options(self) -> 'HarmonicAnalysisExportOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisExportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_units_for_export(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        """list_with_selected_item.ListWithSelectedItem_Unit: 'DistanceUnitsForExport' is the original name of this property."""

        temp = self.wrapped.DistanceUnitsForExport

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_Unit')(temp) if temp is not None else None

    @distance_units_for_export.setter
    def distance_units_for_export(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.DistanceUnitsForExport = value

    @property
    def export_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ExportOutputType':
        """enum_with_selected_value.EnumWithSelectedValue_ExportOutputType: 'ExportType' is the original name of this property."""

        temp = self.wrapped.ExportType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ExportOutputType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @export_type.setter
    def export_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ExportOutputType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ExportOutputType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExportType = value

    @property
    def planetary_duplicate_to_export(self) -> 'list_with_selected_item.ListWithSelectedItem_TPartAnalysis':
        """list_with_selected_item.ListWithSelectedItem_TPartAnalysis: 'PlanetaryDuplicateToExport' is the original name of this property."""

        temp = self.wrapped.PlanetaryDuplicateToExport

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_TPartAnalysis')(temp) if temp is not None else None

    @planetary_duplicate_to_export.setter
    def planetary_duplicate_to_export(self, value: 'list_with_selected_item.ListWithSelectedItem_TPartAnalysis.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_TPartAnalysis.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_TPartAnalysis.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.PlanetaryDuplicateToExport = value

    @property
    def status_message_for_export(self) -> 'str':
        """str: 'StatusMessageForExport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatusMessageForExport

        if temp is None:
            return ''

        return temp

    @property
    def type_of_result_to_export(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType':
        """enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType: 'TypeOfResultToExport' is the original name of this property."""

        temp = self.wrapped.TypeOfResultToExport

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @type_of_result_to_export.setter
    def type_of_result_to_export(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TypeOfResultToExport = value

    @property
    def analysis_options(self) -> '_5736.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'AnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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

    def export_results(self):
        """ 'ExportResults' is the original name of this method."""

        self.wrapped.ExportResults()

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
    def cast_to(self) -> 'HarmonicAnalysisExportOptions._Cast_HarmonicAnalysisExportOptions':
        return self._Cast_HarmonicAnalysisExportOptions(self)
