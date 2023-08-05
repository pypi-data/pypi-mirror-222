"""_3394.py

CouplingCompoundSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3455
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'CouplingCompoundSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3266


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundSteadyStateSynchronousResponseOnAShaft',)


class CouplingCompoundSteadyStateSynchronousResponseOnAShaft(_3455.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft):
    """CouplingCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_CouplingCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'CouplingCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3455.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3357
            
            return self._parent._cast(_3357.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft)

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
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3378
            
            return self._parent._cast(_3378.ClutchCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3383
            
            return self._parent._cast(_3383.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3437
            
            return self._parent._cast(_3437.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3459
            
            return self._parent._cast(_3459.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3474
            
            return self._parent._cast(_3474.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'CouplingCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3266.CouplingSteadyStateSynchronousResponseOnAShaft]':
        """List[CouplingSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3266.CouplingSteadyStateSynchronousResponseOnAShaft]':
        """List[CouplingSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CouplingCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_CouplingCompoundSteadyStateSynchronousResponseOnAShaft(self)
