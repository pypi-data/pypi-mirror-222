"""_2979.py

BevelDifferentialPlanetGearSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2978
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'BevelDifferentialPlanetGearSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2499


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialPlanetGearSteadyStateSynchronousResponse',)


class BevelDifferentialPlanetGearSteadyStateSynchronousResponse(_2978.BevelDifferentialGearSteadyStateSynchronousResponse):
    """BevelDifferentialPlanetGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialPlanetGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'BevelDifferentialPlanetGearSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response(self):
            return self._parent._cast(_2978.BevelDifferentialGearSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2983
            
            return self._parent._cast(_2983.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2971
            
            return self._parent._cast(_2971.AGMAGleasonConicalGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2999
            
            return self._parent._cast(_2999.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026
            
            return self._parent._cast(_3026.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
            
            return self._parent._cast(_3043.MountableComponentSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2990
            
            return self._parent._cast(_2990.ComponentSteadyStateSynchronousResponse)

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
        def bevel_differential_planet_gear_steady_state_synchronous_response(self) -> 'BevelDifferentialPlanetGearSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialPlanetGearSteadyStateSynchronousResponse.TYPE'):
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
    def cast_to(self) -> 'BevelDifferentialPlanetGearSteadyStateSynchronousResponse._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse':
        return self._Cast_BevelDifferentialPlanetGearSteadyStateSynchronousResponse(self)
