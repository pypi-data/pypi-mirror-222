"""_2285.py

BevelDifferentialGearTeethSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearTeethSocket',)


class BevelDifferentialGearTeethSocket(_2287.BevelGearTeethSocket):
    """BevelDifferentialGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_TEETH_SOCKET

    class _Cast_BevelDifferentialGearTeethSocket:
        """Special nested class for casting BevelDifferentialGearTeethSocket to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearTeethSocket'):
            self._parent = parent

        @property
        def bevel_gear_teeth_socket(self):
            return self._parent._cast(_2287.BevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2283
            
            return self._parent._cast(_2283.AGMAGleasonConicalGearTeethSocket)

        @property
        def conical_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2291
            
            return self._parent._cast(_2291.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2297
            
            return self._parent._cast(_2297.GearTeethSocket)

        @property
        def socket(self):
            from mastapy.system_model.connections_and_sockets import _2279
            
            return self._parent._cast(_2279.Socket)

        @property
        def bevel_differential_gear_teeth_socket(self) -> 'BevelDifferentialGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelDifferentialGearTeethSocket._Cast_BevelDifferentialGearTeethSocket':
        return self._Cast_BevelDifferentialGearTeethSocket(self)
