"""_5771.py

RingPinsToDiscConnectionHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RingPinsToDiscConnectionHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2324
    from mastapy.system_model.analyses_and_results.static_loads import _6912
    from mastapy.system_model.analyses_and_results.system_deflections import _2777


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionHarmonicAnalysis',)


class RingPinsToDiscConnectionHarmonicAnalysis(_5744.InterMountableComponentConnectionHarmonicAnalysis):
    """RingPinsToDiscConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_RingPinsToDiscConnectionHarmonicAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
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
        def ring_pins_to_disc_connection_harmonic_analysis(self) -> 'RingPinsToDiscConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2324.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6912.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2777.RingPinsToDiscConnectionSystemDeflection':
        """RingPinsToDiscConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RingPinsToDiscConnectionHarmonicAnalysis._Cast_RingPinsToDiscConnectionHarmonicAnalysis':
        return self._Cast_RingPinsToDiscConnectionHarmonicAnalysis(self)
