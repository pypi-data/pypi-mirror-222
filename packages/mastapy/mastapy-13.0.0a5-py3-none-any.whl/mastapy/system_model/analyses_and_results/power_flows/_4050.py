"""_4050.py

CouplingHalfPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CouplingHalfPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2566


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfPowerFlow',)


class CouplingHalfPowerFlow(_4090.MountableComponentPowerFlow):
    """CouplingHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_POWER_FLOW

    class _Cast_CouplingHalfPowerFlow:
        """Special nested class for casting CouplingHalfPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingHalfPowerFlow'):
            self._parent = parent

        @property
        def mountable_component_power_flow(self):
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
        def clutch_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
            return self._parent._cast(_4034.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4039
            
            return self._parent._cast(_4039.ConceptCouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4054
            
            return self._parent._cast(_4054.CVTPulleyPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4094
            
            return self._parent._cast(_4094.PartToPartShearCouplingHalfPowerFlow)

        @property
        def pulley_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4103
            
            return self._parent._cast(_4103.PulleyPowerFlow)

        @property
        def rolling_ring_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4108
            
            return self._parent._cast(_4108.RollingRingPowerFlow)

        @property
        def spring_damper_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4118
            
            return self._parent._cast(_4118.SpringDamperHalfPowerFlow)

        @property
        def synchroniser_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4128
            
            return self._parent._cast(_4128.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4129
            
            return self._parent._cast(_4129.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4135
            
            return self._parent._cast(_4135.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4136
            
            return self._parent._cast(_4136.TorqueConverterTurbinePowerFlow)

        @property
        def coupling_half_power_flow(self) -> 'CouplingHalfPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2566.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow':
        return self._Cast_CouplingHalfPowerFlow(self)
