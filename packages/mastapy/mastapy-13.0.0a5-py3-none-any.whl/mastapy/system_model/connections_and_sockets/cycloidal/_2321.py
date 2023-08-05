"""_2321.py

CycloidalDiscPlanetaryBearingConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2248
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscPlanetaryBearingConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnection',)


class CycloidalDiscPlanetaryBearingConnection(_2248.AbstractShaftToMountableComponentConnection):
    """CycloidalDiscPlanetaryBearingConnection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION

    class _Cast_CycloidalDiscPlanetaryBearingConnection:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnection to subclasses."""

        def __init__(self, parent: 'CycloidalDiscPlanetaryBearingConnection'):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            return self._parent._cast(_2248.AbstractShaftToMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2255
            
            return self._parent._cast(_2255.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def cycloidal_disc_planetary_bearing_connection(self) -> 'CycloidalDiscPlanetaryBearingConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CycloidalDiscPlanetaryBearingConnection._Cast_CycloidalDiscPlanetaryBearingConnection':
        return self._Cast_CycloidalDiscPlanetaryBearingConnection(self)
