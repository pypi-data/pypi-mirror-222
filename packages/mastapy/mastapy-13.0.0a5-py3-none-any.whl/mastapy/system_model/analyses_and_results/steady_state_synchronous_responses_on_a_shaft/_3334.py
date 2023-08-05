"""_3334.py

StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3244
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3335, _3333


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft',)


class StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft(_3244.BevelGearSetSteadyStateSynchronousResponseOnAShaft):
    """StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft'):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            return self._parent._cast(_3244.BevelGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3232
            
            return self._parent._cast(_3232.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3260
            
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
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(self) -> 'StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2528.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6929.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3335.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3333.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft]: 'StraightBevelDiffMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft(self)
