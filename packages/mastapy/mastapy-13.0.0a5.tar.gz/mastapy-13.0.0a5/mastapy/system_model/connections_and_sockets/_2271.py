"""_2271.py

PlanetarySocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetarySocket')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetarySocket',)


class PlanetarySocket(_2272.PlanetarySocketBase):
    """PlanetarySocket

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET

    class _Cast_PlanetarySocket:
        """Special nested class for casting PlanetarySocket to subclasses."""

        def __init__(self, parent: 'PlanetarySocket'):
            self._parent = parent

        @property
        def planetary_socket_base(self):
            return self._parent._cast(_2272.PlanetarySocketBase)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def planetary_socket(self) -> 'PlanetarySocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetarySocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_tip_clearance(self) -> 'float':
        """float: 'PlanetTipClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetTipClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'PlanetarySocket._Cast_PlanetarySocket':
        return self._Cast_PlanetarySocket(self)
