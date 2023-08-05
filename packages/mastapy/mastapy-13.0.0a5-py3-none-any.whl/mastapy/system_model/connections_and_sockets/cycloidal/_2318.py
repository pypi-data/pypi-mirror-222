﻿"""_2318.py

CycloidalDiscCentralBearingConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2252
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscCentralBearingConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnection',)


class CycloidalDiscCentralBearingConnection(_2252.CoaxialConnection):
    """CycloidalDiscCentralBearingConnection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION

    class _Cast_CycloidalDiscCentralBearingConnection:
        """Special nested class for casting CycloidalDiscCentralBearingConnection to subclasses."""

        def __init__(self, parent: 'CycloidalDiscCentralBearingConnection'):
            self._parent = parent

        @property
        def coaxial_connection(self):
            return self._parent._cast(_2252.CoaxialConnection)

        @property
        def shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2278
            
            return self._parent._cast(_2278.ShaftToMountableComponentConnection)

        @property
        def abstract_shaft_to_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2248
            
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
        def cycloidal_disc_central_bearing_connection(self) -> 'CycloidalDiscCentralBearingConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection':
        return self._Cast_CycloidalDiscCentralBearingConnection(self)
