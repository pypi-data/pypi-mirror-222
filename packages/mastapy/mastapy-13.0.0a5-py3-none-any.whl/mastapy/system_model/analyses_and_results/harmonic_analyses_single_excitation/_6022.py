"""_6022.py

CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2318


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation',)


class CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(_6002.CoaxialConnectionHarmonicAnalysisOfSingleExcitation):
    """CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    class _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation'):
            self._parent = parent

        @property
        def coaxial_connection_harmonic_analysis_of_single_excitation(self):
            return self._parent._cast(_6002.CoaxialConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6076
            
            return self._parent._cast(_6076.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5981
            
            return self._parent._cast(_5981.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation)

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
        def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(self) -> 'CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2318.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation':
        return self._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(self)
