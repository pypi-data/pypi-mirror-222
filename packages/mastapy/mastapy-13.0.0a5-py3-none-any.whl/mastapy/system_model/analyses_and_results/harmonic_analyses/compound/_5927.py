"""_5927.py

OilSealCompoundHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'OilSealCompoundHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5757


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCompoundHarmonicAnalysis',)


class OilSealCompoundHarmonicAnalysis(_5885.ConnectorCompoundHarmonicAnalysis):
    """OilSealCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS

    class _Cast_OilSealCompoundHarmonicAnalysis:
        """Special nested class for casting OilSealCompoundHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'OilSealCompoundHarmonicAnalysis'):
            self._parent = parent

        @property
        def connector_compound_harmonic_analysis(self):
            return self._parent._cast(_5885.ConnectorCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5926
            
            return self._parent._cast(_5926.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5874
            
            return self._parent._cast(_5874.ComponentCompoundHarmonicAnalysis)

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
        def oil_seal_compound_harmonic_analysis(self) -> 'OilSealCompoundHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OilSealCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5757.OilSealHarmonicAnalysis]':
        """List[OilSealHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5757.OilSealHarmonicAnalysis]':
        """List[OilSealHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'OilSealCompoundHarmonicAnalysis._Cast_OilSealCompoundHarmonicAnalysis':
        return self._Cast_OilSealCompoundHarmonicAnalysis(self)
