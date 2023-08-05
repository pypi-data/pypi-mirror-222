"""_6772.py

StaticLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StaticLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results import (
        _2628, _2623, _2603, _2614,
        _2622, _2606, _2625, _2617,
        _2607, _2624, _2605, _2611,
        _2665, _2602
    )
    from mastapy.gears import _339
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7241
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736
    from mastapy.system_model.analyses_and_results.load_case_groups import _5634, _5635, _5636
    from mastapy.system_model.analyses_and_results.static_loads import _6785


__docformat__ = 'restructuredtext en'
__all__ = ('StaticLoadCase',)


class StaticLoadCase(_6771.LoadCase):
    """StaticLoadCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_CASE

    class _Cast_StaticLoadCase:
        """Special nested class for casting StaticLoadCase to subclasses."""

        def __init__(self, parent: 'StaticLoadCase'):
            self._parent = parent

        @property
        def load_case(self):
            return self._parent._cast(_6771.LoadCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.Context)

        @property
        def parametric_study_static_load(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4365
            
            return self._parent._cast(_4365.ParametricStudyStaticLoad)

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
            
            return self._parent._cast(_5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6779
            
            return self._parent._cast(_6779.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase)

        @property
        def static_load_case(self) -> 'StaticLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StaticLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def system_deflection(self) -> '_2628.SystemDeflectionAnalysis':
        """SystemDeflectionAnalysis: 'SystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow(self) -> '_2623.PowerFlowAnalysis':
        """PowerFlowAnalysis: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_system_deflection(self) -> '_2603.AdvancedSystemDeflectionAnalysis':
        """AdvancedSystemDeflectionAnalysis: 'AdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis(self) -> '_2614.HarmonicAnalysis':
        """HarmonicAnalysis: 'HarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_study_tool(self) -> '_2622.ParametricStudyToolAnalysis':
        """ParametricStudyToolAnalysis: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_parametric_study_tool(self) -> '_2606.CompoundParametricStudyToolAnalysis':
        """CompoundParametricStudyToolAnalysis: 'CompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response(self) -> '_2625.SteadyStateSynchronousResponseAnalysis':
        """SteadyStateSynchronousResponseAnalysis: 'SteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis(self) -> '_2617.ModalAnalysis':
        """ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speed_analysis(self) -> '_2607.CriticalSpeedAnalysis':
        """CriticalSpeedAnalysis: 'CriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis(self) -> '_2624.StabilityAnalysis':
        """StabilityAnalysis: 'StabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_time_stepping_analysis_for_modulation(self) -> '_2605.AdvancedTimeSteppingAnalysisForModulation':
        """AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_model_for_modal_analysis(self) -> '_2611.DynamicModelForModalAnalysis':
        """DynamicModelForModalAnalysis: 'DynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_time(self) -> 'float':
        """float: 'CurrentTime' is the original name of this property."""

        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    def current_time(self, value: 'float'):
        self.wrapped.CurrentTime = float(value) if value is not None else 0.0

    @property
    def design_state(self) -> 'str':
        """str: 'DesignState' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignState

        if temp is None:
            return ''

        return temp

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property."""

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value is not None else 0.0

    @property
    def input_shaft_cycles(self) -> 'float':
        """float: 'InputShaftCycles' is the original name of this property."""

        temp = self.wrapped.InputShaftCycles

        if temp is None:
            return 0.0

        return temp

    @input_shaft_cycles.setter
    def input_shaft_cycles(self, value: 'float'):
        self.wrapped.InputShaftCycles = float(value) if value is not None else 0.0

    @property
    def is_stop_start_load_case(self) -> 'bool':
        """bool: 'IsStopStartLoadCase' is the original name of this property."""

        temp = self.wrapped.IsStopStartLoadCase

        if temp is None:
            return False

        return temp

    @is_stop_start_load_case.setter
    def is_stop_start_load_case(self, value: 'bool'):
        self.wrapped.IsStopStartLoadCase = bool(value) if value is not None else False

    @property
    def number_of_stop_start_cycles(self) -> 'int':
        """int: 'NumberOfStopStartCycles' is the original name of this property."""

        temp = self.wrapped.NumberOfStopStartCycles

        if temp is None:
            return 0

        return temp

    @number_of_stop_start_cycles.setter
    def number_of_stop_start_cycles(self, value: 'int'):
        self.wrapped.NumberOfStopStartCycles = int(value) if value is not None else 0

    @property
    def percentage_of_shaft_torque_alternating(self) -> 'float':
        """float: 'PercentageOfShaftTorqueAlternating' is the original name of this property."""

        temp = self.wrapped.PercentageOfShaftTorqueAlternating

        if temp is None:
            return 0.0

        return temp

    @percentage_of_shaft_torque_alternating.setter
    def percentage_of_shaft_torque_alternating(self, value: 'float'):
        self.wrapped.PercentageOfShaftTorqueAlternating = float(value) if value is not None else 0.0

    @property
    def planetary_rating_load_sharing_method(self) -> '_339.PlanetaryRatingLoadSharingOption':
        """PlanetaryRatingLoadSharingOption: 'PlanetaryRatingLoadSharingMethod' is the original name of this property."""

        temp = self.wrapped.PlanetaryRatingLoadSharingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption')
        return constructor.new_from_mastapy('mastapy.gears._339', 'PlanetaryRatingLoadSharingOption')(value) if value is not None else None

    @planetary_rating_load_sharing_method.setter
    def planetary_rating_load_sharing_method(self, value: '_339.PlanetaryRatingLoadSharingOption'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption')
        self.wrapped.PlanetaryRatingLoadSharingMethod = value

    @property
    def power_convergence_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PowerConvergenceTolerance' is the original name of this property."""

        temp = self.wrapped.PowerConvergenceTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @power_convergence_tolerance.setter
    def power_convergence_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PowerConvergenceTolerance = value

    @property
    def unbalanced_mass_inclusion(self) -> 'overridable.Overridable_UnbalancedMassInclusionOption':
        """overridable.Overridable_UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property."""

        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = overridable.Overridable_UnbalancedMassInclusionOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: 'overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()'):
        wrapper_type = overridable.Overridable_UnbalancedMassInclusionOption.wrapper_type()
        enclosed_type = overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def advanced_system_deflection_options(self) -> '_7241.AdvancedSystemDeflectionOptions':
        """AdvancedSystemDeflectionOptions: 'AdvancedSystemDeflectionOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflectionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5736.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options_for_atsam(self) -> '_5736.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptionsForATSAM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptionsForATSAM

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def te_set_up_for_dynamic_analyses_options(self) -> '_2665.TESetUpForDynamicAnalysisOptions':
        """TESetUpForDynamicAnalysisOptions: 'TESetUpForDynamicAnalysesOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TESetUpForDynamicAnalysesOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clutch_engagements(self) -> 'List[_5634.ClutchEngagementStatus]':
        """List[ClutchEngagementStatus]: 'ClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_clutch_engagements(self) -> 'List[_5635.ConceptSynchroGearEngagementStatus]':
        """List[ConceptSynchroGearEngagementStatus]: 'ConceptClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def design_state_load_case_group(self) -> '_5636.DesignState':
        """DesignState: 'DesignStateLoadCaseGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStateLoadCaseGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_of(self, analysis_type: '_6785.AnalysisType') -> '_2602.SingleAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.SingleAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType')
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_time_series_load_case(self):
        """ 'CreateTimeSeriesLoadCase' is the original name of this method."""

        self.wrapped.CreateTimeSeriesLoadCase()

    def run_power_flow(self):
        """ 'RunPowerFlow' is the original name of this method."""

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def duplicate(self, new_design_state_group: '_5636.DesignState', name: Optional['str'] = 'None') -> 'StaticLoadCase':
        """ 'Duplicate' is the original name of this method.

        Args:
            new_design_state_group (mastapy.system_model.analyses_and_results.load_case_groups.DesignState)
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase
        """

        name = str(name)
        method_result = self.wrapped.Duplicate(new_design_state_group.wrapped if new_design_state_group else None, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'StaticLoadCase._Cast_StaticLoadCase':
        return self._Cast_StaticLoadCase(self)
