"""_5815.py

ExcitationSourceSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_SOURCE_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results', 'ExcitationSourceSelection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5818
    from mastapy.math_utility import _1519


__docformat__ = 'restructuredtext en'
__all__ = ('ExcitationSourceSelection',)


class ExcitationSourceSelection(_5816.ExcitationSourceSelectionBase):
    """ExcitationSourceSelection

    This is a mastapy class.
    """

    TYPE = _EXCITATION_SOURCE_SELECTION

    class _Cast_ExcitationSourceSelection:
        """Special nested class for casting ExcitationSourceSelection to subclasses."""

        def __init__(self, parent: 'ExcitationSourceSelection'):
            self._parent = parent

        @property
        def excitation_source_selection_base(self):
            return self._parent._cast(_5816.ExcitationSourceSelectionBase)

        @property
        def excitation_source_selection(self) -> 'ExcitationSourceSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExcitationSourceSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_selections(self) -> 'List[_5818.HarmonicSelection]':
        """List[HarmonicSelection]: 'HarmonicSelections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicSelections

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

    def invert_is_included_in_excitations_selection(self):
        """ 'InvertIsIncludedInExcitationsSelection' is the original name of this method."""

        self.wrapped.InvertIsIncludedInExcitationsSelection()

    def invert_is_shown_selection(self):
        """ 'InvertIsShownSelection' is the original name of this method."""

        self.wrapped.InvertIsShownSelection()

    def include_only_harmonic_with_order(self, order: '_1519.RoundedOrder') -> 'bool':
        """ 'IncludeOnlyHarmonicWithOrder' is the original name of this method.

        Args:
            order (mastapy.math_utility.RoundedOrder)

        Returns:
            bool
        """

        method_result = self.wrapped.IncludeOnlyHarmonicWithOrder(order.wrapped if order else None)
        return method_result

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
    def cast_to(self) -> 'ExcitationSourceSelection._Cast_ExcitationSourceSelection':
        return self._Cast_ExcitationSourceSelection(self)
