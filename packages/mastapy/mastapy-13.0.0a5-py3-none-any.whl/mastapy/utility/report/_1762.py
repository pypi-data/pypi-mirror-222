"""_1762.py

CustomReportNameableItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1754
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_NAMEABLE_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportNameableItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportNameableItem',)


class CustomReportNameableItem(_1754.CustomReportItem):
    """CustomReportNameableItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_NAMEABLE_ITEM

    class _Cast_CustomReportNameableItem:
        """Special nested class for casting CustomReportNameableItem to subclasses."""

        def __init__(self, parent: 'CustomReportNameableItem'):
            self._parent = parent

        @property
        def custom_report_item(self):
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
        def ad_hoc_custom_table(self):
            from mastapy.utility.report import _1733
            
            return self._parent._cast(_1733.AdHocCustomTable)

        @property
        def custom_chart(self):
            from mastapy.utility.report import _1741
            
            return self._parent._cast(_1741.CustomChart)

        @property
        def custom_drawing(self):
            from mastapy.utility.report import _1742
            
            return self._parent._cast(_1742.CustomDrawing)

        @property
        def custom_graphic(self):
            from mastapy.utility.report import _1743
            
            return self._parent._cast(_1743.CustomGraphic)

        @property
        def custom_image(self):
            from mastapy.utility.report import _1744
            
            return self._parent._cast(_1744.CustomImage)

        @property
        def custom_report_cad_drawing(self):
            from mastapy.utility.report import _1746
            
            return self._parent._cast(_1746.CustomReportCadDrawing)

        @property
        def custom_report_chart(self):
            from mastapy.utility.report import _1747
            
            return self._parent._cast(_1747.CustomReportChart)

        @property
        def custom_report_definition_item(self):
            from mastapy.utility.report import _1751
            
            return self._parent._cast(_1751.CustomReportDefinitionItem)

        @property
        def custom_report_html_item(self):
            from mastapy.utility.report import _1753
            
            return self._parent._cast(_1753.CustomReportHtmlItem)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1761
            
            return self._parent._cast(_1761.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_named_item(self):
            from mastapy.utility.report import _1763
            
            return self._parent._cast(_1763.CustomReportNamedItem)

        @property
        def custom_report_status_item(self):
            from mastapy.utility.report import _1765
            
            return self._parent._cast(_1765.CustomReportStatusItem)

        @property
        def custom_report_text(self):
            from mastapy.utility.report import _1768
            
            return self._parent._cast(_1768.CustomReportText)

        @property
        def custom_sub_report(self):
            from mastapy.utility.report import _1770
            
            return self._parent._cast(_1770.CustomSubReport)

        @property
        def custom_table(self):
            from mastapy.utility.report import _1771
            
            return self._parent._cast(_1771.CustomTable)

        @property
        def dynamic_custom_report_item(self):
            from mastapy.utility.report import _1773
            
            return self._parent._cast(_1773.DynamicCustomReportItem)

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
        def loaded_bearing_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1934
            
            return self._parent._cast(_1934.LoadedBearingChartReporter)

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
        def parametric_study_histogram(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4364
            
            return self._parent._cast(_4364.ParametricStudyHistogram)

        @property
        def campbell_diagram_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4693
            
            return self._parent._cast(_4693.CampbellDiagramReport)

        @property
        def per_mode_results_report(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4697
            
            return self._parent._cast(_4697.PerModeResultsReport)

        @property
        def custom_report_nameable_item(self) -> 'CustomReportNameableItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportNameableItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value is not None else ''

    @property
    def x_position_for_cad(self) -> 'float':
        """float: 'XPositionForCAD' is the original name of this property."""

        temp = self.wrapped.XPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @x_position_for_cad.setter
    def x_position_for_cad(self, value: 'float'):
        self.wrapped.XPositionForCAD = float(value) if value is not None else 0.0

    @property
    def y_position_for_cad(self) -> 'float':
        """float: 'YPositionForCAD' is the original name of this property."""

        temp = self.wrapped.YPositionForCAD

        if temp is None:
            return 0.0

        return temp

    @y_position_for_cad.setter
    def y_position_for_cad(self, value: 'float'):
        self.wrapped.YPositionForCAD = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'CustomReportNameableItem._Cast_CustomReportNameableItem':
        return self._Cast_CustomReportNameableItem(self)
