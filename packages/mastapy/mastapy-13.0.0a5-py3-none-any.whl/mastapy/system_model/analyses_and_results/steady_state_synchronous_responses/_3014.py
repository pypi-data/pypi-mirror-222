"""_3014.py

CylindricalGearSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3026
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CylindricalGearSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2507
    from mastapy.system_model.analyses_and_results.static_loads import _6829


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSteadyStateSynchronousResponse',)


class CylindricalGearSteadyStateSynchronousResponse(_3026.GearSteadyStateSynchronousResponse):
    """CylindricalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_CylindricalGearSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'CylindricalGearSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response(self):
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
        def cylindrical_planet_gear_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3015
            
            return self._parent._cast(_3015.CylindricalPlanetGearSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_steady_state_synchronous_response(self) -> 'CylindricalGearSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSteadyStateSynchronousResponse.TYPE'):
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
    def component_load_case(self) -> '_6829.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearSteadyStateSynchronousResponse]':
        """List[CylindricalGearSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse':
        return self._Cast_CylindricalGearSteadyStateSynchronousResponse(self)
