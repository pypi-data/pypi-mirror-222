"""_2265.py

MountableComponentInnerSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_INNER_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'MountableComponentInnerSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentInnerSocket',)


class MountableComponentInnerSocket(_2267.MountableComponentSocket):
    """MountableComponentInnerSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_INNER_SOCKET

    class _Cast_MountableComponentInnerSocket:
        """Special nested class for casting MountableComponentInnerSocket to subclasses."""

        def __init__(self, parent: 'MountableComponentInnerSocket'):
            self._parent = parent

        @property
        def mountable_component_socket(self):
            return self._parent._cast(_2267.MountableComponentSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def bearing_inner_socket(self):
            from mastapy.system_model.connections_and_sockets import _2249
            
            return self._parent._cast(_2249.BearingInnerSocket)

        @property
        def mountable_component_inner_socket(self) -> 'MountableComponentInnerSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentInnerSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MountableComponentInnerSocket._Cast_MountableComponentInnerSocket':
        return self._Cast_MountableComponentInnerSocket(self)
