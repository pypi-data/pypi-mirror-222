﻿"""_5633.py

AbstractStaticLoadCaseGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'AbstractStaticLoadCaseGroup')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import (
        _5642, _5643, _5631, _5641
    )
    from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5646, _5649, _5650
    from mastapy.system_model.part_model import (
        _2422, _2436, _2454, _2455
    )
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6787, _6829, _6831, _6833,
        _6855, _6906, _6907, _6772,
        _6785
    )
    from mastapy.system_model.part_model.gears import _2508, _2507
    from mastapy.system_model.connections_and_sockets.gears import _2292
    from mastapy.system_model.analyses_and_results.power_flows.compound import _4194
    from mastapy.system_model.analyses_and_results import (
        _2663, _2658, _2640, _2650,
        _2660, _2653, _2643, _2659,
        _2642, _2647, _2601
    )


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractStaticLoadCaseGroup',)


class AbstractStaticLoadCaseGroup(_5632.AbstractLoadCaseGroup):
    """AbstractStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STATIC_LOAD_CASE_GROUP

    class _Cast_AbstractStaticLoadCaseGroup:
        """Special nested class for casting AbstractStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'AbstractStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def abstract_load_case_group(self):
            return self._parent._cast(_5632.AbstractLoadCaseGroup)

        @property
        def abstract_design_state_load_case_group(self):
            return self._parent._cast(_5631.AbstractDesignStateLoadCaseGroup)

        @property
        def design_state(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5636
            
            return self._parent._cast(_5636.DesignState)

        @property
        def duty_cycle(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5637
            
            return self._parent._cast(_5637.DutyCycle)

        @property
        def sub_group_in_single_design_state(self):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5640
            
            return self._parent._cast(_5640.SubGroupInSingleDesignState)

        @property
        def abstract_static_load_case_group(self) -> 'AbstractStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_optimisation(self) -> '_5642.SystemOptimiserGearSetOptimisation':
        """SystemOptimiserGearSetOptimisation: 'GearSetOptimisation' is the original name of this property."""

        temp = self.wrapped.GearSetOptimisation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserGearSetOptimisation')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.load_case_groups._5642', 'SystemOptimiserGearSetOptimisation')(value) if value is not None else None

    @gear_set_optimisation.setter
    def gear_set_optimisation(self, value: '_5642.SystemOptimiserGearSetOptimisation'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserGearSetOptimisation')
        self.wrapped.GearSetOptimisation = value

    @property
    def max_number_of_load_cases_to_display(self) -> 'int':
        """int: 'MaxNumberOfLoadCasesToDisplay' is the original name of this property."""

        temp = self.wrapped.MaxNumberOfLoadCasesToDisplay

        if temp is None:
            return 0

        return temp

    @max_number_of_load_cases_to_display.setter
    def max_number_of_load_cases_to_display(self, value: 'int'):
        self.wrapped.MaxNumberOfLoadCasesToDisplay = int(value) if value is not None else 0

    @property
    def number_of_configurations_to_create(self) -> 'int':
        """int: 'NumberOfConfigurationsToCreate' is the original name of this property."""

        temp = self.wrapped.NumberOfConfigurationsToCreate

        if temp is None:
            return 0

        return temp

    @number_of_configurations_to_create.setter
    def number_of_configurations_to_create(self, value: 'int'):
        self.wrapped.NumberOfConfigurationsToCreate = int(value) if value is not None else 0

    @property
    def number_of_possible_system_designs(self) -> 'int':
        """int: 'NumberOfPossibleSystemDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPossibleSystemDesigns

        if temp is None:
            return 0

        return temp

    @property
    def optimum_tooth_numbers_target(self) -> '_5643.SystemOptimiserTargets':
        """SystemOptimiserTargets: 'OptimumToothNumbersTarget' is the original name of this property."""

        temp = self.wrapped.OptimumToothNumbersTarget

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserTargets')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.load_case_groups._5643', 'SystemOptimiserTargets')(value) if value is not None else None

    @optimum_tooth_numbers_target.setter
    def optimum_tooth_numbers_target(self, value: '_5643.SystemOptimiserTargets'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserTargets')
        self.wrapped.OptimumToothNumbersTarget = value

    @property
    def system_optimiser_log(self) -> 'str':
        """str: 'SystemOptimiserLog' is the original name of this property."""

        temp = self.wrapped.SystemOptimiserLog

        if temp is None:
            return ''

        return temp

    @system_optimiser_log.setter
    def system_optimiser_log(self, value: 'str'):
        self.wrapped.SystemOptimiserLog = str(value) if value is not None else ''

    @property
    def bearings(self) -> 'List[_5646.ComponentStaticLoadCaseGroup[_2422.Bearing, _6787.BearingLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[Bearing, BearingLoadCase]]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5649.GearSetStaticLoadCaseGroup[_2508.CylindricalGearSet, _2507.CylindricalGear, _6829.CylindricalGearLoadCase, _2292.CylindricalGearMesh, _6831.CylindricalGearMeshLoadCase, _6833.CylindricalGearSetLoadCase]]':
        """List[GearSetStaticLoadCaseGroup[CylindricalGearSet, CylindricalGear, CylindricalGearLoadCase, CylindricalGearMesh, CylindricalGearMeshLoadCase, CylindricalGearSetLoadCase]]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def design_states(self) -> 'List[_5631.AbstractDesignStateLoadCaseGroup]':
        """List[AbstractDesignStateLoadCaseGroup]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_5646.ComponentStaticLoadCaseGroup[_2436.FEPart, _6855.FEPartLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[FEPart, FEPartLoadCase]]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def loaded_gear_sets(self) -> 'List[_4194.CylindricalGearSetCompoundPowerFlow]':
        """List[CylindricalGearSetCompoundPowerFlow]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def parts_with_excitations(self) -> 'List[_5650.PartStaticLoadCaseGroup]':
        """List[PartStaticLoadCaseGroup]: 'PartsWithExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartsWithExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_5646.ComponentStaticLoadCaseGroup[_2454.PointLoad, _6906.PointLoadLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[PointLoad, PointLoadLoadCase]]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_5646.ComponentStaticLoadCaseGroup[_2455.PowerLoad, _6907.PowerLoadLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[PowerLoad, PowerLoadLoadCase]]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def static_loads(self) -> 'List[_6772.StaticLoadCase]':
        """List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def static_loads_limited_by_max_number_of_load_cases_to_display(self) -> 'List[_6772.StaticLoadCase]':
        """List[StaticLoadCase]: 'StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_optimisation_gear_sets(self) -> 'List[_5641.SystemOptimisationGearSet]':
        """List[SystemOptimisationGearSet]: 'SystemOptimisationGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemOptimisationGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def compound_system_deflection(self) -> '_2663.CompoundSystemDeflectionAnalysis':
        """CompoundSystemDeflectionAnalysis: 'CompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_power_flow(self) -> '_2658.CompoundPowerFlowAnalysis':
        """CompoundPowerFlowAnalysis: 'CompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundPowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_advanced_system_deflection(self) -> '_2640.CompoundAdvancedSystemDeflectionAnalysis':
        """CompoundAdvancedSystemDeflectionAnalysis: 'CompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundAdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_harmonic_analysis(self) -> '_2650.CompoundHarmonicAnalysis':
        """CompoundHarmonicAnalysis: 'CompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundHarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_steady_state_synchronous_response(self) -> '_2660.CompoundSteadyStateSynchronousResponseAnalysis':
        """CompoundSteadyStateSynchronousResponseAnalysis: 'CompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_modal_analysis(self) -> '_2653.CompoundModalAnalysis':
        """CompoundModalAnalysis: 'CompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_critical_speed_analysis(self) -> '_2643.CompoundCriticalSpeedAnalysis':
        """CompoundCriticalSpeedAnalysis: 'CompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_stability_analysis(self) -> '_2659.CompoundStabilityAnalysis':
        """CompoundStabilityAnalysis: 'CompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(self) -> '_2642.CompoundAdvancedTimeSteppingAnalysisForModulation':
        """CompoundAdvancedTimeSteppingAnalysisForModulation: 'CompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_dynamic_model_for_modal_analysis(self) -> '_2647.CompoundDynamicModelForModalAnalysis':
        """CompoundDynamicModelForModalAnalysis: 'CompoundDynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundDynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def calculate_candidates(self):
        """ 'CalculateCandidates' is the original name of this method."""

        self.wrapped.CalculateCandidates()

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        """ 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method."""

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    def create_designs(self):
        """ 'CreateDesigns' is the original name of this method."""

        self.wrapped.CreateDesigns()

    def optimise_gear_sets_quick(self):
        """ 'OptimiseGearSetsQuick' is the original name of this method."""

        self.wrapped.OptimiseGearSetsQuick()

    def perform_system_optimisation(self):
        """ 'PerformSystemOptimisation' is the original name of this method."""

        self.wrapped.PerformSystemOptimisation()

    def run_power_flow(self):
        """ 'RunPowerFlow' is the original name of this method."""

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def analysis_of(self, analysis_type: '_6785.AnalysisType') -> '_2601.CompoundAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.CompoundAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType')
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup':
        return self._Cast_AbstractStaticLoadCaseGroup(self)
