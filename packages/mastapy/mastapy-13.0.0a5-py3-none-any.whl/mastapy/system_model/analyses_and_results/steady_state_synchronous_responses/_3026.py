"""_3026.py

GearSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'GearSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = 'restructuredtext en'
__all__ = ('GearSteadyStateSynchronousResponse',)


class GearSteadyStateSynchronousResponse(_3043.MountableComponentSteadyStateSynchronousResponse):
    """GearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearSteadyStateSynchronousResponse:
        """Special nested class for casting GearSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(self):
            return self._parent._cast(_3043.MountableComponentSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartSteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2971
            
            return self._parent._cast(_2971.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2978
            
            return self._parent._cast(_2978.BevelDifferentialGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2979
            
            return self._parent._cast(_2979.BevelDifferentialPlanetGearSteadyStateSynchronousResponse)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2980
            
            return self._parent._cast(_2980.BevelDifferentialSunGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2983
            
            return self._parent._cast(_2983.BevelGearSteadyStateSynchronousResponse)

        @property
        def concept_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2996
            
            return self._parent._cast(_2996.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2999
            
            return self._parent._cast(_2999.ConicalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3014
            
            return self._parent._cast(_3014.CylindricalGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3015
            
            return self._parent._cast(_3015.CylindricalPlanetGearSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3021
            
            return self._parent._cast(_3021.FaceGearSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3030
            
            return self._parent._cast(_3030.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3034
            
            return self._parent._cast(_3034.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3037
            
            return self._parent._cast(_3037.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3040
            
            return self._parent._cast(_3040.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3067
            
            return self._parent._cast(_3067.SpiralBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3076
            
            return self._parent._cast(_3076.StraightBevelDiffGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3079
            
            return self._parent._cast(_3079.StraightBevelGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3080
            
            return self._parent._cast(_3080.StraightBevelPlanetGearSteadyStateSynchronousResponse)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3081
            
            return self._parent._cast(_3081.StraightBevelSunGearSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3094
            
            return self._parent._cast(_3094.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3097
            
            return self._parent._cast(_3097.ZerolBevelGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self) -> 'GearSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2512.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSteadyStateSynchronousResponse._Cast_GearSteadyStateSynchronousResponse':
        return self._Cast_GearSteadyStateSynchronousResponse(self)
