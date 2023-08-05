﻿"""_1028.py

CylindricalGearSetManufacturingConfigurationSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MANUFACTURING_CONFIGURATION_SELECTION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearSetManufacturingConfigurationSelection')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _622


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetManufacturingConfigurationSelection',)


class CylindricalGearSetManufacturingConfigurationSelection(_0.APIBase):
    """CylindricalGearSetManufacturingConfigurationSelection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MANUFACTURING_CONFIGURATION_SELECTION

    class _Cast_CylindricalGearSetManufacturingConfigurationSelection:
        """Special nested class for casting CylindricalGearSetManufacturingConfigurationSelection to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetManufacturingConfigurationSelection'):
            self._parent = parent

        @property
        def cylindrical_gear_set_manufacturing_configuration_selection(self) -> 'CylindricalGearSetManufacturingConfigurationSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetManufacturingConfigurationSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig':
        """list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property."""

        temp = self.wrapped.ManufacturingConfiguration

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_CylindricalSetManufacturingConfig')(temp) if temp is not None else None

    @manufacturing_configuration.setter
    def manufacturing_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalSetManufacturingConfig.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ManufacturingConfiguration = value

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
    def cast_to(self) -> 'CylindricalGearSetManufacturingConfigurationSelection._Cast_CylindricalGearSetManufacturingConfigurationSelection':
        return self._Cast_CylindricalGearSetManufacturingConfigurationSelection(self)
