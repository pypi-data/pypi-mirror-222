"""_6707.py

InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6677
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'InterMountableComponentConnectionCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundCriticalSpeedAnalysis',)


class InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(_6677.ConnectionCompoundCriticalSpeedAnalysis):
    """InterMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6677.ConnectionCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6647
            
            return self._parent._cast(_6647.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def belt_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6651
            
            return self._parent._cast(_6651.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6654
            
            return self._parent._cast(_6654.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6659
            
            return self._parent._cast(_6659.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
            return self._parent._cast(_6664.ClutchConnectionCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6669
            
            return self._parent._cast(_6669.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6672
            
            return self._parent._cast(_6672.ConceptGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6675
            
            return self._parent._cast(_6675.ConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6680
            
            return self._parent._cast(_6680.CouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6682
            
            return self._parent._cast(_6682.CVTBeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6690
            
            return self._parent._cast(_6690.CylindricalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6696
            
            return self._parent._cast(_6696.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
            
            return self._parent._cast(_6701.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
            
            return self._parent._cast(_6705.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6709
            
            return self._parent._cast(_6709.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6712
            
            return self._parent._cast(_6712.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6715
            
            return self._parent._cast(_6715.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6723
            
            return self._parent._cast(_6723.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6732
            
            return self._parent._cast(_6732.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6735
            
            return self._parent._cast(_6735.RollingRingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6742
            
            return self._parent._cast(_6742.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6745
            
            return self._parent._cast(_6745.SpringDamperConnectionCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6748
            
            return self._parent._cast(_6748.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6751
            
            return self._parent._cast(_6751.StraightBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6760
            
            return self._parent._cast(_6760.TorqueConverterConnectionCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6766
            
            return self._parent._cast(_6766.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6769
            
            return self._parent._cast(_6769.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self) -> 'InterMountableComponentConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6578.InterMountableComponentConnectionCriticalSpeedAnalysis]':
        """List[InterMountableComponentConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6578.InterMountableComponentConnectionCriticalSpeedAnalysis]':
        """List[InterMountableComponentConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(self)
