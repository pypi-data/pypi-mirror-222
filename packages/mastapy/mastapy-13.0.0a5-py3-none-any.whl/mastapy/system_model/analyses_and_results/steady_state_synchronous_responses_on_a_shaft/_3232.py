"""_3232.py

AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3260
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2496


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft',)


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(_3260.ConicalGearSetSteadyStateSynchronousResponseOnAShaft):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3260.ConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3286
            
            return self._parent._cast(_3286.GearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3325
            
            return self._parent._cast(_3325.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3227
            
            return self._parent._cast(_3227.AbstractAssemblySteadyStateSynchronousResponseOnAShaft)

        @property
        def part_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
            
            return self._parent._cast(_3306.PartSteadyStateSynchronousResponseOnAShaft)

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
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3239
            
            return self._parent._cast(_3239.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3244
            
            return self._parent._cast(_3244.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3290
            
            return self._parent._cast(_3290.HypoidGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3327
            
            return self._parent._cast(_3327.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3334
            
            return self._parent._cast(_3334.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3337
            
            return self._parent._cast(_3337.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3355
            
            return self._parent._cast(_3355.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self) -> 'AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2496.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft(self)
