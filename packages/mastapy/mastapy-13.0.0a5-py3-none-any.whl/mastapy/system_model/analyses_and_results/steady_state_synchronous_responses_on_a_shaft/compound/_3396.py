"""_3396.py

CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3265


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft',)


class CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(_3434.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft):
    """CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(self):
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
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3380
            
            return self._parent._cast(_3380.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3385
            
            return self._parent._cast(_3385.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3399
            
            return self._parent._cast(_3399.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3439
            
            return self._parent._cast(_3439.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3445
            
            return self._parent._cast(_3445.PulleyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3449
            
            return self._parent._cast(_3449.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3461
            
            return self._parent._cast(_3461.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3471
            
            return self._parent._cast(_3471.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3472
            
            return self._parent._cast(_3472.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3473
            
            return self._parent._cast(_3473.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3476
            
            return self._parent._cast(_3476.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3477
            
            return self._parent._cast(_3477.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3265.CouplingHalfSteadyStateSynchronousResponseOnAShaft]':
        """List[CouplingHalfSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3265.CouplingHalfSteadyStateSynchronousResponseOnAShaft]':
        """List[CouplingHalfSteadyStateSynchronousResponseOnAShaft]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft(self)
