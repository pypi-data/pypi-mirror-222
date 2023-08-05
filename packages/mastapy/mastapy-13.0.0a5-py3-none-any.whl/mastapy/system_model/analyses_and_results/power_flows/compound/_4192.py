"""_4192.py

CylindricalGearCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CylindricalGearCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2507
    from mastapy.gears.rating.cylindrical import _453
    from mastapy.system_model.analyses_and_results.power_flows import _4061


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCompoundPowerFlow',)


class CylindricalGearCompoundPowerFlow(_4203.GearCompoundPowerFlow):
    """CylindricalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW

    class _Cast_CylindricalGearCompoundPowerFlow:
        """Special nested class for casting CylindricalGearCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'CylindricalGearCompoundPowerFlow'):
            self._parent = parent

        @property
        def gear_compound_power_flow(self):
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
        def cylindrical_planet_gear_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
            
            return self._parent._cast(_4195.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(self) -> 'CylindricalGearCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2507.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating(self) -> '_453.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_duty_cycle_rating(self) -> '_453.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'CylindricalGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4061.CylindricalGearPowerFlow]':
        """List[CylindricalGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4061.CylindricalGearPowerFlow]':
        """List[CylindricalGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow':
        return self._Cast_CylindricalGearCompoundPowerFlow(self)
