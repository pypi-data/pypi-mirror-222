"""_2328.py

ConceptCouplingSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.couplings import _2330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingSocket',)


class ConceptCouplingSocket(_2330.CouplingSocket):
    """ConceptCouplingSocket

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_SOCKET

    class _Cast_ConceptCouplingSocket:
        """Special nested class for casting ConceptCouplingSocket to subclasses."""

        def __init__(self, parent: 'ConceptCouplingSocket'):
            self._parent = parent

        @property
        def coupling_socket(self):
            return self._parent._cast(_2330.CouplingSocket)

        @property
        def cylindrical_socket(self):
            from mastapy.system_model.connections_and_sockets import _2259
            
            return self._parent._cast(_2259.CylindricalSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def concept_coupling_socket(self) -> 'ConceptCouplingSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptCouplingSocket._Cast_ConceptCouplingSocket':
        return self._Cast_ConceptCouplingSocket(self)
