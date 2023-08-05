"""_6420.py

CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis',)


class CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis(_6400.CoaxialConnectionCompoundDynamicAnalysis):
    """CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def coaxial_connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6400.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6473
            
            return self._parent._cast(_6473.ShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6379
            
            return self._parent._cast(_6379.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6411
            
            return self._parent._cast(_6411.ConnectionCompoundDynamicAnalysis)

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
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(self) -> 'CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6290.CycloidalDiscCentralBearingConnectionDynamicAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6290.CycloidalDiscCentralBearingConnectionDynamicAnalysis]':
        """List[CycloidalDiscCentralBearingConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis':
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis(self)
