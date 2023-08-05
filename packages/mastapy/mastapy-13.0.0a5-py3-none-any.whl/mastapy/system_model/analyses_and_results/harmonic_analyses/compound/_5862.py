"""_5862.py

BevelDifferentialGearSetCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'BevelDifferentialGearSetCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2498
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5665
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5860, _5861


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundHarmonicAnalysis',)


class BevelDifferentialGearSetCompoundHarmonicAnalysis(_5867.BevelGearSetCompoundHarmonicAnalysis):
    """BevelDifferentialGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_harmonic_analysis(self):
            return self._parent._cast(_5867.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5855
            
            return self._parent._cast(_5855.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5883
            
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
        def bevel_differential_gear_set_compound_harmonic_analysis(self) -> 'BevelDifferentialGearSetCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundHarmonicAnalysis.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_5665.BevelDifferentialGearSetHarmonicAnalysis]':
        """List[BevelDifferentialGearSetHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_compound_harmonic_analysis(self) -> 'List[_5860.BevelDifferentialGearCompoundHarmonicAnalysis]':
        """List[BevelDifferentialGearCompoundHarmonicAnalysis]: 'BevelDifferentialGearsCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_compound_harmonic_analysis(self) -> 'List[_5861.BevelDifferentialGearMeshCompoundHarmonicAnalysis]':
        """List[BevelDifferentialGearMeshCompoundHarmonicAnalysis]: 'BevelDifferentialMeshesCompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesCompoundHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5665.BevelDifferentialGearSetHarmonicAnalysis]':
        """List[BevelDifferentialGearSetHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetCompoundHarmonicAnalysis._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis':
        return self._Cast_BevelDifferentialGearSetCompoundHarmonicAnalysis(self)
