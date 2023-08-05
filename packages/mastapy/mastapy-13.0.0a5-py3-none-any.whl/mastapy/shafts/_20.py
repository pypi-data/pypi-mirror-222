"""_20.py

ShaftDamageResultsTableAndChart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility.report import _1747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART = python_net_import('SMT.MastaAPI.Shafts', 'ShaftDamageResultsTableAndChart')

if TYPE_CHECKING:
    from mastapy.utility.enums import _1809


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDamageResultsTableAndChart',)


class ShaftDamageResultsTableAndChart(_1747.CustomReportChart):
    """ShaftDamageResultsTableAndChart

    This is a mastapy class.
    """

    TYPE = _SHAFT_DAMAGE_RESULTS_TABLE_AND_CHART

    class _Cast_ShaftDamageResultsTableAndChart:
        """Special nested class for casting ShaftDamageResultsTableAndChart to subclasses."""

        def __init__(self, parent: 'ShaftDamageResultsTableAndChart'):
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
        def shaft_damage_results_table_and_chart(self) -> 'ShaftDamageResultsTableAndChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftDamageResultsTableAndChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display(self) -> '_1809.TableAndChartOptions':
        """TableAndChartOptions: 'Display' is the original name of this property."""

        temp = self.wrapped.Display

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Utility.Enums.TableAndChartOptions')
        return constructor.new_from_mastapy('mastapy.utility.enums._1809', 'TableAndChartOptions')(value) if value is not None else None

    @display.setter
    def display(self, value: '_1809.TableAndChartOptions'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Utility.Enums.TableAndChartOptions')
        self.wrapped.Display = value

    @property
    def cast_to(self) -> 'ShaftDamageResultsTableAndChart._Cast_ShaftDamageResultsTableAndChart':
        return self._Cast_ShaftDamageResultsTableAndChart(self)
