﻿"""_4219.py

KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.power_flows import _4087
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4217, _4218


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow',)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow(_4213.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(self):
            return self._parent._cast(_4213.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4179
            
            return self._parent._cast(_4179.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
            
            return self._parent._cast(_4205.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4145
            
            return self._parent._cast(_4145.AbstractAssemblyCompoundPowerFlow)

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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2523.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2523.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4087.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_power_flow(self) -> 'List[_4217.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow]: 'KlingelnbergCycloPalloidSpiralBevelGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_power_flow(self) -> 'List[_4218.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow]: 'KlingelnbergCycloPalloidSpiralBevelMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4087.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow(self)
