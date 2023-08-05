"""_3842.py

ShaftStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ShaftStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2465
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.stability_analyses import _3785


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftStabilityAnalysis',)


class ShaftStabilityAnalysis(_3747.AbstractShaftStabilityAnalysis):
    """ShaftStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_STABILITY_ANALYSIS

    class _Cast_ShaftStabilityAnalysis:
        """Special nested class for casting ShaftStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftStabilityAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_stability_analysis(self):
            return self._parent._cast(_3747.AbstractShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3746
            
            return self._parent._cast(_3746.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def component_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3770
            
            return self._parent._cast(_3770.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

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
        def shaft_stability_analysis(self) -> 'ShaftStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2465.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6918.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speeds(self) -> 'List[_3785.CriticalSpeed]':
        """List[CriticalSpeed]: 'CriticalSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeeds

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftStabilityAnalysis]':
        """List[ShaftStabilityAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftStabilityAnalysis._Cast_ShaftStabilityAnalysis':
        return self._Cast_ShaftStabilityAnalysis(self)
