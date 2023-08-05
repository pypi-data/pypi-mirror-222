"""_4748.py

CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4595


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundModalAnalysis',)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysis(_4728.CoaxialConnectionCompoundModalAnalysis):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis(self):
            return self._parent._cast(_4728.CoaxialConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
            
            return self._parent._cast(_4801.ShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4707
            
            return self._parent._cast(_4707.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
            
            return self._parent._cast(_4739.ConnectionCompoundModalAnalysis)

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
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4595.CycloidalDiscCentralBearingConnectionModalAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4595.CycloidalDiscCentralBearingConnectionModalAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis(self)
