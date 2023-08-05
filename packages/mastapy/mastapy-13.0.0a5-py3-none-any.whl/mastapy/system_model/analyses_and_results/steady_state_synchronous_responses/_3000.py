"""_3000.py

ConnectionSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ConnectionSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3071


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionSteadyStateSynchronousResponse',)


class ConnectionSteadyStateSynchronousResponse(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ConnectionSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(self):
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
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2968
            
            return self._parent._cast(_2968.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2969
            
            return self._parent._cast(_2969.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def belt_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2974
            
            return self._parent._cast(_2974.BeltConnectionSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2976
            
            return self._parent._cast(_2976.BevelDifferentialGearMeshSteadyStateSynchronousResponse)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2981
            
            return self._parent._cast(_2981.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2986
            
            return self._parent._cast(_2986.ClutchConnectionSteadyStateSynchronousResponse)

        @property
        def coaxial_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2989
            
            return self._parent._cast(_2989.CoaxialConnectionSteadyStateSynchronousResponse)

        @property
        def concept_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2991
            
            return self._parent._cast(_2991.ConceptCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def concept_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2994
            
            return self._parent._cast(_2994.ConceptGearMeshSteadyStateSynchronousResponse)

        @property
        def conical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2997
            
            return self._parent._cast(_2997.ConicalGearMeshSteadyStateSynchronousResponse)

        @property
        def coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3002
            
            return self._parent._cast(_3002.CouplingConnectionSteadyStateSynchronousResponse)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3005
            
            return self._parent._cast(_3005.CVTBeltConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3009
            
            return self._parent._cast(_3009.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3010
            
            return self._parent._cast(_3010.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3012
            
            return self._parent._cast(_3012.CylindricalGearMeshSteadyStateSynchronousResponse)

        @property
        def face_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3019
            
            return self._parent._cast(_3019.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3024
            
            return self._parent._cast(_3024.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3028
            
            return self._parent._cast(_3028.HypoidGearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3031
            
            return self._parent._cast(_3031.InterMountableComponentConnectionSteadyStateSynchronousResponse)

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
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3046
            
            return self._parent._cast(_3046.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse)

        @property
        def planetary_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3049
            
            return self._parent._cast(_3049.PlanetaryConnectionSteadyStateSynchronousResponse)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3056
            
            return self._parent._cast(_3056.RingPinsToDiscConnectionSteadyStateSynchronousResponse)

        @property
        def rolling_ring_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3058
            
            return self._parent._cast(_3058.RollingRingConnectionSteadyStateSynchronousResponse)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3063
            
            return self._parent._cast(_3063.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3065
            
            return self._parent._cast(_3065.SpiralBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def spring_damper_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3068
            
            return self._parent._cast(_3068.SpringDamperConnectionSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3074
            
            return self._parent._cast(_3074.StraightBevelDiffGearMeshSteadyStateSynchronousResponse)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3077
            
            return self._parent._cast(_3077.StraightBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def torque_converter_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3086
            
            return self._parent._cast(_3086.TorqueConverterConnectionSteadyStateSynchronousResponse)

        @property
        def worm_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3092
            
            return self._parent._cast(_3092.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3095
            
            return self._parent._cast(_3095.ZerolBevelGearMeshSteadyStateSynchronousResponse)

        @property
        def connection_steady_state_synchronous_response(self) -> 'ConnectionSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2255.Connection':
        """Connection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2255.Connection':
        """Connection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response(self) -> '_3071.SteadyStateSynchronousResponse':
        """SteadyStateSynchronousResponse: 'SteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse':
        return self._Cast_ConnectionSteadyStateSynchronousResponse(self)
