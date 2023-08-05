﻿"""_1283.py

Phase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PHASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'Phase')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1854
    from mastapy.math_utility import _1503


__docformat__ = 'restructuredtext en'
__all__ = ('Phase',)


class Phase(_0.APIBase):
    """Phase

    This is a mastapy class.
    """

    TYPE = _PHASE

    class _Cast_Phase:
        """Special nested class for casting Phase to subclasses."""

        def __init__(self, parent: 'Phase'):
            self._parent = parent

        @property
        def phase(self) -> 'Phase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Phase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mmf(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'MMF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMF

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def phase_index(self) -> 'int':
        """int: 'PhaseIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseIndex

        if temp is None:
            return 0

        return temp

    @property
    def mmf_fourier_series_electrical(self) -> '_1503.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesElectrical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesElectrical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mmf_fourier_series_mechanical(self) -> '_1503.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesMechanical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesMechanical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_factor_harmonics_electrical(self) -> '_1503.FourierSeries':
        """FourierSeries: 'WindingFactorHarmonicsElectrical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingFactorHarmonicsElectrical

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_factor_harmonics_mechanical(self) -> '_1503.FourierSeries':
        """FourierSeries: 'WindingFactorHarmonicsMechanical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingFactorHarmonicsMechanical

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
    def cast_to(self) -> 'Phase._Cast_Phase':
        return self._Cast_Phase(self)
