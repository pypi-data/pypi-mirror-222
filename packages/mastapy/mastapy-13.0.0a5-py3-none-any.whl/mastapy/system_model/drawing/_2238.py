﻿"""_2238.py

RotorDynamicsViewable
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_DYNAMICS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'RotorDynamicsViewable')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.rotor_dynamics import _4006


__docformat__ = 'restructuredtext en'
__all__ = ('RotorDynamicsViewable',)


class RotorDynamicsViewable(_0.APIBase):
    """RotorDynamicsViewable

    This is a mastapy class.
    """

    TYPE = _ROTOR_DYNAMICS_VIEWABLE

    class _Cast_RotorDynamicsViewable:
        """Special nested class for casting RotorDynamicsViewable to subclasses."""

        def __init__(self, parent: 'RotorDynamicsViewable'):
            self._parent = parent

        @property
        def critical_speed_analysis_viewable(self):
            from mastapy.system_model.drawing import _2230
            
            return self._parent._cast(_2230.CriticalSpeedAnalysisViewable)

        @property
        def stability_analysis_viewable(self):
            from mastapy.system_model.drawing import _2240
            
            return self._parent._cast(_2240.StabilityAnalysisViewable)

        @property
        def steady_state_synchronous_response_viewable(self):
            from mastapy.system_model.drawing import _2241
            
            return self._parent._cast(_2241.SteadyStateSynchronousResponseViewable)

        @property
        def rotor_dynamics_viewable(self) -> 'RotorDynamicsViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotorDynamicsViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_dynamics(self) -> '_4006.RotorDynamicsDrawStyle':
        """RotorDynamicsDrawStyle: 'RotorDynamics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorDynamics

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
    def cast_to(self) -> 'RotorDynamicsViewable._Cast_RotorDynamicsViewable':
        return self._Cast_RotorDynamicsViewable(self)
