"""_3024.py

GearMeshSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3031
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'GearMeshSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshSteadyStateSynchronousResponse',)


class GearMeshSteadyStateSynchronousResponse(_3031.InterMountableComponentConnectionSteadyStateSynchronousResponse):
    """GearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_GearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting GearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'GearMeshSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            return self._parent._cast(_3031.InterMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3000
            
            return self._parent._cast(_3000.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2969
            
            return self._parent._cast(_2969.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2976
            
            return self._parent._cast(_2976.BevelDifferentialGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2981
            
            return self._parent._cast(_2981.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2994
            
            return self._parent._cast(_2994.ConceptGearMeshSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2997
            
            return self._parent._cast(_2997.ConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3012
            
            return self._parent._cast(_3012.CylindricalGearMeshSteadyStateSynchronousResponse)

        @property
        def face_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3019
            
            return self._parent._cast(_3019.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
            
            return self._parent._cast(_3028.HypoidGearMeshSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3032
            
            return self._parent._cast(_3032.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3035
            
            return self._parent._cast(_3035.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3038
            
            return self._parent._cast(_3038.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3065
            
            return self._parent._cast(_3065.SpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3074
            
            return self._parent._cast(_3074.StraightBevelDiffGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3077
            
            return self._parent._cast(_3077.StraightBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def worm_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3092
            
            return self._parent._cast(_3092.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3095
            
            return self._parent._cast(_3095.ZerolBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(self) -> 'GearMeshSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2296.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshSteadyStateSynchronousResponse._Cast_GearMeshSteadyStateSynchronousResponse':
        return self._Cast_GearMeshSteadyStateSynchronousResponse(self)
