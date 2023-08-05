"""_1765.py

CustomReportStatusItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1751
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_STATUS_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportStatusItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportStatusItem',)


class CustomReportStatusItem(_1751.CustomReportDefinitionItem):
    """CustomReportStatusItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_STATUS_ITEM

    class _Cast_CustomReportStatusItem:
        """Special nested class for casting CustomReportStatusItem to subclasses."""

        def __init__(self, parent: 'CustomReportStatusItem'):
            self._parent = parent

        @property
        def custom_report_definition_item(self):
            return self._parent._cast(_1751.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_report_status_item(self) -> 'CustomReportStatusItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportStatusItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportStatusItem._Cast_CustomReportStatusItem':
        return self._Cast_CustomReportStatusItem(self)
