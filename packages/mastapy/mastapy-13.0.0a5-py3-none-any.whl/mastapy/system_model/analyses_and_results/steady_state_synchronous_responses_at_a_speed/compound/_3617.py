"""_3617.py

AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3488


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed',)


class AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed(_3618.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed):
    """AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3618.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3661
            
            return self._parent._cast(_3661.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3711
            
            return self._parent._cast(_3711.ShaftCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(self) -> 'AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3488.AbstractShaftSteadyStateSynchronousResponseAtASpeed]':
        """List[AbstractShaftSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3488.AbstractShaftSteadyStateSynchronousResponseAtASpeed]':
        """List[AbstractShaftSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed(self)
