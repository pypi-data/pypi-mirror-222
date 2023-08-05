"""_2933.py

SpecialisedAssemblyCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'SpecialisedAssemblyCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2788


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundSystemDeflection',)


class SpecialisedAssemblyCompoundSystemDeflection(_2833.AbstractAssemblyCompoundSystemDeflection):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundSystemDeflection'):
            self._parent = parent

        @property
        def abstract_assembly_compound_system_deflection(self):
            return self._parent._cast(_2833.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
            
            return self._parent._cast(_2913.PartCompoundSystemDeflection)

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
        def agma_gleason_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2839
            
            return self._parent._cast(_2839.AGMAGleasonConicalGearSetCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2843
            
            return self._parent._cast(_2843.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2846
            
            return self._parent._cast(_2846.BevelDifferentialGearSetCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2851
            
            return self._parent._cast(_2851.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2853
            
            return self._parent._cast(_2853.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
            
            return self._parent._cast(_2854.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2859
            
            return self._parent._cast(_2859.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
            
            return self._parent._cast(_2864.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
            
            return self._parent._cast(_2867.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2870
            
            return self._parent._cast(_2870.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
            
            return self._parent._cast(_2874.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
            
            return self._parent._cast(_2876.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2882
            
            return self._parent._cast(_2882.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2889
            
            return self._parent._cast(_2889.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2891
            
            return self._parent._cast(_2891.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
            
            return self._parent._cast(_2894.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2898
            
            return self._parent._cast(_2898.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2902
            
            return self._parent._cast(_2902.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2905
            
            return self._parent._cast(_2905.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
            
            return self._parent._cast(_2908.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2914
            
            return self._parent._cast(_2914.PartToPartShearCouplingCompoundSystemDeflection)

        @property
        def planetary_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2918
            
            return self._parent._cast(_2918.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2925
            
            return self._parent._cast(_2925.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2936
            
            return self._parent._cast(_2936.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
            
            return self._parent._cast(_2937.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2942
            
            return self._parent._cast(_2942.StraightBevelDiffGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2945
            
            return self._parent._cast(_2945.StraightBevelGearSetCompoundSystemDeflection)

        @property
        def synchroniser_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2948
            
            return self._parent._cast(_2948.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
            
            return self._parent._cast(_2952.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2960
            
            return self._parent._cast(_2960.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2963
            
            return self._parent._cast(_2963.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self) -> 'SpecialisedAssemblyCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2788.SpecialisedAssemblySystemDeflection]':
        """List[SpecialisedAssemblySystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2788.SpecialisedAssemblySystemDeflection]':
        """List[SpecialisedAssemblySystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection':
        return self._Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
