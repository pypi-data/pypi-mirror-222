"""_6144.py

ConnectorCompoundHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConnectorCompoundHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6014


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundHarmonicAnalysisOfSingleExcitation',)


class ConnectorCompoundHarmonicAnalysisOfSingleExcitation(_6185.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation):
    """ConnectorCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_ConnectorCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ConnectorCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6185.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def component_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6133
            
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
        def bearing_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6116
            
            return self._parent._cast(_6116.BearingCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6186
            
            return self._parent._cast(_6186.OilSealCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6204
            
            return self._parent._cast(_6204.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation)

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(self) -> 'ConnectorCompoundHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6014.ConnectorHarmonicAnalysisOfSingleExcitation]':
        """List[ConnectorHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6014.ConnectorHarmonicAnalysisOfSingleExcitation]':
        """List[ConnectorHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundHarmonicAnalysisOfSingleExcitation._Cast_ConnectorCompoundHarmonicAnalysisOfSingleExcitation':
        return self._Cast_ConnectorCompoundHarmonicAnalysisOfSingleExcitation(self)
