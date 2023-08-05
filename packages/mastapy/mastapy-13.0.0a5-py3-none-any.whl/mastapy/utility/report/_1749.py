"""_1749.py

CustomReportColumn
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1758
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_COLUMN = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportColumn')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportColumn',)


class CustomReportColumn(_1758.CustomReportItemContainerCollectionItem):
    """CustomReportColumn

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_COLUMN

    class _Cast_CustomReportColumn:
        """Special nested class for casting CustomReportColumn to subclasses."""

        def __init__(self, parent: 'CustomReportColumn'):
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
        def custom_report_column(self) -> 'CustomReportColumn':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportColumn.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auto_width(self) -> 'bool':
        """bool: 'AutoWidth' is the original name of this property."""

        temp = self.wrapped.AutoWidth

        if temp is None:
            return False

        return temp

    @auto_width.setter
    def auto_width(self, value: 'bool'):
        self.wrapped.AutoWidth = bool(value) if value is not None else False

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'CustomReportColumn._Cast_CustomReportColumn':
        return self._Cast_CustomReportColumn(self)
