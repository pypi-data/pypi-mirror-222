"""_4110.py

ShaftHubConnectionPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4048
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ShaftHubConnectionPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.detailed_rigid_connectors.rating import _1426
    from mastapy.system_model.analyses_and_results.static_loads import _6917


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionPowerFlow',)


class ShaftHubConnectionPowerFlow(_4048.ConnectorPowerFlow):
    """ShaftHubConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_POWER_FLOW

    class _Cast_ShaftHubConnectionPowerFlow:
        """Special nested class for casting ShaftHubConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionPowerFlow'):
            self._parent = parent

        @property
        def connector_power_flow(self):
            return self._parent._cast(_4048.ConnectorPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4090
            
            return self._parent._cast(_4090.MountableComponentPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ComponentPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartPowerFlow)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_power_flow(self) -> 'ShaftHubConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2580.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1426.ShaftHubConnectionRating':
        """ShaftHubConnectionRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6917.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow':
        return self._Cast_ShaftHubConnectionPowerFlow(self)
