"""_7121.py

BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6991


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation',)


class BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(_7118.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation):
    """BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7118.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7123
            
            return self._parent._cast(_7123.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7111
            
            return self._parent._cast(_7111.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7139
            
            return self._parent._cast(_7139.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7165
            
            return self._parent._cast(_7165.GearCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7184
            
            return self._parent._cast(_7184.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7132
            
            return self._parent._cast(_7132.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_6991.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6991.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(self)
