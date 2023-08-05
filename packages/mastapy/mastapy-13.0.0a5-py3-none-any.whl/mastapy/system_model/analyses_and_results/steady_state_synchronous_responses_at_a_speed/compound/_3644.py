"""_3644.py

ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2564
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3513


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed',)


class ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(_3655.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed):
    """ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3655.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3693
            
            return self._parent._cast(_3693.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3641
            
            return self._parent._cast(_3641.ComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3695
            
            return self._parent._cast(_3695.PartCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(self) -> 'ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2564.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3513.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed]':
        """List[ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3513.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed]':
        """List[ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(self)
