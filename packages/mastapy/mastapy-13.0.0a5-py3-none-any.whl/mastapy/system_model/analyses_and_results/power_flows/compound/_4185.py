"""_4185.py

CVTBeltConnectionCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4154
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CVTBeltConnectionCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4052


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundPowerFlow',)


class CVTBeltConnectionCompoundPowerFlow(_4154.BeltConnectionCompoundPowerFlow):
    """CVTBeltConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_POWER_FLOW

    class _Cast_CVTBeltConnectionCompoundPowerFlow:
        """Special nested class for casting CVTBeltConnectionCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundPowerFlow'):
            self._parent = parent

        @property
        def belt_connection_compound_power_flow(self):
            return self._parent._cast(_4154.BeltConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
            
            return self._parent._cast(_4210.InterMountableComponentConnectionCompoundPowerFlow)

        @property
        def connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
            
            return self._parent._cast(_4180.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_power_flow(self) -> 'CVTBeltConnectionCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4052.CVTBeltConnectionPowerFlow]':
        """List[CVTBeltConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4052.CVTBeltConnectionPowerFlow]':
        """List[CVTBeltConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundPowerFlow._Cast_CVTBeltConnectionCompoundPowerFlow':
        return self._Cast_CVTBeltConnectionCompoundPowerFlow(self)
