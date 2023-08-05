"""_4161.py

BevelGearCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BevelGearCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4029


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundPowerFlow',)


class BevelGearCompoundPowerFlow(_4149.AGMAGleasonConicalGearCompoundPowerFlow):
    """BevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_POWER_FLOW

    class _Cast_BevelGearCompoundPowerFlow:
        """Special nested class for casting BevelGearCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelGearCompoundPowerFlow'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_power_flow(self):
            return self._parent._cast(_4149.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4177
            
            return self._parent._cast(_4177.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
            
            return self._parent._cast(_4203.GearCompoundPowerFlow)

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
        def bevel_differential_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4156
            
            return self._parent._cast(_4156.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4159
            
            return self._parent._cast(_4159.BevelDifferentialPlanetGearCompoundPowerFlow)

        @property
        def bevel_differential_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4160
            
            return self._parent._cast(_4160.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
            
            return self._parent._cast(_4244.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4250
            
            return self._parent._cast(_4250.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4253
            
            return self._parent._cast(_4253.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4256
            
            return self._parent._cast(_4256.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4257
            
            return self._parent._cast(_4257.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4271
            
            return self._parent._cast(_4271.ZerolBevelGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(self) -> 'BevelGearCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4029.BevelGearPowerFlow]':
        """List[BevelGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4029.BevelGearPowerFlow]':
        """List[BevelGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearCompoundPowerFlow._Cast_BevelGearCompoundPowerFlow':
        return self._Cast_BevelGearCompoundPowerFlow(self)
