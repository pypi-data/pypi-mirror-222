﻿"""_2262.py

InnerShaftSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2263
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SHAFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InnerShaftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerShaftSocket',)


class InnerShaftSocket(_2263.InnerShaftSocketBase):
    """InnerShaftSocket

    This is a mastapy class.
    """

    TYPE = _INNER_SHAFT_SOCKET

    class _Cast_InnerShaftSocket:
        """Special nested class for casting InnerShaftSocket to subclasses."""

        def __init__(self, parent: 'InnerShaftSocket'):
            self._parent = parent

        @property
        def inner_shaft_socket_base(self):
            return self._parent._cast(_2263.InnerShaftSocketBase)

        @property
        def shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2277
            
            return self._parent._cast(_2277.ShaftSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def inner_shaft_socket(self) -> 'InnerShaftSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InnerShaftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InnerShaftSocket._Cast_InnerShaftSocket':
        return self._Cast_InnerShaftSocket(self)
