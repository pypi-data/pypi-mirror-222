"""_3370.py

BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2498
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3239
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3368, _3369


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft',)


class BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft(_3375.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft):
    """BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3375.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3363
            
            return self._parent._cast(_3363.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3391
            
            return self._parent._cast(_3391.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3417
            
            return self._parent._cast(_3417.GearSetCompoundSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3455
            
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
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3239.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3368.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialGearsCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_compound_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3369.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]: 'BevelDifferentialMeshesCompoundSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesCompoundSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3239.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]':
        """List[BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft(self)
