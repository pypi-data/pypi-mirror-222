"""_5890.py

CVTCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5859
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'CVTCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5694


__docformat__ = 'restructuredtext en'
__all__ = ('CVTCompoundHarmonicAnalysis',)


class CVTCompoundHarmonicAnalysis(_5859.BeltDriveCompoundHarmonicAnalysis):
    """CVTCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_CVTCompoundHarmonicAnalysis:
        """Special nested class for casting CVTCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CVTCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def belt_drive_compound_harmonic_analysis(self):
            return self._parent._cast(_5859.BeltDriveCompoundHarmonicAnalysis)

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
        def cvt_compound_harmonic_analysis(self) -> 'CVTCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5694.CVTHarmonicAnalysis]':
        """List[CVTHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5694.CVTHarmonicAnalysis]':
        """List[CVTHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTCompoundHarmonicAnalysis._Cast_CVTCompoundHarmonicAnalysis':
        return self._Cast_CVTCompoundHarmonicAnalysis(self)
