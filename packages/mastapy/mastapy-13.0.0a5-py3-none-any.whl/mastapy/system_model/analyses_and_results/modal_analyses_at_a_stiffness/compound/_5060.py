"""_5060.py

ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4966
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4931


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness',)


class ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(_4966.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness):
    """ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4966.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4998
            
            return self._parent._cast(_4998.ConnectionCompoundModalAnalysisAtAStiffness)

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
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4987
            
            return self._parent._cast(_4987.CoaxialConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5007
            
            return self._parent._cast(_5007.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5046
            
            return self._parent._cast(_5046.PlanetaryConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self) -> 'ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4931.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]':
        """List[ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4931.ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]':
        """List[ShaftToMountableComponentConnectionModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness':
        return self._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness(self)
