"""_7501.py

AnalysisCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'AnalysisCase')

if TYPE_CHECKING:
    from mastapy.utility import _1569
    from mastapy.system_model import _2190
    from mastapy.system_model.analyses_and_results import _2633


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisCase',)


class AnalysisCase(_2632.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self, parent: 'AnalysisCase'):
            self._parent = parent

        @property
        def context(self):
            return self._parent._cast(_2632.Context)

        @property
        def system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2807
            
            return self._parent._cast(_2807.SystemDeflection)

        @property
        def torsional_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2814
            
            return self._parent._cast(_2814.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3017
            
            return self._parent._cast(_3017.DynamicModelForSteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3071
            
            return self._parent._cast(_3071.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3332
            
            return self._parent._cast(_3332.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3591
            
            return self._parent._cast(_3591.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2612
            
            return self._parent._cast(_2612.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _2624
            
            return self._parent._cast(_2624.StabilityAnalysis)

        @property
        def power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4100
            
            return self._parent._cast(_4100.PowerFlow)

        @property
        def parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4366
            
            return self._parent._cast(_4366.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2611
            
            return self._parent._cast(_2611.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _2617
            
            return self._parent._cast(_2617.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4885
            
            return self._parent._cast(_4885.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _2619
            
            return self._parent._cast(_2619.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _2618
            
            return self._parent._cast(_2618.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _2621
            
            return self._parent._cast(_2621.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2610
            
            return self._parent._cast(_2610.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2614
            
            return self._parent._cast(_2614.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _2615
            
            return self._parent._cast(_2615.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation)

        @property
        def harmonic_analysis_of_single_excitation(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6040
            
            return self._parent._cast(_6040.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _2620
            
            return self._parent._cast(_2620.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _2608
            
            return self._parent._cast(_2608.DynamicAnalysis)

        @property
        def critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _2607
            
            return self._parent._cast(_2607.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _2605
            
            return self._parent._cast(_2605.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7240
            
            return self._parent._cast(_7240.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7242
            
            return self._parent._cast(_7242.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7503
            
            return self._parent._cast(_7503.CompoundAnalysisCase)

        @property
        def fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.FEAnalysis)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7516
            
            return self._parent._cast(_7516.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7517
            
            return self._parent._cast(_7517.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self) -> 'AnalysisCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self) -> 'float':
        """float: 'AnalysisSetupTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self) -> 'str':
        """str: 'LoadCaseName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ''

        return temp

    @property
    def analysis_run_information(self) -> '_1569.AnalysisRunInformation':
        """AnalysisRunInformation: 'AnalysisRunInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_ready(self) -> 'bool':
        """bool: 'ResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    def results_for(self, design_entity: '_2190.DesignEntity') -> '_2633.DesignEntityAnalysis':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        """

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_analysis(self):
        """ 'PerformAnalysis' is the original name of this method."""

        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self) -> 'AnalysisCase._Cast_AnalysisCase':
        return self._Cast_AnalysisCase(self)
