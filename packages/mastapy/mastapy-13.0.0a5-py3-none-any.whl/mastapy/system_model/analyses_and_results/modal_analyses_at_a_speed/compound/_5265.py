﻿"""_5265.py

CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5245
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5136


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed',)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed(_5245.CoaxialConnectionCompoundModalAnalysisAtASpeed):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5245.CoaxialConnectionCompoundModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5318
            
            return self._parent._cast(_5318.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5224
            
            return self._parent._cast(_5224.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5256
            
            return self._parent._cast(_5256.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5136.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5136.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed(self)
