"""_4259.py

SynchroniserHalfCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4260
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SynchroniserHalfCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.power_flows import _4128


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundPowerFlow',)


class SynchroniserHalfCompoundPowerFlow(_4260.SynchroniserPartCompoundPowerFlow):
    """SynchroniserHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_POWER_FLOW

    class _Cast_SynchroniserHalfCompoundPowerFlow:
        """Special nested class for casting SynchroniserHalfCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'SynchroniserHalfCompoundPowerFlow'):
            self._parent = parent

        @property
        def synchroniser_part_compound_power_flow(self):
            return self._parent._cast(_4260.SynchroniserPartCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4184
            
            return self._parent._cast(_4184.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
            
            return self._parent._cast(_4222.MountableComponentCompoundPowerFlow)

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
        def synchroniser_half_compound_power_flow(self) -> 'SynchroniserHalfCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2586.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4128.SynchroniserHalfPowerFlow]':
        """List[SynchroniserHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4128.SynchroniserHalfPowerFlow]':
        """List[SynchroniserHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserHalfCompoundPowerFlow._Cast_SynchroniserHalfCompoundPowerFlow':
        return self._Cast_SynchroniserHalfCompoundPowerFlow(self)
