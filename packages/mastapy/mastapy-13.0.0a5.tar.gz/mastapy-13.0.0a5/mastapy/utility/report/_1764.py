"""_1764.py

CustomReportPropertyItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_PROPERTY_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportPropertyItem')

if TYPE_CHECKING:
    from mastapy.utility.report import _1774, _1775
    from mastapy.utility.reporting_property_framework import _1779


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportPropertyItem',)


class CustomReportPropertyItem(_0.APIBase):
    """CustomReportPropertyItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_PROPERTY_ITEM

    class _Cast_CustomReportPropertyItem:
        """Special nested class for casting CustomReportPropertyItem to subclasses."""

        def __init__(self, parent: 'CustomReportPropertyItem'):
            self._parent = parent

        @property
        def blank_row(self):
            from mastapy.utility.report import _1735
            
            return self._parent._cast(_1735.BlankRow)

        @property
        def custom_report_chart_item(self):
            from mastapy.utility.report import _1748
            
            return self._parent._cast(_1748.CustomReportChartItem)

        @property
        def custom_row(self):
            from mastapy.utility.report import _1769
            
            return self._parent._cast(_1769.CustomRow)

        @property
        def user_text_row(self):
            from mastapy.utility.report import _1778
            
            return self._parent._cast(_1778.UserTextRow)

        @property
        def custom_report_property_item(self) -> 'CustomReportPropertyItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportPropertyItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def font_style(self) -> '_1774.FontStyle':
        """FontStyle: 'FontStyle' is the original name of this property."""

        temp = self.wrapped.FontStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Report.FontStyle')
        return constructor.new_from_mastapy('mastapy.utility.report._1774', 'FontStyle')(value) if value is not None else None

    @font_style.setter
    def font_style(self, value: '_1774.FontStyle'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Report.FontStyle')
        self.wrapped.FontStyle = value

    @property
    def font_weight(self) -> '_1775.FontWeight':
        """FontWeight: 'FontWeight' is the original name of this property."""

        temp = self.wrapped.FontWeight

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Report.FontWeight')
        return constructor.new_from_mastapy('mastapy.utility.report._1775', 'FontWeight')(value) if value is not None else None

    @font_weight.setter
    def font_weight(self, value: '_1775.FontWeight'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Report.FontWeight')
        self.wrapped.FontWeight = value

    @property
    def horizontal_position(self) -> '_1779.CellValuePosition':
        """CellValuePosition: 'HorizontalPosition' is the original name of this property."""

        temp = self.wrapped.HorizontalPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.ReportingPropertyFramework.CellValuePosition')
        return constructor.new_from_mastapy('mastapy.utility.reporting_property_framework._1779', 'CellValuePosition')(value) if value is not None else None

    @horizontal_position.setter
    def horizontal_position(self, value: '_1779.CellValuePosition'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.ReportingPropertyFramework.CellValuePosition')
        self.wrapped.HorizontalPosition = value

    @property
    def show_property_name(self) -> 'bool':
        """bool: 'ShowPropertyName' is the original name of this property."""

        temp = self.wrapped.ShowPropertyName

        if temp is None:
            return False

        return temp

    @show_property_name.setter
    def show_property_name(self, value: 'bool'):
        self.wrapped.ShowPropertyName = bool(value) if value is not None else False

    def add_condition(self):
        """ 'AddCondition' is the original name of this method."""

        self.wrapped.AddCondition()

    @property
    def cast_to(self) -> 'CustomReportPropertyItem._Cast_CustomReportPropertyItem':
        return self._Cast_CustomReportPropertyItem(self)
