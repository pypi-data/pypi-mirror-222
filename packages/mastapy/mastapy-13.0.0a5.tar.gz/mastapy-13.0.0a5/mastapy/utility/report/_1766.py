"""_1766.py

CustomReportTab
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1758
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TAB = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportTab')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportTab',)


class CustomReportTab(_1758.CustomReportItemContainerCollectionItem):
    """CustomReportTab

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TAB

    class _Cast_CustomReportTab:
        """Special nested class for casting CustomReportTab to subclasses."""

        def __init__(self, parent: 'CustomReportTab'):
            self._parent = parent

        @property
        def custom_report_item_container_collection_item(self):
            return self._parent._cast(_1758.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_item_container(self):
            from mastapy.utility.report import _1755
            
            return self._parent._cast(_1755.CustomReportItemContainer)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_report_tab(self) -> 'CustomReportTab':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportTab.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hide_when_has_no_content(self) -> 'bool':
        """bool: 'HideWhenHasNoContent' is the original name of this property."""

        temp = self.wrapped.HideWhenHasNoContent

        if temp is None:
            return False

        return temp

    @hide_when_has_no_content.setter
    def hide_when_has_no_content(self, value: 'bool'):
        self.wrapped.HideWhenHasNoContent = bool(value) if value is not None else False

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value is not None else ''

    @property
    def cast_to(self) -> 'CustomReportTab._Cast_CustomReportTab':
        return self._Cast_CustomReportTab(self)
