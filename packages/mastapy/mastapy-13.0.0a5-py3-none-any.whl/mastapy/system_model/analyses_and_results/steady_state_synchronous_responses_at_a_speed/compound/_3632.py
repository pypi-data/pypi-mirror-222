"""_3632.py

BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'BevelGearCompoundSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3504


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundSteadyStateSynchronousResponseAtASpeed',)


class BevelGearCompoundSteadyStateSynchronousResponseAtASpeed(_3620.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed):
    """BevelGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_BevelGearCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'BevelGearCompoundSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3620.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3648
            
            return self._parent._cast(_3648.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3674
            
            return self._parent._cast(_3674.GearCompoundSteadyStateSynchronousResponseAtASpeed)

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
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3627
            
            return self._parent._cast(_3627.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3630
            
            return self._parent._cast(_3630.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3631
            
            return self._parent._cast(_3631.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3715
            
            return self._parent._cast(_3715.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3721
            
            return self._parent._cast(_3721.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3724
            
            return self._parent._cast(_3724.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3727
            
            return self._parent._cast(_3727.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3728
            
            return self._parent._cast(_3728.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3742
            
            return self._parent._cast(_3742.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed)

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(self) -> 'BevelGearCompoundSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3504.BevelGearSteadyStateSynchronousResponseAtASpeed]':
        """List[BevelGearSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3504.BevelGearSteadyStateSynchronousResponseAtASpeed]':
        """List[BevelGearSteadyStateSynchronousResponseAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearCompoundSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_BevelGearCompoundSteadyStateSynchronousResponseAtASpeed(self)
