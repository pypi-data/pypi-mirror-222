﻿"""_2836.py

AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2868
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AbstractShaftToMountableComponentConnectionCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2670


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundSystemDeflection',)


class AbstractShaftToMountableComponentConnectionCompoundSystemDeflection(_2868.ConnectionCompoundSystemDeflection):
    """AbstractShaftToMountableComponentConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundSystemDeflection'):
            self._parent = parent

        @property
        def connection_compound_system_deflection(self):
            return self._parent._cast(_2868.ConnectionCompoundSystemDeflection)

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
        def coaxial_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2857
            
            return self._parent._cast(_2857.CoaxialConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2877
            
            return self._parent._cast(_2877.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879
            
            return self._parent._cast(_2879.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection)

        @property
        def planetary_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2917
            
            return self._parent._cast(_2917.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2932
            
            return self._parent._cast(_2932.ShaftToMountableComponentConnectionCompoundSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(self) -> 'AbstractShaftToMountableComponentConnectionCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2670.AbstractShaftToMountableComponentConnectionSystemDeflection]':
        """List[AbstractShaftToMountableComponentConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2670.AbstractShaftToMountableComponentConnectionSystemDeflection]':
        """List[AbstractShaftToMountableComponentConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundSystemDeflection':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundSystemDeflection(self)
