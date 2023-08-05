"""_2277.py

ShaftSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2259
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSocket',)


class ShaftSocket(_2259.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET

    class _Cast_ShaftSocket:
        """Special nested class for casting ShaftSocket to subclasses."""

        def __init__(self, parent: 'ShaftSocket'):
            self._parent = parent

        @property
        def cylindrical_socket(self):
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def inner_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2262
            
            return self._parent._cast(_2262.InnerShaftSocket)

        @property
        def inner_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2263
            
            return self._parent._cast(_2263.InnerShaftSocketBase)

        @property
        def outer_shaft_socket(self):
            from mastapy.system_model.connections_and_sockets import _2268
            
            return self._parent._cast(_2268.OuterShaftSocket)

        @property
        def outer_shaft_socket_base(self):
            from mastapy.system_model.connections_and_sockets import _2269
            
            return self._parent._cast(_2269.OuterShaftSocketBase)

        @property
        def cycloidal_disc_axial_left_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2316
            
            return self._parent._cast(_2316.CycloidalDiscAxialLeftSocket)

        @property
        def cycloidal_disc_axial_right_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2317
            
            return self._parent._cast(_2317.CycloidalDiscAxialRightSocket)

        @property
        def cycloidal_disc_inner_socket(self):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2319
            
            return self._parent._cast(_2319.CycloidalDiscInnerSocket)

        @property
        def shaft_socket(self) -> 'ShaftSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShaftSocket._Cast_ShaftSocket':
        return self._Cast_ShaftSocket(self)
