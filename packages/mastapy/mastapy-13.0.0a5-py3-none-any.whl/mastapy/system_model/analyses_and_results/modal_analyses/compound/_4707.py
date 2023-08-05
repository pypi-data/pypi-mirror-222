"""_4707.py

AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4553


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundModalAnalysis',)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(_4739.ConnectionCompoundModalAnalysis):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysis'):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(self):
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
        def coaxial_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
            
            return self._parent._cast(_4728.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4748
            
            return self._parent._cast(_4748.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4750
            
            return self._parent._cast(_4750.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis)

        @property
        def planetary_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4787
            
            return self._parent._cast(_4787.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
            
            return self._parent._cast(_4801.ShaftToMountableComponentConnectionCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(self) -> 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4553.AbstractShaftToMountableComponentConnectionModalAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4553.AbstractShaftToMountableComponentConnectionModalAnalysis]':
        """List[AbstractShaftToMountableComponentConnectionModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(self)
