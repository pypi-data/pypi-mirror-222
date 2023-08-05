"""_4026.py

BevelDifferentialPlanetGearPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4024
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'BevelDifferentialPlanetGearPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2499


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearPowerFlow',)


class BevelDifferentialPlanetGearPowerFlow(_4024.BevelDifferentialGearPowerFlow):
    """BevelDifferentialPlanetGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_POWER_FLOW

    class _Cast_BevelDifferentialPlanetGearPowerFlow:
        """Special nested class for casting BevelDifferentialPlanetGearPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearPowerFlow'):
            self._parent = parent

        @property
        def bevel_differential_gear_power_flow(self):
            return self._parent._cast(_4024.BevelDifferentialGearPowerFlow)

        @property
        def bevel_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4029
            
            return self._parent._cast(_4029.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4017
            
            return self._parent._cast(_4017.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4045
            
            return self._parent._cast(_4045.ConicalGearPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4072
            
            return self._parent._cast(_4072.GearPowerFlow)

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
        def bevel_differential_planet_gear_power_flow(self) -> 'BevelDifferentialPlanetGearPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2499.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialPlanetGearPowerFlow._Cast_BevelDifferentialPlanetGearPowerFlow':
        return self._Cast_BevelDifferentialPlanetGearPowerFlow(self)
