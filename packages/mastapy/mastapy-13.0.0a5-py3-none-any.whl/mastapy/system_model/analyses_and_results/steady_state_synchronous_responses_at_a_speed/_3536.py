"""_3536.py

CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2509


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed',)


class CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed(_3535.CylindricalGearSteadyStateSynchronousResponseAtASpeed):
    """CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    class _Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed'):
            self._parent = parent

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(self):
            return self._parent._cast(_3535.CylindricalGearSteadyStateSynchronousResponseAtASpeed)

        @property
        def gear_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3546
            
            return self._parent._cast(_3546.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3563
            
            return self._parent._cast(_3563.MountableComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def component_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3511
            
            return self._parent._cast(_3511.ComponentSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_steady_state_synchronous_response_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3565
            
            return self._parent._cast(_3565.PartSteadyStateSynchronousResponseAtASpeed)

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
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(self) -> 'CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed':
        return self._Cast_CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed(self)
