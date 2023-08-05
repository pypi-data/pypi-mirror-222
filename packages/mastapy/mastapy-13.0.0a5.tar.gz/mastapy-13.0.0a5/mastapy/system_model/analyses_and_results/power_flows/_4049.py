"""_4049.py

CouplingConnectionPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CouplingConnectionPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2329


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionPowerFlow',)


class CouplingConnectionPowerFlow(_4078.InterMountableComponentConnectionPowerFlow):
    """CouplingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_POWER_FLOW

    class _Cast_CouplingConnectionPowerFlow:
        """Special nested class for casting CouplingConnectionPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingConnectionPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(self):
            return self._parent._cast(_4078.InterMountableComponentConnectionPowerFlow)

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
        def clutch_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4033
            
            return self._parent._cast(_4033.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4038
            
            return self._parent._cast(_4038.ConceptCouplingConnectionPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4093
            
            return self._parent._cast(_4093.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def spring_damper_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4117
            
            return self._parent._cast(_4117.SpringDamperConnectionPowerFlow)

        @property
        def torque_converter_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4133
            
            return self._parent._cast(_4133.TorqueConverterConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(self) -> 'CouplingConnectionPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2329.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow':
        return self._Cast_CouplingConnectionPowerFlow(self)
