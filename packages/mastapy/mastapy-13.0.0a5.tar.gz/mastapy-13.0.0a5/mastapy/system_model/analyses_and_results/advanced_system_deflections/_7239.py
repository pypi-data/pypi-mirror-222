"""_7239.py

AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7274
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection',)


class AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(_7274.ConnectionAdvancedSystemDeflection):
    """AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(self):
            return self._parent._cast(_7274.ConnectionAdvancedSystemDeflection)

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
        def coaxial_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7263
            
            return self._parent._cast(_7263.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7285
            
            return self._parent._cast(_7285.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7286
            
            return self._parent._cast(_7286.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection)

        @property
        def planetary_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7325
            
            return self._parent._cast(_7325.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7339
            
            return self._parent._cast(_7339.ShaftToMountableComponentConnectionAdvancedSystemDeflection)

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(self) -> 'AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2248.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection':
        return self._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(self)
