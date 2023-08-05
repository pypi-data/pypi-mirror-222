"""_5502.py

AbstractAssemblyCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AbstractAssemblyCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5350


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundMultibodyDynamicsAnalysis',)


class AbstractAssemblyCompoundMultibodyDynamicsAnalysis(_5581.PartCompoundMultibodyDynamicsAnalysis):
    """AbstractAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5581.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5508
            
            return self._parent._cast(_5508.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5509
            
            return self._parent._cast(_5509.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5512
            
            return self._parent._cast(_5512.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5520
            
            return self._parent._cast(_5520.BevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5522
            
            return self._parent._cast(_5522.BoltedJointCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5523
            
            return self._parent._cast(_5523.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5528
            
            return self._parent._cast(_5528.ConceptCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5533
            
            return self._parent._cast(_5533.ConceptGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5536
            
            return self._parent._cast(_5536.ConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5539
            
            return self._parent._cast(_5539.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5543
            
            return self._parent._cast(_5543.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5545
            
            return self._parent._cast(_5545.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5551
            
            return self._parent._cast(_5551.CylindricalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5557
            
            return self._parent._cast(_5557.FaceGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5559
            
            return self._parent._cast(_5559.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
            
            return self._parent._cast(_5562.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
            
            return self._parent._cast(_5566.HypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5570
            
            return self._parent._cast(_5570.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5573
            
            return self._parent._cast(_5573.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
            
            return self._parent._cast(_5576.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5582
            
            return self._parent._cast(_5582.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5586
            
            return self._parent._cast(_5586.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5593
            
            return self._parent._cast(_5593.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def root_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5596
            
            return self._parent._cast(_5596.RootAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5600
            
            return self._parent._cast(_5600.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
            
            return self._parent._cast(_5603.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5604
            
            return self._parent._cast(_5604.SpringDamperCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5609
            
            return self._parent._cast(_5609.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5612
            
            return self._parent._cast(_5612.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
            
            return self._parent._cast(_5615.SynchroniserCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5619
            
            return self._parent._cast(_5619.TorqueConverterCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5627
            
            return self._parent._cast(_5627.WormGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5630
            
            return self._parent._cast(_5630.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self) -> 'AbstractAssemblyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5350.AbstractAssemblyMultibodyDynamicsAnalysis]':
        """List[AbstractAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5350.AbstractAssemblyMultibodyDynamicsAnalysis]':
        """List[AbstractAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis(self)
