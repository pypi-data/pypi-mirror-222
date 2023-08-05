"""_5855.py

AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5883
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5658


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundHarmonicAnalysis',)


class AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(_5883.ConicalGearSetCompoundHarmonicAnalysis):
    """AGMAGleasonConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_harmonic_analysis(self):
            return self._parent._cast(_5883.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5909
            
            return self._parent._cast(_5909.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5947
            
            return self._parent._cast(_5947.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5849
            
            return self._parent._cast(_5849.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
            
            return self._parent._cast(_5928.PartCompoundHarmonicAnalysis)

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
        def bevel_differential_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5862
            
            return self._parent._cast(_5862.BevelDifferentialGearSetCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5867
            
            return self._parent._cast(_5867.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5913
            
            return self._parent._cast(_5913.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5950
            
            return self._parent._cast(_5950.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5956
            
            return self._parent._cast(_5956.StraightBevelDiffGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5959
            
            return self._parent._cast(_5959.StraightBevelGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5977
            
            return self._parent._cast(_5977.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(self) -> 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5658.AGMAGleasonConicalGearSetHarmonicAnalysis]':
        """List[AGMAGleasonConicalGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5658.AGMAGleasonConicalGearSetHarmonicAnalysis]':
        """List[AGMAGleasonConicalGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis':
        return self._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(self)
