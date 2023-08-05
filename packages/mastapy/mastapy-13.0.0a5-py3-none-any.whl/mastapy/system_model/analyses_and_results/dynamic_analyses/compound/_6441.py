"""_6441.py

InterMountableComponentConnectionCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'InterMountableComponentConnectionCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionCompoundDynamicAnalysis',)


class InterMountableComponentConnectionCompoundDynamicAnalysis(_6411.ConnectionCompoundDynamicAnalysis):
    """InterMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_InterMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6411.ConnectionCompoundDynamicAnalysis)

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
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6381
            
            return self._parent._cast(_6381.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis)

        @property
        def belt_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6385
            
            return self._parent._cast(_6385.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6388
            
            return self._parent._cast(_6388.BevelDifferentialGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6393
            
            return self._parent._cast(_6393.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
            
            return self._parent._cast(_6398.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6403
            
            return self._parent._cast(_6403.ConceptCouplingConnectionCompoundDynamicAnalysis)

        @property
        def concept_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6406
            
            return self._parent._cast(_6406.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6409
            
            return self._parent._cast(_6409.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6414
            
            return self._parent._cast(_6414.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6416
            
            return self._parent._cast(_6416.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
            
            return self._parent._cast(_6424.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6430
            
            return self._parent._cast(_6430.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6435
            
            return self._parent._cast(_6435.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6439
            
            return self._parent._cast(_6439.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6443
            
            return self._parent._cast(_6443.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
            
            return self._parent._cast(_6446.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6449
            
            return self._parent._cast(_6449.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6457
            
            return self._parent._cast(_6457.PartToPartShearCouplingConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6466
            
            return self._parent._cast(_6466.RingPinsToDiscConnectionCompoundDynamicAnalysis)

        @property
        def rolling_ring_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6469
            
            return self._parent._cast(_6469.RollingRingConnectionCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6476
            
            return self._parent._cast(_6476.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6479
            
            return self._parent._cast(_6479.SpringDamperConnectionCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6482
            
            return self._parent._cast(_6482.StraightBevelDiffGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6485
            
            return self._parent._cast(_6485.StraightBevelGearMeshCompoundDynamicAnalysis)

        @property
        def torque_converter_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
            
            return self._parent._cast(_6494.TorqueConverterConnectionCompoundDynamicAnalysis)

        @property
        def worm_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6500
            
            return self._parent._cast(_6500.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6503
            
            return self._parent._cast(_6503.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self) -> 'InterMountableComponentConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6312.InterMountableComponentConnectionDynamicAnalysis]':
        """List[InterMountableComponentConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6312.InterMountableComponentConnectionDynamicAnalysis]':
        """List[InterMountableComponentConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis':
        return self._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis(self)
