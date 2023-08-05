"""_5067.py

SpringDamperHalfCompoundModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'SpringDamperHalfCompoundModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4937


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundModalAnalysisAtAStiffness',)


class SpringDamperHalfCompoundModalAnalysisAtAStiffness(_5002.CouplingHalfCompoundModalAnalysisAtAStiffness):
    """SpringDamperHalfCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_SpringDamperHalfCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting SpringDamperHalfCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'SpringDamperHalfCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5002.CouplingHalfCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5040
            
            return self._parent._cast(_5040.MountableComponentCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4988
            
            return self._parent._cast(_4988.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5042
            
            return self._parent._cast(_5042.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(self) -> 'SpringDamperHalfCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2583.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4937.SpringDamperHalfModalAnalysisAtAStiffness]':
        """List[SpringDamperHalfModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4937.SpringDamperHalfModalAnalysisAtAStiffness]':
        """List[SpringDamperHalfModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpringDamperHalfCompoundModalAnalysisAtAStiffness._Cast_SpringDamperHalfCompoundModalAnalysisAtAStiffness':
        return self._Cast_SpringDamperHalfCompoundModalAnalysisAtAStiffness(self)
