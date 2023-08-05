"""_1758.py

CustomReportItemContainerCollectionItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainerCollectionItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainerCollectionItem',)


class CustomReportItemContainerCollectionItem(_1755.CustomReportItemContainer):
    """CustomReportItemContainerCollectionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_ITEM

    class _Cast_CustomReportItemContainerCollectionItem:
        """Special nested class for casting CustomReportItemContainerCollectionItem to subclasses."""

        def __init__(self, parent: 'CustomReportItemContainerCollectionItem'):
            self._parent = parent

        @property
        def custom_report_item_container(self):
            return self._parent._cast(_1755.CustomReportItemContainer)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_report_column(self):
            from mastapy.utility.report import _1749
            
            return self._parent._cast(_1749.CustomReportColumn)

        @property
        def custom_report_tab(self):
            from mastapy.utility.report import _1766
            
            return self._parent._cast(_1766.CustomReportTab)

        @property
        def custom_report_item_container_collection_item(self) -> 'CustomReportItemContainerCollectionItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItemContainerCollectionItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportItemContainerCollectionItem._Cast_CustomReportItemContainerCollectionItem':
        return self._Cast_CustomReportItemContainerCollectionItem(self)
