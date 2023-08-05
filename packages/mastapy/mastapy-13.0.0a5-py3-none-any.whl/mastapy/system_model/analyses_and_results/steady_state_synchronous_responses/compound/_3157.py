"""_3157.py

GearMeshCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3163
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'GearMeshCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3024


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundSteadyStateSynchronousResponse',)


class GearMeshCompoundSteadyStateSynchronousResponse(_3163.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse):
    """GearMeshCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearMeshCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting GearMeshCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3163.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3133
            
            return self._parent._cast(_3133.ConnectionCompoundSteadyStateSynchronousResponse)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3103
            
            return self._parent._cast(_3103.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3110
            
            return self._parent._cast(_3110.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3115
            
            return self._parent._cast(_3115.BevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3128
            
            return self._parent._cast(_3128.ConceptGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3131
            
            return self._parent._cast(_3131.ConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3146
            
            return self._parent._cast(_3146.CylindricalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3152
            
            return self._parent._cast(_3152.FaceGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3161
            
            return self._parent._cast(_3161.HypoidGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3165
            
            return self._parent._cast(_3165.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3168
            
            return self._parent._cast(_3168.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3171
            
            return self._parent._cast(_3171.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3198
            
            return self._parent._cast(_3198.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3204
            
            return self._parent._cast(_3204.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3207
            
            return self._parent._cast(_3207.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3222
            
            return self._parent._cast(_3222.WormGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3225
            
            return self._parent._cast(_3225.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse)

        @property
        def gear_mesh_compound_steady_state_synchronous_response(self) -> 'GearMeshCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3024.GearMeshSteadyStateSynchronousResponse]':
        """List[GearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3024.GearMeshSteadyStateSynchronousResponse]':
        """List[GearMeshSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundSteadyStateSynchronousResponse._Cast_GearMeshCompoundSteadyStateSynchronousResponse':
        return self._Cast_GearMeshCompoundSteadyStateSynchronousResponse(self)
