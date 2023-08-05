"""_4112.py

ShaftToMountableComponentConnectionPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ShaftToMountableComponentConnectionPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionPowerFlow',)


class ShaftToMountableComponentConnectionPowerFlow(_4015.AbstractShaftToMountableComponentConnectionPowerFlow):
    """ShaftToMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW

    class _Cast_ShaftToMountableComponentConnectionPowerFlow:
        """Special nested class for casting ShaftToMountableComponentConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(self):
            return self._parent._cast(_4015.AbstractShaftToMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.ConnectionPowerFlow)

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
        def coaxial_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4036
            
            return self._parent._cast(_4036.CoaxialConnectionPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4056
            
            return self._parent._cast(_4056.CycloidalDiscCentralBearingConnectionPowerFlow)

        @property
        def planetary_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4096
            
            return self._parent._cast(_4096.PlanetaryConnectionPowerFlow)

        @property
        def shaft_to_mountable_component_connection_power_flow(self) -> 'ShaftToMountableComponentConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2278.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionPowerFlow._Cast_ShaftToMountableComponentConnectionPowerFlow':
        return self._Cast_ShaftToMountableComponentConnectionPowerFlow(self)
