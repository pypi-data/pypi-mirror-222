"""_5537.py

ConnectionCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7505
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ConnectionCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5388


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundMultibodyDynamicsAnalysis',)


class ConnectionCompoundMultibodyDynamicsAnalysis(_7505.ConnectionCompoundAnalysis):
    """ConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectionCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def connection_compound_analysis(self):
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
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5505
            
            return self._parent._cast(_5505.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5507
            
            return self._parent._cast(_5507.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
            
            return self._parent._cast(_5511.BeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5514
            
            return self._parent._cast(_5514.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5519
            
            return self._parent._cast(_5519.BevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5524
            
            return self._parent._cast(_5524.ClutchConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5526
            
            return self._parent._cast(_5526.CoaxialConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5529
            
            return self._parent._cast(_5529.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5532
            
            return self._parent._cast(_5532.ConceptGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5535
            
            return self._parent._cast(_5535.ConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5540
            
            return self._parent._cast(_5540.CouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5542
            
            return self._parent._cast(_5542.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5546
            
            return self._parent._cast(_5546.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5548
            
            return self._parent._cast(_5548.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5550
            
            return self._parent._cast(_5550.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5556
            
            return self._parent._cast(_5556.FaceGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5561
            
            return self._parent._cast(_5561.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5565
            
            return self._parent._cast(_5565.HypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
            
            return self._parent._cast(_5567.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5569
            
            return self._parent._cast(_5569.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5572
            
            return self._parent._cast(_5572.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5575
            
            return self._parent._cast(_5575.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5583
            
            return self._parent._cast(_5583.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5585
            
            return self._parent._cast(_5585.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5592
            
            return self._parent._cast(_5592.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5595
            
            return self._parent._cast(_5595.RollingRingConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5599
            
            return self._parent._cast(_5599.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
            
            return self._parent._cast(_5602.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5605
            
            return self._parent._cast(_5605.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
            
            return self._parent._cast(_5608.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5611
            
            return self._parent._cast(_5611.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5620
            
            return self._parent._cast(_5620.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5626
            
            return self._parent._cast(_5626.WormGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5629
            
            return self._parent._cast(_5629.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_multibody_dynamics_analysis(self) -> 'ConnectionCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5388.ConnectionMultibodyDynamicsAnalysis]':
        """List[ConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5388.ConnectionMultibodyDynamicsAnalysis]':
        """List[ConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis':
        return self._Cast_ConnectionCompoundMultibodyDynamicsAnalysis(self)
