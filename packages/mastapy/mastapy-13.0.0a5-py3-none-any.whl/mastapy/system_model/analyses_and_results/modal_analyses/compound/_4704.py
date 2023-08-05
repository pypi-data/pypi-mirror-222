"""_4704.py

AbstractAssemblyCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AbstractAssemblyCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4550


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundModalAnalysis',)


class AbstractAssemblyCompoundModalAnalysis(_4783.PartCompoundModalAnalysis):
    """AbstractAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    class _Cast_AbstractAssemblyCompoundModalAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundModalAnalysis'):
            self._parent = parent

        @property
        def part_compound_modal_analysis(self):
            return self._parent._cast(_4783.PartCompoundModalAnalysis)

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
        def agma_gleason_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4710
            
            return self._parent._cast(_4710.AGMAGleasonConicalGearSetCompoundModalAnalysis)

        @property
        def assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4711
            
            return self._parent._cast(_4711.AssemblyCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4714
            
            return self._parent._cast(_4714.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4717
            
            return self._parent._cast(_4717.BevelDifferentialGearSetCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4722
            
            return self._parent._cast(_4722.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4724
            
            return self._parent._cast(_4724.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4725
            
            return self._parent._cast(_4725.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4730
            
            return self._parent._cast(_4730.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4735
            
            return self._parent._cast(_4735.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4738
            
            return self._parent._cast(_4738.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4741
            
            return self._parent._cast(_4741.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
            
            return self._parent._cast(_4745.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4747
            
            return self._parent._cast(_4747.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4753
            
            return self._parent._cast(_4753.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
            
            return self._parent._cast(_4759.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
            
            return self._parent._cast(_4761.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4764
            
            return self._parent._cast(_4764.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4768
            
            return self._parent._cast(_4768.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4772
            
            return self._parent._cast(_4772.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4775
            
            return self._parent._cast(_4775.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4778
            
            return self._parent._cast(_4778.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
            
            return self._parent._cast(_4784.PartToPartShearCouplingCompoundModalAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
            
            return self._parent._cast(_4788.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4795
            
            return self._parent._cast(_4795.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4798
            
            return self._parent._cast(_4798.RootAssemblyCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
            
            return self._parent._cast(_4802.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4805
            
            return self._parent._cast(_4805.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4806
            
            return self._parent._cast(_4806.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4811
            
            return self._parent._cast(_4811.StraightBevelDiffGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4814
            
            return self._parent._cast(_4814.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4817
            
            return self._parent._cast(_4817.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4821
            
            return self._parent._cast(_4821.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4829
            
            return self._parent._cast(_4829.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4832
            
            return self._parent._cast(_4832.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(self) -> 'AbstractAssemblyCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4550.AbstractAssemblyModalAnalysis]':
        """List[AbstractAssemblyModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4550.AbstractAssemblyModalAnalysis]':
        """List[AbstractAssemblyModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundModalAnalysis._Cast_AbstractAssemblyCompoundModalAnalysis':
        return self._Cast_AbstractAssemblyCompoundModalAnalysis(self)
