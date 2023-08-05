﻿"""_2270.py

PlanetaryConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2278
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetaryConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnection',)


class PlanetaryConnection(_2278.ShaftToMountableComponentConnection):
    """PlanetaryConnection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION

    class _Cast_PlanetaryConnection:
        """Special nested class for casting PlanetaryConnection to subclasses."""

        def __init__(self, parent: 'PlanetaryConnection'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection(self):
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
        def planetary_connection(self) -> 'PlanetaryConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlanetaryConnection._Cast_PlanetaryConnection':
        return self._Cast_PlanetaryConnection(self)
