"""_1933.py

LoadedBallElementChartReporter
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility.report import _1747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_ELEMENT_CHART_REPORTER = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBallElementChartReporter')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1949


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallElementChartReporter',)


class LoadedBallElementChartReporter(_1747.CustomReportChart):
    """LoadedBallElementChartReporter

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_ELEMENT_CHART_REPORTER

    class _Cast_LoadedBallElementChartReporter:
        """Special nested class for casting LoadedBallElementChartReporter to subclasses."""

        def __init__(self, parent: 'LoadedBallElementChartReporter'):
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
        def loaded_ball_element_chart_reporter(self) -> 'LoadedBallElementChartReporter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBallElementChartReporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_to_plot(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType':
        """enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType: 'ElementToPlot' is the original name of this property."""

        temp = self.wrapped.ElementToPlot

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @element_to_plot.setter
    def element_to_plot(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LoadedBallElementPropertyType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ElementToPlot = value

    @property
    def cast_to(self) -> 'LoadedBallElementChartReporter._Cast_LoadedBallElementChartReporter':
        return self._Cast_LoadedBallElementChartReporter(self)
