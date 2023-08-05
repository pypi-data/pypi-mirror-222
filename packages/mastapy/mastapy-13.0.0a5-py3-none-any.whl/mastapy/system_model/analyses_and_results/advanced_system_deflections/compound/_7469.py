"""_7469.py

ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7375
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7339


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection',)


class ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(_7375.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection):
    """ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(self):
            return self._parent._cast(_7375.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7407
            
            return self._parent._cast(_7407.ConnectionCompoundAdvancedSystemDeflection)

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
        def coaxial_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7396
            
            return self._parent._cast(_7396.CoaxialConnectionCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7416
            
            return self._parent._cast(_7416.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection)

        @property
        def planetary_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7455
            
            return self._parent._cast(_7455.PlanetaryConnectionCompoundAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(self) -> 'ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_7339.ShaftToMountableComponentConnectionAdvancedSystemDeflection]':
        """List[ShaftToMountableComponentConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7339.ShaftToMountableComponentConnectionAdvancedSystemDeflection]':
        """List[ShaftToMountableComponentConnectionAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection':
        return self._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(self)
