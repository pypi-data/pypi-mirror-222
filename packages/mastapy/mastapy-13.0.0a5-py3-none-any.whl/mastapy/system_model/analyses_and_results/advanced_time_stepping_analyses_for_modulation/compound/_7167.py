"""_7167.py

GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'GearSetCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7037


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class GearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7205.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation):
    """GearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_GearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'GearSetCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7205.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7107
            
            return self._parent._cast(_7107.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7186
            
            return self._parent._cast(_7186.PartCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7113
            
            return self._parent._cast(_7113.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7120
            
            return self._parent._cast(_7120.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7125
            
            return self._parent._cast(_7125.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7138
            
            return self._parent._cast(_7138.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7141
            
            return self._parent._cast(_7141.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7156
            
            return self._parent._cast(_7156.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7162
            
            return self._parent._cast(_7162.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7171
            
            return self._parent._cast(_7171.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7175
            
            return self._parent._cast(_7175.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7178
            
            return self._parent._cast(_7178.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7181
            
            return self._parent._cast(_7181.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7191
            
            return self._parent._cast(_7191.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7208
            
            return self._parent._cast(_7208.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7214
            
            return self._parent._cast(_7214.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7217
            
            return self._parent._cast(_7217.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7232
            
            return self._parent._cast(_7232.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7235
            
            return self._parent._cast(_7235.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'GearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_7037.GearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[GearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7037.GearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[GearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_GearSetCompoundAdvancedTimeSteppingAnalysisForModulation(self)
