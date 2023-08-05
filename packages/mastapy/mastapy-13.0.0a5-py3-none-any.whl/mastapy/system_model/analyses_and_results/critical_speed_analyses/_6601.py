"""_6601.py

PulleyCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'PulleyCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _6908


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCriticalSpeedAnalysis',)


class PulleyCriticalSpeedAnalysis(_6550.CouplingHalfCriticalSpeedAnalysis):
    """PulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_CRITICAL_SPEED_ANALYSIS

    class _Cast_PulleyCriticalSpeedAnalysis:
        """Special nested class for casting PulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'PulleyCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(self):
            return self._parent._cast(_6550.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590
            
            return self._parent._cast(_6590.MountableComponentCriticalSpeedAnalysis)

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
        def cvt_pulley_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6555
            
            return self._parent._cast(_6555.CVTPulleyCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(self) -> 'PulleyCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PulleyCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2572.Pulley':
        """Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6908.PulleyLoadCase':
        """PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis':
        return self._Cast_PulleyCriticalSpeedAnalysis(self)
