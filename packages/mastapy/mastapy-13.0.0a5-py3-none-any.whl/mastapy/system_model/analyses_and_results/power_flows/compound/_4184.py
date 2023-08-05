"""_4184.py

CouplingHalfCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CouplingHalfCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4050


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundPowerFlow',)


class CouplingHalfCompoundPowerFlow(_4222.MountableComponentCompoundPowerFlow):
    """CouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_POWER_FLOW

    class _Cast_CouplingHalfCompoundPowerFlow:
        """Special nested class for casting CouplingHalfCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingHalfCompoundPowerFlow'):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(self):
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
        def clutch_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4168
            
            return self._parent._cast(_4168.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4173
            
            return self._parent._cast(_4173.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4187
            
            return self._parent._cast(_4187.CVTPulleyCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
            
            return self._parent._cast(_4227.PartToPartShearCouplingHalfCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
            
            return self._parent._cast(_4233.PulleyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4237
            
            return self._parent._cast(_4237.RollingRingCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
            
            return self._parent._cast(_4249.SpringDamperHalfCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4259
            
            return self._parent._cast(_4259.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4260
            
            return self._parent._cast(_4260.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4261
            
            return self._parent._cast(_4261.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4264
            
            return self._parent._cast(_4264.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4265
            
            return self._parent._cast(_4265.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(self) -> 'CouplingHalfCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4050.CouplingHalfPowerFlow]':
        """List[CouplingHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4050.CouplingHalfPowerFlow]':
        """List[CouplingHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow':
        return self._Cast_CouplingHalfCompoundPowerFlow(self)
