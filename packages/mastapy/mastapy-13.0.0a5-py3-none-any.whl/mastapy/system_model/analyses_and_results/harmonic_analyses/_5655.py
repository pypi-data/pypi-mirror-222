"""_5655.py

AbstractShaftToMountableComponentConnectionHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AbstractShaftToMountableComponentConnectionHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248
    from mastapy.system_model.analyses_and_results.system_deflections import _2670


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionHarmonicAnalysis',)


class AbstractShaftToMountableComponentConnectionHarmonicAnalysis(_5688.ConnectionHarmonicAnalysis):
    """AbstractShaftToMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def connection_harmonic_analysis(self):
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
        def coaxial_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5676
            
            return self._parent._cast(_5676.CoaxialConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
            
            return self._parent._cast(_5697.CycloidalDiscCentralBearingConnectionHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5699
            
            return self._parent._cast(_5699.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis)

        @property
        def planetary_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5763
            
            return self._parent._cast(_5763.PlanetaryConnectionHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5778
            
            return self._parent._cast(_5778.ShaftToMountableComponentConnectionHarmonicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_harmonic_analysis(self) -> 'AbstractShaftToMountableComponentConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2248.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2670.AbstractShaftToMountableComponentConnectionSystemDeflection':
        """AbstractShaftToMountableComponentConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionHarmonicAnalysis._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionHarmonicAnalysis(self)
