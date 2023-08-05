"""_3748.py

AbstractShaftToMountableComponentConnectionStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'AbstractShaftToMountableComponentConnectionStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionStabilityAnalysis',)


class AbstractShaftToMountableComponentConnectionStabilityAnalysis(_3780.ConnectionStabilityAnalysis):
    """AbstractShaftToMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionStabilityAnalysis'):
            self._parent = parent

        @property
        def connection_stability_analysis(self):
            return self._parent._cast(_3780.ConnectionStabilityAnalysis)

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
        def coaxial_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3769
            
            return self._parent._cast(_3769.CoaxialConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3790
            
            return self._parent._cast(_3790.CycloidalDiscCentralBearingConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3791
            
            return self._parent._cast(_3791.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis)

        @property
        def planetary_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3829
            
            return self._parent._cast(_3829.PlanetaryConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3843
            
            return self._parent._cast(_3843.ShaftToMountableComponentConnectionStabilityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(self) -> 'AbstractShaftToMountableComponentConnectionStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis(self)
