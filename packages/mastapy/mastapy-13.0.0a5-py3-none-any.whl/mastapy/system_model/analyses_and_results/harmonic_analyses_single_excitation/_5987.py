"""_5987.py

BeltConnectionHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6044
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BeltConnectionHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2251
    from mastapy.system_model.analyses_and_results.static_loads import _6788


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionHarmonicAnalysisOfSingleExcitation',)


class BeltConnectionHarmonicAnalysisOfSingleExcitation(_6044.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation):
    """BeltConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'BeltConnectionHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6044.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6013
            
            return self._parent._cast(_6013.ConnectionHarmonicAnalysisOfSingleExcitation)

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
        def cvt_belt_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6018
            
            return self._parent._cast(_6018.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_connection_harmonic_analysis_of_single_excitation(self) -> 'BeltConnectionHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2251.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6788.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltConnectionHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation':
        return self._Cast_BeltConnectionHarmonicAnalysisOfSingleExcitation(self)
