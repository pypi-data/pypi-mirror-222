"""_7012.py

ConnectionAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ConnectionAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2605
    from mastapy.system_model.connections_and_sockets import _2255
    from mastapy.system_model.analyses_and_results.system_deflections import _2709


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionAdvancedTimeSteppingAnalysisForModulation',)


class ConnectionAdvancedTimeSteppingAnalysisForModulation(_7507.ConnectionStaticLoadAnalysisCase):
    """ConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'ConnectionAdvancedTimeSteppingAnalysisForModulation'):
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
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6976
            
            return self._parent._cast(_6976.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6981
            
            return self._parent._cast(_6981.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def belt_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6986
            
            return self._parent._cast(_6986.BeltConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6989
            
            return self._parent._cast(_6989.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6994
            
            return self._parent._cast(_6994.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6999
            
            return self._parent._cast(_6999.ClutchConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7001
            
            return self._parent._cast(_7001.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7004
            
            return self._parent._cast(_7004.ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7007
            
            return self._parent._cast(_7007.ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7010
            
            return self._parent._cast(_7010.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7015
            
            return self._parent._cast(_7015.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cvt_belt_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7018
            
            return self._parent._cast(_7018.CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7022
            
            return self._parent._cast(_7022.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7023
            
            return self._parent._cast(_7023.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7025
            
            return self._parent._cast(_7025.CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7031
            
            return self._parent._cast(_7031.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7036
            
            return self._parent._cast(_7036.GearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7041
            
            return self._parent._cast(_7041.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7043
            
            return self._parent._cast(_7043.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7045
            
            return self._parent._cast(_7045.KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7048
            
            return self._parent._cast(_7048.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7051
            
            return self._parent._cast(_7051.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_to_part_shear_coupling_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7059
            
            return self._parent._cast(_7059.PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7061
            
            return self._parent._cast(_7061.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7068
            
            return self._parent._cast(_7068.RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def rolling_ring_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7071
            
            return self._parent._cast(_7071.RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7075
            
            return self._parent._cast(_7075.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7078
            
            return self._parent._cast(_7078.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spring_damper_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7081
            
            return self._parent._cast(_7081.SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7084
            
            return self._parent._cast(_7084.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7087
            
            return self._parent._cast(_7087.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def torque_converter_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7096
            
            return self._parent._cast(_7096.TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7102
            
            return self._parent._cast(_7102.WormGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7105
            
            return self._parent._cast(_7105.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self) -> 'ConnectionAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation(self) -> '_2605.AdvancedTimeSteppingAnalysisForModulation':
        """AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def system_deflection_results(self) -> '_2709.ConnectionSystemDeflection':
        """ConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_ConnectionAdvancedTimeSteppingAnalysisForModulation(self)
