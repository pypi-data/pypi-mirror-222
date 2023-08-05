"""_4078.py

InterMountableComponentConnectionPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4047
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'InterMountableComponentConnectionPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2264


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionPowerFlow',)


class InterMountableComponentConnectionPowerFlow(_4047.ConnectionPowerFlow):
    """InterMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW

    class _Cast_InterMountableComponentConnectionPowerFlow:
        """Special nested class for casting InterMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionPowerFlow'):
            self._parent = parent

        @property
        def connection_power_flow(self):
            return self._parent._cast(_4047.ConnectionPowerFlow)

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
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
            return self._parent._cast(_4016.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def belt_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4021
            
            return self._parent._cast(_4021.BeltConnectionPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4023
            
            return self._parent._cast(_4023.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4028
            
            return self._parent._cast(_4028.BevelGearMeshPowerFlow)

        @property
        def clutch_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4033
            
            return self._parent._cast(_4033.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4038
            
            return self._parent._cast(_4038.ConceptCouplingConnectionPowerFlow)

        @property
        def concept_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4041
            
            return self._parent._cast(_4041.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConicalGearMeshPowerFlow)

        @property
        def coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4049
            
            return self._parent._cast(_4049.CouplingConnectionPowerFlow)

        @property
        def cvt_belt_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4052
            
            return self._parent._cast(_4052.CVTBeltConnectionPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4060
            
            return self._parent._cast(_4060.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4066
            
            return self._parent._cast(_4066.FaceGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4071
            
            return self._parent._cast(_4071.GearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4075
            
            return self._parent._cast(_4075.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4079
            
            return self._parent._cast(_4079.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4082
            
            return self._parent._cast(_4082.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4093
            
            return self._parent._cast(_4093.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def ring_pins_to_disc_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4105
            
            return self._parent._cast(_4105.RingPinsToDiscConnectionPowerFlow)

        @property
        def rolling_ring_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4107
            
            return self._parent._cast(_4107.RollingRingConnectionPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4114
            
            return self._parent._cast(_4114.SpiralBevelGearMeshPowerFlow)

        @property
        def spring_damper_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4117
            
            return self._parent._cast(_4117.SpringDamperConnectionPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4120
            
            return self._parent._cast(_4120.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4123
            
            return self._parent._cast(_4123.StraightBevelGearMeshPowerFlow)

        @property
        def torque_converter_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4133
            
            return self._parent._cast(_4133.TorqueConverterConnectionPowerFlow)

        @property
        def worm_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4139
            
            return self._parent._cast(_4139.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4142
            
            return self._parent._cast(_4142.ZerolBevelGearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(self) -> 'InterMountableComponentConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2264.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow':
        return self._Cast_InterMountableComponentConnectionPowerFlow(self)
