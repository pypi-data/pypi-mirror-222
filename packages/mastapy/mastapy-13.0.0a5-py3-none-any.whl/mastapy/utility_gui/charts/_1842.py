﻿"""_1842.py

CustomLineChart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_LINE_CHART = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'CustomLineChart')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomLineChart',)


class CustomLineChart(_1747.CustomReportChart):
    """CustomLineChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_LINE_CHART

    class _Cast_CustomLineChart:
        """Special nested class for casting CustomLineChart to subclasses."""

        def __init__(self, parent: 'CustomLineChart'):
            self._parent = parent

        @property
        def custom_report_chart(self):
            return self._parent._cast(_1747.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760, _1748
            
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
        def custom_line_chart(self) -> 'CustomLineChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomLineChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def x_values(self):
        """ 'XValues' is the original name of this method."""

        self.wrapped.XValues()

    def y_values(self):
        """ 'YValues' is the original name of this method."""

        self.wrapped.YValues()

    @property
    def cast_to(self) -> 'CustomLineChart._Cast_CustomLineChart':
        return self._Cast_CustomLineChart(self)
