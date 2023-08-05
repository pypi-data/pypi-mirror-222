"""_4046.py

ConicalGearSetPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConicalGearSetPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2506


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetPowerFlow',)


class ConicalGearSetPowerFlow(_4073.GearSetPowerFlow):
    """ConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_POWER_FLOW

    class _Cast_ConicalGearSetPowerFlow:
        """Special nested class for casting ConicalGearSetPowerFlow to subclasses."""

        def __init__(self, parent: 'ConicalGearSetPowerFlow'):
            self._parent = parent

        @property
        def gear_set_power_flow(self):
            return self._parent._cast(_4073.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4012
            
            return self._parent._cast(_4012.AbstractAssemblyPowerFlow)

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
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4018
            
            return self._parent._cast(_4018.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4025
            
            return self._parent._cast(_4025.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4030
            
            return self._parent._cast(_4030.BevelGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4125
            
            return self._parent._cast(_4125.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4144
            
            return self._parent._cast(_4144.ZerolBevelGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(self) -> 'ConicalGearSetPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2506.ConicalGearSet':
        """ConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow':
        return self._Cast_ConicalGearSetPowerFlow(self)
