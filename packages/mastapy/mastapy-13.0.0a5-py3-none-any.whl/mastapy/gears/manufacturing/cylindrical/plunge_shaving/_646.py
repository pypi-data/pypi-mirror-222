﻿"""_646.py

PlungeShaverGeneration
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_GENERATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'PlungeShaverGeneration')

if TYPE_CHECKING:
    from mastapy.math_utility import _1479
    from mastapy.gears.gear_designs.cylindrical import _1001
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _639, _653


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShaverGeneration',)


class PlungeShaverGeneration(_0.APIBase):
    """PlungeShaverGeneration

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_GENERATION

    class _Cast_PlungeShaverGeneration:
        """Special nested class for casting PlungeShaverGeneration to subclasses."""

        def __init__(self, parent: 'PlungeShaverGeneration'):
            self._parent = parent

        @property
        def plunge_shaver_generation(self) -> 'PlungeShaverGeneration':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlungeShaverGeneration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_conjugate_face_width(self) -> '_1479.Range':
        """Range: 'CalculatedConjugateFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedConjugateFaceWidth

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_start_of_active_profile_diameter(self) -> 'float':
        """float: 'GearStartOfActiveProfileDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_end_of_active_profile_diameter(self) -> 'float':
        """float: 'ManufacturedEndOfActiveProfileDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturedEndOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_start_of_active_profile_diameter(self) -> 'float':
        """float: 'ManufacturedStartOfActiveProfileDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturedStartOfActiveProfileDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_angle_unsigned(self) -> 'float':
        """float: 'ShaftAngleUnsigned' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftAngleUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def crossed_axis_calculation_details(self) -> '_1001.CrossedAxisCylindricalGearPairLineContact':
        """CrossedAxisCylindricalGearPairLineContact: 'CrossedAxisCalculationDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrossedAxisCalculationDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculation_errors(self) -> 'List[_639.CalculationError]':
        """List[CalculationError]: 'CalculationErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculationErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def points_of_interest_on_the_shaver(self) -> 'List[_653.ShaverPointOfInterest]':
        """List[ShaverPointOfInterest]: 'PointsOfInterestOnTheShaver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointsOfInterestOnTheShaver

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
    def cast_to(self) -> 'PlungeShaverGeneration._Cast_PlungeShaverGeneration':
        return self._Cast_PlungeShaverGeneration(self)
