"""_2719.py

CycloidalDiscPlanetaryBearingConnectionSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CycloidalDiscPlanetaryBearingConnectionSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2321
    from mastapy.system_model.analyses_and_results.static_loads import _6828
    from mastapy.system_model.analyses_and_results.power_flows import _4057


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionSystemDeflection',)


class CycloidalDiscPlanetaryBearingConnectionSystemDeflection(_2670.AbstractShaftToMountableComponentConnectionSystemDeflection):
    """CycloidalDiscPlanetaryBearingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_SYSTEM_DEFLECTION

    class _Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnectionSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(self):
            return self._parent._cast(_2670.AbstractShaftToMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2709
            
            return self._parent._cast(_2709.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
            return self._parent._cast(_7506.ConnectionFEAnalysis)

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
        def cycloidal_disc_planetary_bearing_connection_system_deflection(self) -> 'CycloidalDiscPlanetaryBearingConnectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2321.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6828.CycloidalDiscPlanetaryBearingConnectionLoadCase':
        """CycloidalDiscPlanetaryBearingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4057.CycloidalDiscPlanetaryBearingConnectionPowerFlow':
        """CycloidalDiscPlanetaryBearingConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnectionSystemDeflection._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection':
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionSystemDeflection(self)
