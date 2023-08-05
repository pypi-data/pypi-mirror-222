"""_1771.py

CustomTable
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1760, _1769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomTable')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomTable',)


class CustomTable(_1760.CustomReportMultiPropertyItem['_1769.CustomRow']):
    """CustomTable

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE

    class _Cast_CustomTable:
        """Special nested class for casting CustomTable to subclasses."""

        def __init__(self, parent: 'CustomTable'):
            self._parent = parent

        @property
        def custom_report_multi_property_item(self):
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
        def cylindrical_gear_table_with_mg_charts(self):
            from mastapy.gears.gear_designs.cylindrical import _1031
            
            return self._parent._cast(_1031.CylindricalGearTableWithMGCharts)

        @property
        def custom_table_and_chart(self):
            from mastapy.utility_gui.charts import _1843
            
            return self._parent._cast(_1843.CustomTableAndChart)

        @property
        def custom_table(self) -> 'CustomTable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomTable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self) -> 'bool':
        """bool: 'IsMainReportItem' is the original name of this property."""

        temp = self.wrapped.IsMainReportItem

        if temp is None:
            return False

        return temp

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'CustomTable._Cast_CustomTable':
        return self._Cast_CustomTable(self)
