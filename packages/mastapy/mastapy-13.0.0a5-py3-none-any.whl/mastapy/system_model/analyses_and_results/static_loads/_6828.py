﻿"""_6828.py

CycloidalDiscPlanetaryBearingConnectionLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CycloidalDiscPlanetaryBearingConnectionLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2321


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionLoadCase',)


class CycloidalDiscPlanetaryBearingConnectionLoadCase(_6777.AbstractShaftToMountableComponentConnectionLoadCase):
    """CycloidalDiscPlanetaryBearingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE

    class _Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnectionLoadCase'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(self):
            return self._parent._cast(_6777.AbstractShaftToMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6817
            
            return self._parent._cast(_6817.ConnectionLoadCase)

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
        def cycloidal_disc_planetary_bearing_connection_load_case(self) -> 'CycloidalDiscPlanetaryBearingConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionLoadCase.TYPE'):
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
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnectionLoadCase._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase':
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionLoadCase(self)
