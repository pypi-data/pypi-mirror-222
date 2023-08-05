"""_6169.py

GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6133
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2438
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6039


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation',)


class GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation(_6133.ComponentCompoundHarmonicAnalysisOfSingleExcitation):
    """GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6133.ComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def part_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6187
            
            return self._parent._cast(_6187.PartCompoundHarmonicAnalysisOfSingleExcitation)

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
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(self) -> 'GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2438.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6039.GuideDxfModelHarmonicAnalysisOfSingleExcitation]':
        """List[GuideDxfModelHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6039.GuideDxfModelHarmonicAnalysisOfSingleExcitation]':
        """List[GuideDxfModelHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation(self)
