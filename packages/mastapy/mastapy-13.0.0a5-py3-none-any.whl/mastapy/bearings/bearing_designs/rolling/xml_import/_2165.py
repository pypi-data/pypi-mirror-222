﻿"""_2165.py

RollingBearingImporter
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_IMPORTER = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport', 'RollingBearingImporter')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling.xml_import import _2166


__docformat__ = 'restructuredtext en'
__all__ = ('RollingBearingImporter',)


class RollingBearingImporter(_0.APIBase):
    """RollingBearingImporter

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_IMPORTER

    class _Cast_RollingBearingImporter:
        """Special nested class for casting RollingBearingImporter to subclasses."""

        def __init__(self, parent: 'RollingBearingImporter'):
            self._parent = parent

        @property
        def rolling_bearing_importer(self) -> 'RollingBearingImporter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingBearingImporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_bearings_ready_to_import(self) -> 'int':
        """int: 'NumberOfBearingsReadyToImport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfBearingsReadyToImport

        if temp is None:
            return 0

        return temp

    @property
    def replace_existing_bearings(self) -> 'bool':
        """bool: 'ReplaceExistingBearings' is the original name of this property."""

        temp = self.wrapped.ReplaceExistingBearings

        if temp is None:
            return False

        return temp

    @replace_existing_bearings.setter
    def replace_existing_bearings(self, value: 'bool'):
        self.wrapped.ReplaceExistingBearings = bool(value) if value is not None else False

    @property
    def mappings(self) -> 'List[_2166.XmlBearingTypeMapping]':
        """List[XmlBearingTypeMapping]: 'Mappings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mappings

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

    def import_all(self):
        """ 'ImportAll' is the original name of this method."""

        self.wrapped.ImportAll()

    def load_setup(self):
        """ 'LoadSetup' is the original name of this method."""

        self.wrapped.LoadSetup()

    def open_files_in_directory(self):
        """ 'OpenFilesInDirectory' is the original name of this method."""

        self.wrapped.OpenFilesInDirectory()

    def reset_to_defaults(self):
        """ 'ResetToDefaults' is the original name of this method."""

        self.wrapped.ResetToDefaults()

    def save_setup(self):
        """ 'SaveSetup' is the original name of this method."""

        self.wrapped.SaveSetup()

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
    def cast_to(self) -> 'RollingBearingImporter._Cast_RollingBearingImporter':
        return self._Cast_RollingBearingImporter(self)
