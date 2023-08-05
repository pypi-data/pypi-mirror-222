"""_3156.py

GearCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'GearCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundSteadyStateSynchronousResponse',)


class GearCompoundSteadyStateSynchronousResponse(_3175.MountableComponentCompoundSteadyStateSynchronousResponse):
    """GearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting GearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3175.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3123
            
            return self._parent._cast(_3123.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
            
            return self._parent._cast(_3177.PartCompoundSteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3102
            
            return self._parent._cast(_3102.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3109
            
            return self._parent._cast(_3109.BevelDifferentialGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3112
            
            return self._parent._cast(_3112.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3113
            
            return self._parent._cast(_3113.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3114
            
            return self._parent._cast(_3114.BevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3127
            
            return self._parent._cast(_3127.ConceptGearCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
            
            return self._parent._cast(_3130.ConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3145
            
            return self._parent._cast(_3145.CylindricalGearCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3148
            
            return self._parent._cast(_3148.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3151
            
            return self._parent._cast(_3151.FaceGearCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3160
            
            return self._parent._cast(_3160.HypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3164
            
            return self._parent._cast(_3164.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3167
            
            return self._parent._cast(_3167.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3170
            
            return self._parent._cast(_3170.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3197
            
            return self._parent._cast(_3197.SpiralBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3203
            
            return self._parent._cast(_3203.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3206
            
            return self._parent._cast(_3206.StraightBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3209
            
            return self._parent._cast(_3209.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3210
            
            return self._parent._cast(_3210.StraightBevelSunGearCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3221
            
            return self._parent._cast(_3221.WormGearCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3224
            
            return self._parent._cast(_3224.ZerolBevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_compound_steady_state_synchronous_response(self) -> 'GearCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3026.GearSteadyStateSynchronousResponse]':
        """List[GearSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3026.GearSteadyStateSynchronousResponse]':
        """List[GearSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundSteadyStateSynchronousResponse._Cast_GearCompoundSteadyStateSynchronousResponse':
        return self._Cast_GearCompoundSteadyStateSynchronousResponse(self)
