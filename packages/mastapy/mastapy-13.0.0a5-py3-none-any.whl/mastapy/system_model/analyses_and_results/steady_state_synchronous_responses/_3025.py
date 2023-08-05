"""_3025.py

GearSetSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3064
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'GearSetSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetSteadyStateSynchronousResponse',)


class GearSetSteadyStateSynchronousResponse(_3064.SpecialisedAssemblySteadyStateSynchronousResponse):
    """GearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearSetSteadyStateSynchronousResponse:
        """Special nested class for casting GearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearSetSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            return self._parent._cast(_3064.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965
            
            return self._parent._cast(_2965.AbstractAssemblySteadyStateSynchronousResponse)

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
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2970
            
            return self._parent._cast(_2970.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2977
            
            return self._parent._cast(_2977.BevelDifferentialGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2982
            
            return self._parent._cast(_2982.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def concept_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2995
            
            return self._parent._cast(_2995.ConceptGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2998
            
            return self._parent._cast(_2998.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3013
            
            return self._parent._cast(_3013.CylindricalGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3020
            
            return self._parent._cast(_3020.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3029
            
            return self._parent._cast(_3029.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3033
            
            return self._parent._cast(_3033.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3036
            
            return self._parent._cast(_3036.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3039
            
            return self._parent._cast(_3039.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def planetary_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3050
            
            return self._parent._cast(_3050.PlanetaryGearSetSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3066
            
            return self._parent._cast(_3066.SpiralBevelGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3075
            
            return self._parent._cast(_3075.StraightBevelDiffGearSetSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3078
            
            return self._parent._cast(_3078.StraightBevelGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3093
            
            return self._parent._cast(_3093.WormGearSetSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3096
            
            return self._parent._cast(_3096.ZerolBevelGearSetSteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self) -> 'GearSetSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2514.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetSteadyStateSynchronousResponse._Cast_GearSetSteadyStateSynchronousResponse':
        return self._Cast_GearSetSteadyStateSynchronousResponse(self)
