"""_3029.py

HypoidGearSetSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2970
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'HypoidGearSetSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.static_loads import _6875
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3030, _3028


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSteadyStateSynchronousResponse',)


class HypoidGearSetSteadyStateSynchronousResponse(_2970.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse):
    """HypoidGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_HypoidGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'HypoidGearSetSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(self):
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
        def hypoid_gear_set_steady_state_synchronous_response(self) -> 'HypoidGearSetSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2517.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6875.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears_steady_state_synchronous_response(self) -> 'List[_3030.HypoidGearSteadyStateSynchronousResponse]':
        """List[HypoidGearSteadyStateSynchronousResponse]: 'HypoidGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_steady_state_synchronous_response(self) -> 'List[_3028.HypoidGearMeshSteadyStateSynchronousResponse]':
        """List[HypoidGearMeshSteadyStateSynchronousResponse]: 'HypoidMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetSteadyStateSynchronousResponse._Cast_HypoidGearSetSteadyStateSynchronousResponse':
        return self._Cast_HypoidGearSetSteadyStateSynchronousResponse(self)
