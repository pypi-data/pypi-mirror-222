﻿"""_5209.py

TorqueConverterConnectionModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5129
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'TorqueConverterConnectionModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6940


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionModalAnalysisAtASpeed',)


class TorqueConverterConnectionModalAnalysisAtASpeed(_5129.CouplingConnectionModalAnalysisAtASpeed):
    """TorqueConverterConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_TorqueConverterConnectionModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'TorqueConverterConnectionModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5129.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5157
            
            return self._parent._cast(_5157.InterMountableComponentConnectionModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5127
            
            return self._parent._cast(_5127.ConnectionModalAnalysisAtASpeed)

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
        def torque_converter_connection_modal_analysis_at_a_speed(self) -> 'TorqueConverterConnectionModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2335.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6940.TorqueConverterConnectionLoadCase':
        """TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterConnectionModalAnalysisAtASpeed._Cast_TorqueConverterConnectionModalAnalysisAtASpeed':
        return self._Cast_TorqueConverterConnectionModalAnalysisAtASpeed(self)
