"""_3224.py

ZerolBevelGearCompoundSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3114
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'ZerolBevelGearCompoundSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3097


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearCompoundSteadyStateSynchronousResponse',)


class ZerolBevelGearCompoundSteadyStateSynchronousResponse(_3114.BevelGearCompoundSteadyStateSynchronousResponse):
    """ZerolBevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ZerolBevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ZerolBevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearCompoundSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def bevel_gear_compound_steady_state_synchronous_response(self):
            return self._parent._cast(_3114.BevelGearCompoundSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3102
            
            return self._parent._cast(_3102.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def conical_gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130
            
            return self._parent._cast(_3130.ConicalGearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3156
            
            return self._parent._cast(_3156.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3175
            
            return self._parent._cast(_3175.MountableComponentCompoundSteadyStateSynchronousResponse)

        @property
        def component_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3123
            
            return self._parent._cast(_3123.ComponentCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3177
            
            return self._parent._cast(_3177.PartCompoundSteadyStateSynchronousResponse)

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
        def zerol_bevel_gear_compound_steady_state_synchronous_response(self) -> 'ZerolBevelGearCompoundSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2535.ZerolBevelGear':
        """ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3097.ZerolBevelGearSteadyStateSynchronousResponse]':
        """List[ZerolBevelGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3097.ZerolBevelGearSteadyStateSynchronousResponse]':
        """List[ZerolBevelGearSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearCompoundSteadyStateSynchronousResponse._Cast_ZerolBevelGearCompoundSteadyStateSynchronousResponse':
        return self._Cast_ZerolBevelGearCompoundSteadyStateSynchronousResponse(self)
