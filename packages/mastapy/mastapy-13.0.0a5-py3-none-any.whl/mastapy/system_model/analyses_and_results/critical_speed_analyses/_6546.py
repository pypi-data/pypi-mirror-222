"""_6546.py

ConnectionCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ConnectionCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _2607


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCriticalSpeedAnalysis',)


class ConnectionCriticalSpeedAnalysis(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_CRITICAL_SPEED_ANALYSIS

    class _Cast_ConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCriticalSpeedAnalysis'):
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
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6514
            
            return self._parent._cast(_6514.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6516
            
            return self._parent._cast(_6516.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis)

        @property
        def belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6520
            
            return self._parent._cast(_6520.BeltConnectionCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6523
            
            return self._parent._cast(_6523.BevelDifferentialGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6528
            
            return self._parent._cast(_6528.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6532
            
            return self._parent._cast(_6532.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def coaxial_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6535
            
            return self._parent._cast(_6535.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6537
            
            return self._parent._cast(_6537.ConceptCouplingConnectionCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
            
            return self._parent._cast(_6541.ConceptGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544
            
            return self._parent._cast(_6544.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6548
            
            return self._parent._cast(_6548.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6553
            
            return self._parent._cast(_6553.CVTBeltConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
            
            return self._parent._cast(_6557.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6559
            
            return self._parent._cast(_6559.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6561
            
            return self._parent._cast(_6561.CylindricalGearMeshCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6567
            
            return self._parent._cast(_6567.FaceGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
            
            return self._parent._cast(_6572.GearMeshCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
            
            return self._parent._cast(_6576.HypoidGearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
            
            return self._parent._cast(_6578.InterMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
            
            return self._parent._cast(_6580.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6583
            
            return self._parent._cast(_6583.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6586
            
            return self._parent._cast(_6586.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6593
            
            return self._parent._cast(_6593.PartToPartShearCouplingConnectionCriticalSpeedAnalysis)

        @property
        def planetary_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6596
            
            return self._parent._cast(_6596.PlanetaryConnectionCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6603
            
            return self._parent._cast(_6603.RingPinsToDiscConnectionCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605
            
            return self._parent._cast(_6605.RollingRingConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
            
            return self._parent._cast(_6610.ShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
            
            return self._parent._cast(_6613.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6615
            
            return self._parent._cast(_6615.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6619
            
            return self._parent._cast(_6619.StraightBevelDiffGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6622
            
            return self._parent._cast(_6622.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6630
            
            return self._parent._cast(_6630.TorqueConverterConnectionCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637
            
            return self._parent._cast(_6637.WormGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6640
            
            return self._parent._cast(_6640.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self) -> 'ConnectionCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCriticalSpeedAnalysis.TYPE'):
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
    def critical_speed_analysis(self) -> '_2607.CriticalSpeedAnalysis':
        """CriticalSpeedAnalysis: 'CriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionCriticalSpeedAnalysis._Cast_ConnectionCriticalSpeedAnalysis':
        return self._Cast_ConnectionCriticalSpeedAnalysis(self)
