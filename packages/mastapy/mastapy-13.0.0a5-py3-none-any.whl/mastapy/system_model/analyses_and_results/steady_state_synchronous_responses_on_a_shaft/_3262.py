"""_3262.py

ConnectionSteadyStateSynchronousResponseOnAShaft
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'ConnectionSteadyStateSynchronousResponseOnAShaft')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3332


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionSteadyStateSynchronousResponseOnAShaft',)


class ConnectionSteadyStateSynchronousResponseOnAShaft(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    class _Cast_ConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(self, parent: 'ConnectionSteadyStateSynchronousResponseOnAShaft'):
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
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3230
            
            return self._parent._cast(_3230.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3231
            
            return self._parent._cast(_3231.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def belt_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3236
            
            return self._parent._cast(_3236.BeltConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3238
            
            return self._parent._cast(_3238.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3243
            
            return self._parent._cast(_3243.BevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3248
            
            return self._parent._cast(_3248.ClutchConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3251
            
            return self._parent._cast(_3251.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3253
            
            return self._parent._cast(_3253.ConceptCouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3256
            
            return self._parent._cast(_3256.ConceptGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3259
            
            return self._parent._cast(_3259.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3264
            
            return self._parent._cast(_3264.CouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cvt_belt_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3267
            
            return self._parent._cast(_3267.CVTBeltConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3271
            
            return self._parent._cast(_3271.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3272
            
            return self._parent._cast(_3272.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3274
            
            return self._parent._cast(_3274.CylindricalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def face_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3280
            
            return self._parent._cast(_3280.FaceGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3285
            
            return self._parent._cast(_3285.GearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3289
            
            return self._parent._cast(_3289.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3292
            
            return self._parent._cast(_3292.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3293
            
            return self._parent._cast(_3293.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3296
            
            return self._parent._cast(_3296.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3299
            
            return self._parent._cast(_3299.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3307
            
            return self._parent._cast(_3307.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def planetary_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3310
            
            return self._parent._cast(_3310.PlanetaryConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3317
            
            return self._parent._cast(_3317.RingPinsToDiscConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def rolling_ring_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3319
            
            return self._parent._cast(_3319.RollingRingConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3324
            
            return self._parent._cast(_3324.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3326
            
            return self._parent._cast(_3326.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def spring_damper_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3329
            
            return self._parent._cast(_3329.SpringDamperConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3333
            
            return self._parent._cast(_3333.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3336
            
            return self._parent._cast(_3336.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def torque_converter_connection_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3345
            
            return self._parent._cast(_3345.TorqueConverterConnectionSteadyStateSynchronousResponseOnAShaft)

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3351
            
            return self._parent._cast(_3351.WormGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3354
            
            return self._parent._cast(_3354.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft)

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(self) -> 'ConnectionSteadyStateSynchronousResponseOnAShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionSteadyStateSynchronousResponseOnAShaft.TYPE'):
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
    def steady_state_synchronous_response_on_a_shaft(self) -> '_3332.SteadyStateSynchronousResponseOnAShaft':
        """SteadyStateSynchronousResponseOnAShaft: 'SteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionSteadyStateSynchronousResponseOnAShaft._Cast_ConnectionSteadyStateSynchronousResponseOnAShaft':
        return self._Cast_ConnectionSteadyStateSynchronousResponseOnAShaft(self)
