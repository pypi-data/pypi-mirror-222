"""_4146.py

AbstractShaftCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'AbstractShaftCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4014


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundPowerFlow',)


class AbstractShaftCompoundPowerFlow(_4147.AbstractShaftOrHousingCompoundPowerFlow):
    """AbstractShaftCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_POWER_FLOW

    class _Cast_AbstractShaftCompoundPowerFlow:
        """Special nested class for casting AbstractShaftCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_power_flow(self):
            return self._parent._cast(_4147.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4170
            
            return self._parent._cast(_4170.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4224
            
            return self._parent._cast(_4224.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4190
            
            return self._parent._cast(_4190.CycloidalDiscCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
            
            return self._parent._cast(_4240.ShaftCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(self) -> 'AbstractShaftCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4014.AbstractShaftPowerFlow]':
        """List[AbstractShaftPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4014.AbstractShaftPowerFlow]':
        """List[AbstractShaftPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundPowerFlow._Cast_AbstractShaftCompoundPowerFlow':
        return self._Cast_AbstractShaftCompoundPowerFlow(self)
