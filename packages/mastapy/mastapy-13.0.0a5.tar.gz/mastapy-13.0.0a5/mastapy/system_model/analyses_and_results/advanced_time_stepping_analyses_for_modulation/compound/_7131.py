﻿"""_7131.py

CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7204
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2252
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7001


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation',)


class CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(_7204.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation):
    """CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7204.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7110
            
            return self._parent._cast(_7110.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7142
            
            return self._parent._cast(_7142.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

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
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7151
            
            return self._parent._cast(_7151.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2252.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def connection_analysis_cases_ready(self) -> 'List[_7001.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation]':
        """List[CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_7001.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation]':
        """List[CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(self)
