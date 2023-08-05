"""_3096.py

ZerolBevelGearSetSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ZerolBevelGearSetSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6955
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3097, _3095


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetSteadyStateSynchronousResponse',)


class ZerolBevelGearSetSteadyStateSynchronousResponse(_2982.BevelGearSetSteadyStateSynchronousResponse):
    """ZerolBevelGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ZerolBevelGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting ZerolBevelGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearSetSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(self):
            return self._parent._cast(_2982.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2970
            
            return self._parent._cast(_2970.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2998
            
            return self._parent._cast(_2998.ConicalGearSetSteadyStateSynchronousResponse)

        @property
        def gear_set_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3025
            
            return self._parent._cast(_3025.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3064
            
            return self._parent._cast(_3064.SpecialisedAssemblySteadyStateSynchronousResponse)

        @property
        def abstract_assembly_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2965
            
            return self._parent._cast(_2965.AbstractAssemblySteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3045
            
            return self._parent._cast(_3045.PartSteadyStateSynchronousResponse)

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
        def zerol_bevel_gear_set_steady_state_synchronous_response(self) -> 'ZerolBevelGearSetSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2536.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6955.ZerolBevelGearSetLoadCase':
        """ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears_steady_state_synchronous_response(self) -> 'List[_3097.ZerolBevelGearSteadyStateSynchronousResponse]':
        """List[ZerolBevelGearSteadyStateSynchronousResponse]: 'ZerolBevelGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_steady_state_synchronous_response(self) -> 'List[_3095.ZerolBevelGearMeshSteadyStateSynchronousResponse]':
        """List[ZerolBevelGearMeshSteadyStateSynchronousResponse]: 'ZerolBevelMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse':
        return self._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse(self)
