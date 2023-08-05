"""_3738.py

VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3693
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3609


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed',)


class VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed(_3693.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed):
    """VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(self):
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
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3691
            
            return self._parent._cast(_3691.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3692
            
            return self._parent._cast(_3692.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3702
            
            return self._parent._cast(_3702.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3703
            
            return self._parent._cast(_3703.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3737
            
            return self._parent._cast(_3737.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(self) -> 'VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3609.VirtualComponentSteadyStateSynchronousResponseAtASpeed]':
        """List[VirtualComponentSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3609.VirtualComponentSteadyStateSynchronousResponseAtASpeed]':
        """List[VirtualComponentSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed(self)
