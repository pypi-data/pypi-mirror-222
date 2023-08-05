"""_2246.py

ModalContributionViewOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_CONTRIBUTION_VIEW_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.Drawing.Options', 'ModalContributionViewOptions')

if TYPE_CHECKING:
    from mastapy.math_utility import _1479
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5820, _5819
    from mastapy.utility import _1579


__docformat__ = 'restructuredtext en'
__all__ = ('ModalContributionViewOptions',)


class ModalContributionViewOptions(_0.APIBase):
    """ModalContributionViewOptions

    This is a mastapy class.
    """

    TYPE = _MODAL_CONTRIBUTION_VIEW_OPTIONS

    class _Cast_ModalContributionViewOptions:
        """Special nested class for casting ModalContributionViewOptions to subclasses."""

        def __init__(self, parent: 'ModalContributionViewOptions'):
            self._parent = parent

        @property
        def modal_contribution_view_options(self) -> 'ModalContributionViewOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalContributionViewOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def filtering_frequency(self) -> 'float':
        """float: 'FilteringFrequency' is the original name of this property."""

        temp = self.wrapped.FilteringFrequency

        if temp is None:
            return 0.0

        return temp

    @filtering_frequency.setter
    def filtering_frequency(self, value: 'float'):
        self.wrapped.FilteringFrequency = float(value) if value is not None else 0.0

    @property
    def filtering_frequency_range(self) -> '_1479.Range':
        """Range: 'FilteringFrequencyRange' is the original name of this property."""

        temp = self.wrapped.FilteringFrequencyRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @filtering_frequency_range.setter
    def filtering_frequency_range(self, value: '_1479.Range'):
        self.wrapped.FilteringFrequencyRange = value

    @property
    def filtering_method(self) -> '_5820.ModalContributionFilteringMethod':
        """ModalContributionFilteringMethod: 'FilteringMethod' is the original name of this property."""

        temp = self.wrapped.FilteringMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionFilteringMethod')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.harmonic_analyses.results._5820', 'ModalContributionFilteringMethod')(value) if value is not None else None

    @filtering_method.setter
    def filtering_method(self, value: '_5820.ModalContributionFilteringMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionFilteringMethod')
        self.wrapped.FilteringMethod = value

    @property
    def frequency_range(self) -> '_1479.Range':
        """Range: 'FrequencyRange' is the original name of this property."""

        temp = self.wrapped.FrequencyRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @frequency_range.setter
    def frequency_range(self, value: '_1479.Range'):
        self.wrapped.FrequencyRange = value

    @property
    def index(self) -> 'int':
        """int: 'Index' is the original name of this property."""

        temp = self.wrapped.Index

        if temp is None:
            return 0

        return temp

    @index.setter
    def index(self, value: 'int'):
        self.wrapped.Index = int(value) if value is not None else 0

    @property
    def index_range(self) -> '_1579.IntegerRange':
        """IntegerRange: 'IndexRange' is the original name of this property."""

        temp = self.wrapped.IndexRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @index_range.setter
    def index_range(self, value: '_1579.IntegerRange'):
        self.wrapped.IndexRange = value

    @property
    def modes_to_display(self) -> '_5819.ModalContributionDisplayMethod':
        """ModalContributionDisplayMethod: 'ModesToDisplay' is the original name of this property."""

        temp = self.wrapped.ModesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionDisplayMethod')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.harmonic_analyses.results._5819', 'ModalContributionDisplayMethod')(value) if value is not None else None

    @modes_to_display.setter
    def modes_to_display(self, value: '_5819.ModalContributionDisplayMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ModalContributionDisplayMethod')
        self.wrapped.ModesToDisplay = value

    @property
    def percentage_of_total_response(self) -> 'float':
        """float: 'PercentageOfTotalResponse' is the original name of this property."""

        temp = self.wrapped.PercentageOfTotalResponse

        if temp is None:
            return 0.0

        return temp

    @percentage_of_total_response.setter
    def percentage_of_total_response(self, value: 'float'):
        self.wrapped.PercentageOfTotalResponse = float(value) if value is not None else 0.0

    @property
    def show_modal_contribution(self) -> 'bool':
        """bool: 'ShowModalContribution' is the original name of this property."""

        temp = self.wrapped.ShowModalContribution

        if temp is None:
            return False

        return temp

    @show_modal_contribution.setter
    def show_modal_contribution(self, value: 'bool'):
        self.wrapped.ShowModalContribution = bool(value) if value is not None else False

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
    def cast_to(self) -> 'ModalContributionViewOptions._Cast_ModalContributionViewOptions':
        return self._Cast_ModalContributionViewOptions(self)
