"""_1747.py

CustomReportChart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1760, _1748
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportChart')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportChart',)


class CustomReportChart(_1760.CustomReportMultiPropertyItem['_1748.CustomReportChartItem']):
    """CustomReportChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART

    class _Cast_CustomReportChart:
        """Special nested class for casting CustomReportChart to subclasses."""

        def __init__(self, parent: 'CustomReportChart'):
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
        def shaft_damage_results_table_and_chart(self):
            from mastapy.shafts import _20
            
            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def custom_line_chart(self):
            from mastapy.utility_gui.charts import _1842
            
            return self._parent._cast(_1842.CustomLineChart)

        @property
        def loaded_ball_element_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1933
            
            return self._parent._cast(_1933.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(self):
            from mastapy.bearings.bearing_results import _1937
            
            return self._parent._cast(_1937.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1945
            
            return self._parent._cast(_1945.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(self):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2831
            
            return self._parent._cast(_2831.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4693
            
            return self._parent._cast(_4693.CampbellDiagramReport)

        @property
        def per_mode_results_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4697
            
            return self._parent._cast(_4697.PerModeResultsReport)

        @property
        def custom_report_chart(self) -> 'CustomReportChart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportChart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self) -> 'int':
        """int: 'Height' is the original name of this property."""

        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    def height(self, value: 'int'):
        self.wrapped.Height = int(value) if value is not None else 0

    @property
    def width(self) -> 'int':
        """int: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    def width(self, value: 'int'):
        self.wrapped.Width = int(value) if value is not None else 0

    @property
    def cast_to(self) -> 'CustomReportChart._Cast_CustomReportChart':
        return self._Cast_CustomReportChart(self)
