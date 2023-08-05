"""_6740.py

SpecialisedAssemblyCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'SpecialisedAssemblyCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6611


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundCriticalSpeedAnalysis',)


class SpecialisedAssemblyCompoundCriticalSpeedAnalysis(_6642.AbstractAssemblyCompoundCriticalSpeedAnalysis):
    """SpecialisedAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            return self._parent._cast(_6642.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6648
            
            return self._parent._cast(_6648.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6652
            
            return self._parent._cast(_6652.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6655
            
            return self._parent._cast(_6655.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6660
            
            return self._parent._cast(_6660.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6662
            
            return self._parent._cast(_6662.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6663
            
            return self._parent._cast(_6663.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6668
            
            return self._parent._cast(_6668.ConceptCouplingCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6673
            
            return self._parent._cast(_6673.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6676
            
            return self._parent._cast(_6676.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6679
            
            return self._parent._cast(_6679.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6683
            
            return self._parent._cast(_6683.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6685
            
            return self._parent._cast(_6685.CycloidalAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6691
            
            return self._parent._cast(_6691.CylindricalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6697
            
            return self._parent._cast(_6697.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6699
            
            return self._parent._cast(_6699.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6702
            
            return self._parent._cast(_6702.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6706
            
            return self._parent._cast(_6706.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6710
            
            return self._parent._cast(_6710.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6713
            
            return self._parent._cast(_6713.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6716
            
            return self._parent._cast(_6716.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6722
            
            return self._parent._cast(_6722.PartToPartShearCouplingCompoundCriticalSpeedAnalysis)

        @property
        def planetary_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6726
            
            return self._parent._cast(_6726.PlanetaryGearSetCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6733
            
            return self._parent._cast(_6733.RollingRingAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6743
            
            return self._parent._cast(_6743.SpiralBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6744
            
            return self._parent._cast(_6744.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6749
            
            return self._parent._cast(_6749.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6752
            
            return self._parent._cast(_6752.StraightBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6755
            
            return self._parent._cast(_6755.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6759
            
            return self._parent._cast(_6759.TorqueConverterCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6767
            
            return self._parent._cast(_6767.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6770
            
            return self._parent._cast(_6770.ZerolBevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self) -> 'SpecialisedAssemblyCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6611.SpecialisedAssemblyCriticalSpeedAnalysis]':
        """List[SpecialisedAssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6611.SpecialisedAssemblyCriticalSpeedAnalysis]':
        """List[SpecialisedAssemblyCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundCriticalSpeedAnalysis._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis':
        return self._Cast_SpecialisedAssemblyCompoundCriticalSpeedAnalysis(self)
