﻿"""_7001.py

CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7075
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2252
    from mastapy.system_model.analyses_and_results.static_loads import _6804
    from mastapy.system_model.analyses_and_results.system_deflections import _2696


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation',)


class CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(_7075.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation):
    """CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7075.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6976
            
            return self._parent._cast(_6976.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7012
            
            return self._parent._cast(_7012.ConnectionAdvancedTimeSteppingAnalysisForModulation)

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
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7022
            
            return self._parent._cast(_7022.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(self) -> 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
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
    def system_deflection_results(self) -> '_2696.CoaxialConnectionSystemDeflection':
        """CoaxialConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(self)
