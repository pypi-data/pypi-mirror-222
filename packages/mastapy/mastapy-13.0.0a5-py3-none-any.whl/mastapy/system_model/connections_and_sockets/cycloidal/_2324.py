"""_2324.py

RingPinsToDiscConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2264
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'RingPinsToDiscConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnection',)


class RingPinsToDiscConnection(_2264.InterMountableComponentConnection):
    """RingPinsToDiscConnection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION

    class _Cast_RingPinsToDiscConnection:
        """Special nested class for casting RingPinsToDiscConnection to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection(self):
            return self._parent._cast(_2264.InterMountableComponentConnection)

        @property
        def connection(self):
            from mastapy.system_model.connections_and_sockets import _2255
            
            return self._parent._cast(_2255.Connection)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def ring_pins_to_disc_connection(self) -> 'RingPinsToDiscConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness(self) -> 'float':
        """float: 'ContactStiffness' is the original name of this property."""

        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @contact_stiffness.setter
    def contact_stiffness(self, value: 'float'):
        self.wrapped.ContactStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'RingPinsToDiscConnection._Cast_RingPinsToDiscConnection':
        return self._Cast_RingPinsToDiscConnection(self)
