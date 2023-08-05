"""_7120.py

BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2498
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6990
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7118, _7119


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7125.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    """BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7125.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7113
            
            return self._parent._cast(_7113.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7141
            
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
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6990.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7118.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation]: 'BevelDifferentialGearsCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsCompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7119.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]: 'BevelDifferentialMeshesCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesCompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6990.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(self)
