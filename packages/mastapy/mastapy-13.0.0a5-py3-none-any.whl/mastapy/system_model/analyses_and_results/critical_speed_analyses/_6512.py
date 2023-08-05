"""_6512.py

AbstractShaftCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'AbstractShaftCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2418


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCriticalSpeedAnalysis',)


class AbstractShaftCriticalSpeedAnalysis(_6513.AbstractShaftOrHousingCriticalSpeedAnalysis):
    """AbstractShaftCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_CRITICAL_SPEED_ANALYSIS

    class _Cast_AbstractShaftCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(self):
            return self._parent._cast(_6513.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6536
            
            return self._parent._cast(_6536.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
            
            return self._parent._cast(_6592.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6558
            
            return self._parent._cast(_6558.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6608
            
            return self._parent._cast(_6608.ShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(self) -> 'AbstractShaftCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2418.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftCriticalSpeedAnalysis._Cast_AbstractShaftCriticalSpeedAnalysis':
        return self._Cast_AbstractShaftCriticalSpeedAnalysis(self)
