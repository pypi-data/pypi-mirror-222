"""_2305.py

KlingelnbergSpiralBevelGearTeethSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_SPIRAL_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergSpiralBevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergSpiralBevelGearTeethSocket',)


class KlingelnbergSpiralBevelGearTeethSocket(_2300.KlingelnbergConicalGearTeethSocket):
    """KlingelnbergSpiralBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_SPIRAL_BEVEL_GEAR_TEETH_SOCKET

    class _Cast_KlingelnbergSpiralBevelGearTeethSocket:
        """Special nested class for casting KlingelnbergSpiralBevelGearTeethSocket to subclasses."""

        def __init__(self, parent: 'KlingelnbergSpiralBevelGearTeethSocket'):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_teeth_socket(self):
            return self._parent._cast(_2300.KlingelnbergConicalGearTeethSocket)

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
        def klingelnberg_spiral_bevel_gear_teeth_socket(self) -> 'KlingelnbergSpiralBevelGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergSpiralBevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergSpiralBevelGearTeethSocket._Cast_KlingelnbergSpiralBevelGearTeethSocket':
        return self._Cast_KlingelnbergSpiralBevelGearTeethSocket(self)
