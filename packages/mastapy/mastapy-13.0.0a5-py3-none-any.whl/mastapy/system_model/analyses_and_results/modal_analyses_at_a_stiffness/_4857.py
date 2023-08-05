"""_4857.py

CoaxialConnectionModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CoaxialConnectionModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2252
    from mastapy.system_model.analyses_and_results.static_loads import _6804


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionModalAnalysisAtAStiffness',)


class CoaxialConnectionModalAnalysisAtAStiffness(_4931.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness):
    """CoaxialConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CoaxialConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CoaxialConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4931.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4836
            
            return self._parent._cast(_4836.AbstractShaftToMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4868
            
            return self._parent._cast(_4868.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4877
            
            return self._parent._cast(_4877.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_modal_analysis_at_a_stiffness(self) -> 'CoaxialConnectionModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2252.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6804.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CoaxialConnectionModalAnalysisAtAStiffness._Cast_CoaxialConnectionModalAnalysisAtAStiffness':
        return self._Cast_CoaxialConnectionModalAnalysisAtAStiffness(self)
