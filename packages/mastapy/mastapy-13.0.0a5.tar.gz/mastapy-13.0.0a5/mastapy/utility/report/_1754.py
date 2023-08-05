"""_1754.py

CustomReportItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItem',)


class CustomReportItem(_0.APIBase):
    """CustomReportItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM

    class _Cast_CustomReportItem:
        """Special nested class for casting CustomReportItem to subclasses."""

        def __init__(self, parent: 'CustomReportItem'):
            self._parent = parent

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
        def custom_report(self):
            from mastapy.utility.report import _1745
            
            return self._parent._cast(_1745.CustomReport)

        @property
        def custom_report_cad_drawing(self):
            from mastapy.utility.report import _1746
            
            return self._parent._cast(_1746.CustomReportCadDrawing)

        @property
        def custom_report_chart(self):
            from mastapy.utility.report import _1747
            
            return self._parent._cast(_1747.CustomReportChart)

        @property
        def custom_report_column(self):
            from mastapy.utility.report import _1749
            
            return self._parent._cast(_1749.CustomReportColumn)

        @property
        def custom_report_columns(self):
            from mastapy.utility.report import _1750
            
            return self._parent._cast(_1750.CustomReportColumns)

        @property
        def custom_report_definition_item(self):
            from mastapy.utility.report import _1751
            
            return self._parent._cast(_1751.CustomReportDefinitionItem)

        @property
        def custom_report_horizontal_line(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportHorizontalLine)

        @property
        def custom_report_html_item(self):
            from mastapy.utility.report import _1753
            
            return self._parent._cast(_1753.CustomReportHtmlItem)

        @property
        def custom_report_item_container(self):
            from mastapy.utility.report import _1755
            
            return self._parent._cast(_1755.CustomReportItemContainer)

        @property
        def custom_report_item_container_collection(self):
            from mastapy.utility.report import _1756
            
            return self._parent._cast(_1756.CustomReportItemContainerCollection)

        @property
        def custom_report_item_container_collection_base(self):
            from mastapy.utility.report import _1757
            
            return self._parent._cast(_1757.CustomReportItemContainerCollectionBase)

        @property
        def custom_report_item_container_collection_item(self):
            from mastapy.utility.report import _1758
            
            return self._parent._cast(_1758.CustomReportItemContainerCollectionItem)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1760
            
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
        def custom_report_named_item(self):
            from mastapy.utility.report import _1763
            
            return self._parent._cast(_1763.CustomReportNamedItem)

        @property
        def custom_report_status_item(self):
            from mastapy.utility.report import _1765
            
            return self._parent._cast(_1765.CustomReportStatusItem)

        @property
        def custom_report_tab(self):
            from mastapy.utility.report import _1766
            
            return self._parent._cast(_1766.CustomReportTab)

        @property
        def custom_report_tabs(self):
            from mastapy.utility.report import _1767
            
            return self._parent._cast(_1767.CustomReportTabs)

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
        def custom_report_item(self) -> 'CustomReportItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportItem.TYPE'):
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
    def item_type(self) -> 'str':
        """str: 'ItemType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ItemType

        if temp is None:
            return ''

        return temp

    def add_condition(self):
        """ 'AddCondition' is the original name of this method."""

        self.wrapped.AddCondition()

    @property
    def cast_to(self) -> 'CustomReportItem._Cast_CustomReportItem':
        return self._Cast_CustomReportItem(self)
