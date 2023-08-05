"""_1843.py

CustomTableAndChart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE_AND_CHART = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'CustomTableAndChart')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomTableAndChart',)


class CustomTableAndChart(_1771.CustomTable):
    """CustomTableAndChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE_AND_CHART

    class _Cast_CustomTableAndChart:
        """Special nested class for casting CustomTableAndChart to subclasses."""

        def __init__(self, parent: 'CustomTableAndChart'):
            self._parent = parent

        @property
        def custom_table(self):
            return self._parent._cast(_1771.CustomTable)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760, _1769
            
            return self._parent._cast(_1760.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1761
            
            return self._parent._cast(_1761.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1762
            
            return self._parent._cast(_1762.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1754
            
            return self._parent._cast(_1754.CustomReportItem)

        @property
        def custom_table_and_chart(self) -> 'CustomTableAndChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomTableAndChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomTableAndChart._Cast_CustomTableAndChart':
        return self._Cast_CustomTableAndChart(self)
