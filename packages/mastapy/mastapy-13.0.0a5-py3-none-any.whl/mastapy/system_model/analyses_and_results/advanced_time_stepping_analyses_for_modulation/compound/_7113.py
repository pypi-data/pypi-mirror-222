"""_7113.py

AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6982


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7141.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    """AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7141.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7167
            
            return self._parent._cast(_7167.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7205
            
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
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7120
            
            return self._parent._cast(_7120.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7125
            
            return self._parent._cast(_7125.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7171
            
            return self._parent._cast(_7171.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7235
            
            return self._parent._cast(_7235.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_6982.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6982.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(self)
