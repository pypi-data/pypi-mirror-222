"""_3001.py

ConnectorSteadyStateSynchronousResponse
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3043
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ConnectorSteadyStateSynchronousResponse')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2430


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorSteadyStateSynchronousResponse',)


class ConnectorSteadyStateSynchronousResponse(_3043.MountableComponentSteadyStateSynchronousResponse):
    """ConnectorSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE

    class _Cast_ConnectorSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectorSteadyStateSynchronousResponse to subclasses."""

        def __init__(self, parent: 'ConnectorSteadyStateSynchronousResponse'):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(self):
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
        def bearing_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2973
            
            return self._parent._cast(_2973.BearingSteadyStateSynchronousResponse)

        @property
        def oil_seal_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3044
            
            return self._parent._cast(_3044.OilSealSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3061
            
            return self._parent._cast(_3061.ShaftHubConnectionSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(self) -> 'ConnectorSteadyStateSynchronousResponse':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2430.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConnectorSteadyStateSynchronousResponse._Cast_ConnectorSteadyStateSynchronousResponse':
        return self._Cast_ConnectorSteadyStateSynchronousResponse(self)
