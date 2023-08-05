"""_1755.py

CustomReportItemContainer
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1754
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainer')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainer',)


class CustomReportItemContainer(_1754.CustomReportItem):
    """CustomReportItemContainer

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER

    class _Cast_CustomReportItemContainer:
        """Special nested class for casting CustomReportItemContainer to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainer'):
            self._parent = parent

        @property
        def custom_report_item(self):
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_report(self):
            from mastapy.utility.report import _1745
            
            return self._parent._cast(_1745.CustomReport)

        @property
        def custom_report_column(self):
            from mastapy.utility.report import _1749
            
            return self._parent._cast(_1749.CustomReportColumn)

        @property
        def custom_report_item_container_collection_item(self):
            from mastapy.utility.report import _1758
            
            return self._parent._cast(_1758.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_tab(self):
            from mastapy.utility.report import _1766
            
            return self._parent._cast(_1766.CustomReportTab)

        @property
        def custom_report_item_container(self) -> 'CustomReportItemContainer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainer._Cast_CustomReportItemContainer':
        return self._Cast_CustomReportItemContainer(self)
