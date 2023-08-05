﻿"""_904.py

DesignSpaceSearchCandidateBase
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_SPACE_SEARCH_CANDIDATE_BASE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'DesignSpaceSearchCandidateBase')

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1213


__docformat__ = 'restructuredtext en'
__all__ = ('DesignSpaceSearchCandidateBase',)


TAnalysis = TypeVar('TAnalysis', bound='_1213.AbstractGearSetAnalysis')
TCandidate = TypeVar('TCandidate', bound='DesignSpaceSearchCandidateBase')


class DesignSpaceSearchCandidateBase(_0.APIBase, Generic[TAnalysis, TCandidate]):
    """DesignSpaceSearchCandidateBase

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _DESIGN_SPACE_SEARCH_CANDIDATE_BASE

    class _Cast_DesignSpaceSearchCandidateBase:
        """Special nested class for casting DesignSpaceSearchCandidateBase to subclasses."""

        def __init__(self, parent: 'DesignSpaceSearchCandidateBase'):
            self._parent = parent

        @property
        def gear_set_optimiser_candidate(self):
            from mastapy.gears.gear_set_pareto_optimiser import _908
            
            return self._parent._cast(_908.GearSetOptimiserCandidate)

        @property
        def micro_geometry_design_space_search_candidate(self):
            from mastapy.gears.gear_set_pareto_optimiser import _914
            
            return self._parent._cast(_914.MicroGeometryDesignSpaceSearchCandidate)

        @property
        def design_space_search_candidate_base(self) -> 'DesignSpaceSearchCandidateBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignSpaceSearchCandidateBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_name(self) -> 'str':
        """str: 'DesignName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignName

        if temp is None:
            return ''

        return temp

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

    def select_candidate(self):
        """ 'SelectCandidate' is the original name of this method."""

        self.wrapped.SelectCandidate()

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
    def cast_to(self) -> 'DesignSpaceSearchCandidateBase._Cast_DesignSpaceSearchCandidateBase':
        return self._Cast_DesignSpaceSearchCandidateBase(self)
