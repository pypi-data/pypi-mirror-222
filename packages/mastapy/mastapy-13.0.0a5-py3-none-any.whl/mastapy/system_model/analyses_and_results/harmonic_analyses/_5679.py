"""_5679.py

ConceptCouplingConnectionHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ConceptCouplingConnectionHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6806
    from mastapy.system_model.analyses_and_results.system_deflections import _2699


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionHarmonicAnalysis',)


class ConceptCouplingConnectionHarmonicAnalysis(_5690.CouplingConnectionHarmonicAnalysis):
    """ConceptCouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_ConceptCouplingConnectionHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(self):
            return self._parent._cast(_5690.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
            
            return self._parent._cast(_5744.InterMountableComponentConnectionHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
            
            return self._parent._cast(_5688.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(self) -> 'ConceptCouplingConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6806.ConceptCouplingConnectionLoadCase':
        """ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2699.ConceptCouplingConnectionSystemDeflection':
        """ConceptCouplingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis':
        return self._Cast_ConceptCouplingConnectionHarmonicAnalysis(self)
