﻿"""_246.py

BHCurveSpecification
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BH_CURVE_SPECIFICATION = python_net_import('SMT.MastaAPI.Materials', 'BHCurveSpecification')

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.utility_gui.charts import _1854
    from mastapy.materials import _245


__docformat__ = 'restructuredtext en'
__all__ = ('BHCurveSpecification',)


class BHCurveSpecification(_0.APIBase):
    """BHCurveSpecification

    This is a mastapy class.
    """

    TYPE = _BH_CURVE_SPECIFICATION

    class _Cast_BHCurveSpecification:
        """Special nested class for casting BHCurveSpecification to subclasses."""

        def __init__(self, parent: 'BHCurveSpecification'):
            self._parent = parent

        @property
        def bh_curve_specification(self) -> 'BHCurveSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BHCurveSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bh_curve(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'BHCurve' is the original name of this property."""

        temp = self.wrapped.BHCurve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @bh_curve.setter
    def bh_curve(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.BHCurve = value

    @property
    def bh_curve_plot(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'BHCurvePlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BHCurvePlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bh_curve_extrapolation_method(self) -> '_245.BHCurveExtrapolationMethod':
        """BHCurveExtrapolationMethod: 'BHCurveExtrapolationMethod' is the original name of this property."""

        temp = self.wrapped.BHCurveExtrapolationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.BHCurveExtrapolationMethod')
        return constructor.new_from_mastapy('mastapy.materials._245', 'BHCurveExtrapolationMethod')(value) if value is not None else None

    @bh_curve_extrapolation_method.setter
    def bh_curve_extrapolation_method(self, value: '_245.BHCurveExtrapolationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.BHCurveExtrapolationMethod')
        self.wrapped.BHCurveExtrapolationMethod = value

    @property
    def maximum_h_for_bh_curve_extrapolation(self) -> 'float':
        """float: 'MaximumHForBHCurveExtrapolation' is the original name of this property."""

        temp = self.wrapped.MaximumHForBHCurveExtrapolation

        if temp is None:
            return 0.0

        return temp

    @maximum_h_for_bh_curve_extrapolation.setter
    def maximum_h_for_bh_curve_extrapolation(self, value: 'float'):
        self.wrapped.MaximumHForBHCurveExtrapolation = float(value) if value is not None else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def number_of_points_for_bh_curve_extrapolation(self) -> 'int':
        """int: 'NumberOfPointsForBHCurveExtrapolation' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForBHCurveExtrapolation

        if temp is None:
            return 0

        return temp

    @number_of_points_for_bh_curve_extrapolation.setter
    def number_of_points_for_bh_curve_extrapolation(self, value: 'int'):
        self.wrapped.NumberOfPointsForBHCurveExtrapolation = int(value) if value is not None else 0

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
    def cast_to(self) -> 'BHCurveSpecification._Cast_BHCurveSpecification':
        return self._Cast_BHCurveSpecification(self)
