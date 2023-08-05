"""_6686.py

CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6666
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis',)


class CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis(_6666.CoaxialConnectionCompoundCriticalSpeedAnalysis):
    """CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6666.CoaxialConnectionCompoundCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6739
            
            return self._parent._cast(_6739.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6645
            
            return self._parent._cast(_6645.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6677
            
            return self._parent._cast(_6677.ConnectionCompoundCriticalSpeedAnalysis)

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
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(self) -> 'CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6557.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6557.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis(self)
