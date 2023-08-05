"""_5943.py

RootAssemblyCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5856
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'RootAssemblyCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5775


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundHarmonicAnalysis',)


class RootAssemblyCompoundHarmonicAnalysis(_5856.AssemblyCompoundHarmonicAnalysis):
    """RootAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_RootAssemblyCompoundHarmonicAnalysis:
        """Special nested class for casting RootAssemblyCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def assembly_compound_harmonic_analysis(self):
            return self._parent._cast(_5856.AssemblyCompoundHarmonicAnalysis)

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
        def root_assembly_compound_harmonic_analysis(self) -> 'RootAssemblyCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5775.RootAssemblyHarmonicAnalysis]':
        """List[RootAssemblyHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5775.RootAssemblyHarmonicAnalysis]':
        """List[RootAssemblyHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundHarmonicAnalysis._Cast_RootAssemblyCompoundHarmonicAnalysis':
        return self._Cast_RootAssemblyCompoundHarmonicAnalysis(self)
