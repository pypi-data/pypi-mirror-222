"""_1846.py

NDChartDefinition
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility.report import _1739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ND_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'NDChartDefinition')

if TYPE_CHECKING:
    from mastapy.utility.report import _1734


__docformat__ = 'restructuredtext en'
__all__ = ('NDChartDefinition',)


class NDChartDefinition(_1739.ChartDefinition):
    """NDChartDefinition

    This is a mastapy class.
    """

    TYPE = _ND_CHART_DEFINITION

    class _Cast_NDChartDefinition:
        """Special nested class for casting NDChartDefinition to subclasses."""

        def __init__(self, parent: 'NDChartDefinition'):
            self._parent = parent

        @property
        def chart_definition(self):
            return self._parent._cast(_1739.ChartDefinition)

        @property
        def bubble_chart_definition(self):
            from mastapy.utility_gui.charts import _1840
            
            return self._parent._cast(_1840.BubbleChartDefinition)

        @property
        def parallel_coordinates_chart_definition(self):
            from mastapy.utility_gui.charts import _1847
            
            return self._parent._cast(_1847.ParallelCoordinatesChartDefinition)

        @property
        def scatter_chart_definition(self):
            from mastapy.utility_gui.charts import _1849
            
            return self._parent._cast(_1849.ScatterChartDefinition)

        @property
        def three_d_chart_definition(self):
            from mastapy.utility_gui.charts import _1852
            
            return self._parent._cast(_1852.ThreeDChartDefinition)

        @property
        def three_d_vector_chart_definition(self):
            from mastapy.utility_gui.charts import _1853
            
            return self._parent._cast(_1853.ThreeDVectorChartDefinition)

        @property
        def two_d_chart_definition(self):
            from mastapy.utility_gui.charts import _1854
            
            return self._parent._cast(_1854.TwoDChartDefinition)

        @property
        def nd_chart_definition(self) -> 'NDChartDefinition':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NDChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def specify_shared_chart_settings(self) -> 'bool':
        """bool: 'SpecifySharedChartSettings' is the original name of this property."""

        temp = self.wrapped.SpecifySharedChartSettings

        if temp is None:
            return False

        return temp

    @specify_shared_chart_settings.setter
    def specify_shared_chart_settings(self, value: 'bool'):
        self.wrapped.SpecifySharedChartSettings = bool(value) if value is not None else False

    @property
    def x_axis(self) -> '_1734.AxisSettings':
        """AxisSettings: 'XAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y_axis(self) -> '_1734.AxisSettings':
        """AxisSettings: 'YAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'NDChartDefinition._Cast_NDChartDefinition':
        return self._Cast_NDChartDefinition(self)
