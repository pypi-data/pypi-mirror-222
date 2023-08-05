"""_5697.py

CycloidalDiscCentralBearingConnectionHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5676
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2318
    from mastapy.system_model.analyses_and_results.system_deflections import _2718


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionHarmonicAnalysis',)


class CycloidalDiscCentralBearingConnectionHarmonicAnalysis(_5676.CoaxialConnectionHarmonicAnalysis):
    """CycloidalDiscCentralBearingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_harmonic_analysis(self):
            return self._parent._cast(_5676.CoaxialConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5778
            
            return self._parent._cast(_5778.ShaftToMountableComponentConnectionHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5655
            
            return self._parent._cast(_5655.AbstractShaftToMountableComponentConnectionHarmonicAnalysis)

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
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(self) -> 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2718.CycloidalDiscCentralBearingConnectionSystemDeflection':
        """CycloidalDiscCentralBearingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionHarmonicAnalysis._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysis(self)
