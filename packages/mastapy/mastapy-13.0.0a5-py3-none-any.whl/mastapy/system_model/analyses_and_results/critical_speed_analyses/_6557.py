"""_6557.py

CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2318


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis',)


class CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis(_6535.CoaxialConnectionCriticalSpeedAnalysis):
    """CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_critical_speed_analysis(self):
            return self._parent._cast(_6535.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
            
            return self._parent._cast(_6610.ShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6514
            
            return self._parent._cast(_6514.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
            
            return self._parent._cast(_6546.ConnectionCriticalSpeedAnalysis)

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
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(self) -> 'CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis.TYPE'):
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
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis(self)
