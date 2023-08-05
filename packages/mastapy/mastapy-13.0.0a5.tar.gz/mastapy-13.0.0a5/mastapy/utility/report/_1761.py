"""_1761.py

CustomReportMultiPropertyItemBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.report import _1762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportMultiPropertyItemBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportMultiPropertyItemBase',)


class CustomReportMultiPropertyItemBase(_1762.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(self, parent: 'CustomReportMultiPropertyItemBase'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
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
        def cylindrical_gear_table_with_mg_charts(self):
            from mastapy.gears.gear_designs.cylindrical import _1031
            
            return self._parent._cast(_1031.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(self):
            from mastapy.utility.report import _1747
            
            return self._parent._cast(_1747.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportMultiPropertyItem)

        @property
        def custom_table(self):
            from mastapy.utility.report import _1771
            
            return self._parent._cast(_1771.CustomTable)

        @property
        def custom_line_chart(self):
            from mastapy.utility_gui.charts import _1842
            
            return self._parent._cast(_1842.CustomLineChart)

        @property
        def custom_table_and_chart(self):
            from mastapy.utility_gui.charts import _1843
            
            return self._parent._cast(_1843.CustomTableAndChart)

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
        def custom_report_multi_property_item_base(self) -> 'CustomReportMultiPropertyItemBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportMultiPropertyItemBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase':
        return self._Cast_CustomReportMultiPropertyItemBase(self)
