"""_1745.py

CustomReport
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.report import _1755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReport')

if TYPE_CHECKING:
    from mastapy.utility.report import (
        _1738, _1772, _1736, _1737
    )


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReport',)


class CustomReport(_1755.CustomReportItemContainer):
    """CustomReport

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT

    class _Cast_CustomReport:
        """Special nested class for casting CustomReport to subclasses."""

        def __init__(self, parent: 'CustomReport'):
            self._parent = parent

        @property
        def custom_report_item_container(self):
            return self._parent._cast(_1755.CustomReportItemContainer)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_report(self) -> 'CustomReport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_table_border_style(self) -> '_1738.CadTableBorderType':
        """CadTableBorderType: 'CADTableBorderStyle' is the original name of this property."""

        temp = self.wrapped.CADTableBorderStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Report.CadTableBorderType')
        return constructor.new_from_mastapy('mastapy.utility.report._1738', 'CadTableBorderType')(value) if value is not None else None

    @cad_table_border_style.setter
    def cad_table_border_style(self, value: '_1738.CadTableBorderType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Report.CadTableBorderType')
        self.wrapped.CADTableBorderStyle = value

    @property
    def font_height_for_cad_tables(self) -> 'float':
        """float: 'FontHeightForCADTables' is the original name of this property."""

        temp = self.wrapped.FontHeightForCADTables

        if temp is None:
            return 0.0

        return temp

    @font_height_for_cad_tables.setter
    def font_height_for_cad_tables(self, value: 'float'):
        self.wrapped.FontHeightForCADTables = float(value) if value is not None else 0.0

    @property
    def hide_cad_table_borders(self) -> 'bool':
        """bool: 'HideCADTableBorders' is the original name of this property."""

        temp = self.wrapped.HideCADTableBorders

        if temp is None:
            return False

        return temp

    @hide_cad_table_borders.setter
    def hide_cad_table_borders(self, value: 'bool'):
        self.wrapped.HideCADTableBorders = bool(value) if value is not None else False

    @property
    def include_report_check(self) -> '_1772.DefinitionBooleanCheckOptions':
        """DefinitionBooleanCheckOptions: 'IncludeReportCheck' is the original name of this property."""

        temp = self.wrapped.IncludeReportCheck

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Report.DefinitionBooleanCheckOptions')
        return constructor.new_from_mastapy('mastapy.utility.report._1772', 'DefinitionBooleanCheckOptions')(value) if value is not None else None

    @include_report_check.setter
    def include_report_check(self, value: '_1772.DefinitionBooleanCheckOptions'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Report.DefinitionBooleanCheckOptions')
        self.wrapped.IncludeReportCheck = value

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
    def page_height_for_cad_export(self) -> 'float':
        """float: 'PageHeightForCADExport' is the original name of this property."""

        temp = self.wrapped.PageHeightForCADExport

        if temp is None:
            return 0.0

        return temp

    @page_height_for_cad_export.setter
    def page_height_for_cad_export(self, value: 'float'):
        self.wrapped.PageHeightForCADExport = float(value) if value is not None else 0.0

    @property
    def page_orientation_for_cad_export(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation':
        """enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation: 'PageOrientationForCADExport' is the original name of this property."""

        temp = self.wrapped.PageOrientationForCADExport

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @page_orientation_for_cad_export.setter
    def page_orientation_for_cad_export(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CadPageOrientation.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PageOrientationForCADExport = value

    @property
    def page_size_for_cad_export(self) -> '_1737.CadPageSize':
        """CadPageSize: 'PageSizeForCADExport' is the original name of this property."""

        temp = self.wrapped.PageSizeForCADExport

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Report.CadPageSize')
        return constructor.new_from_mastapy('mastapy.utility.report._1737', 'CadPageSize')(value) if value is not None else None

    @page_size_for_cad_export.setter
    def page_size_for_cad_export(self, value: '_1737.CadPageSize'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Report.CadPageSize')
        self.wrapped.PageSizeForCADExport = value

    @property
    def page_width_for_cad_export(self) -> 'float':
        """float: 'PageWidthForCADExport' is the original name of this property."""

        temp = self.wrapped.PageWidthForCADExport

        if temp is None:
            return 0.0

        return temp

    @page_width_for_cad_export.setter
    def page_width_for_cad_export(self, value: 'float'):
        self.wrapped.PageWidthForCADExport = float(value) if value is not None else 0.0

    @property
    def show_table_of_contents(self) -> 'bool':
        """bool: 'ShowTableOfContents' is the original name of this property."""

        temp = self.wrapped.ShowTableOfContents

        if temp is None:
            return False

        return temp

    @show_table_of_contents.setter
    def show_table_of_contents(self, value: 'bool'):
        self.wrapped.ShowTableOfContents = bool(value) if value is not None else False

    @property
    def text_margin_for_cad_tables(self) -> 'float':
        """float: 'TextMarginForCADTables' is the original name of this property."""

        temp = self.wrapped.TextMarginForCADTables

        if temp is None:
            return 0.0

        return temp

    @text_margin_for_cad_tables.setter
    def text_margin_for_cad_tables(self, value: 'float'):
        self.wrapped.TextMarginForCADTables = float(value) if value is not None else 0.0

    @property
    def use_default_border(self) -> 'bool':
        """bool: 'UseDefaultBorder' is the original name of this property."""

        temp = self.wrapped.UseDefaultBorder

        if temp is None:
            return False

        return temp

    @use_default_border.setter
    def use_default_border(self, value: 'bool'):
        self.wrapped.UseDefaultBorder = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'CustomReport._Cast_CustomReport':
        return self._Cast_CustomReport(self)
