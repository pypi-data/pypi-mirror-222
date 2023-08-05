"""_3478.py

UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3479
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3349


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft',)


class UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft(_3479.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft):
    """UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3479.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3434
            
            return self._parent._cast(_3434.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3382
            
            return self._parent._cast(_3382.ComponentCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3436
            
            return self._parent._cast(_3436.PartCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2460.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3349.UnbalancedMassSteadyStateSynchronousResponseOnAShaft]':
        """List[UnbalancedMassSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3349.UnbalancedMassSteadyStateSynchronousResponseOnAShaft]':
        """List[UnbalancedMassSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft(self)
