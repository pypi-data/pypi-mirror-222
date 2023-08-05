"""_2327.py

ConceptCouplingConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.couplings import _2329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnection',)


class ConceptCouplingConnection(_2329.CouplingConnection):
    """ConceptCouplingConnection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION

    class _Cast_ConceptCouplingConnection:
        """Special nested class for casting ConceptCouplingConnection to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnection'):
            self._parent = parent

        @property
        def coupling_connection(self):
            return self._parent._cast(_2329.CouplingConnection)

        @property
        def inter_mountable_component_connection(self):
            from mastapy.system_model.connections_and_sockets import _2264
            
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
        def concept_coupling_connection(self) -> 'ConceptCouplingConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptCouplingConnection._Cast_ConceptCouplingConnection':
        return self._Cast_ConceptCouplingConnection(self)
