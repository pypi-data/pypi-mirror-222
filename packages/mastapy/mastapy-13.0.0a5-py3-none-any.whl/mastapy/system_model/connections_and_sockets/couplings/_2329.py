"""_2329.py

CouplingConnection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets import _2264
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnection',)


class CouplingConnection(_2264.InterMountableComponentConnection):
    """CouplingConnection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION

    class _Cast_CouplingConnection:
        """Special nested class for casting CouplingConnection to subclasses."""

        def __init__(self, parent: 'CouplingConnection'):
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
        def clutch_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2325
            
            return self._parent._cast(_2325.ClutchConnection)

        @property
        def concept_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2327
            
            return self._parent._cast(_2327.ConceptCouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2331
            
            return self._parent._cast(_2331.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2333
            
            return self._parent._cast(_2333.SpringDamperConnection)

        @property
        def torque_converter_connection(self):
            from mastapy.system_model.connections_and_sockets.couplings import _2335
            
            return self._parent._cast(_2335.TorqueConverterConnection)

        @property
        def coupling_connection(self) -> 'CouplingConnection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CouplingConnection._Cast_CouplingConnection':
        return self._Cast_CouplingConnection(self)
