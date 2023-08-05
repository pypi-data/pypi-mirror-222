"""_2287.py

BevelGearTeethSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearTeethSocket',)


class BevelGearTeethSocket(_2283.AGMAGleasonConicalGearTeethSocket):
    """BevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_TEETH_SOCKET

    class _Cast_BevelGearTeethSocket:
        """Special nested class for casting BevelGearTeethSocket to subclasses."""

        def __init__(self, parent: 'BevelGearTeethSocket'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_teeth_socket(self):
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
        def bevel_differential_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2285
            
            return self._parent._cast(_2285.BevelDifferentialGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2307
            
            return self._parent._cast(_2307.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2309
            
            return self._parent._cast(_2309.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2311
            
            return self._parent._cast(_2311.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2315
            
            return self._parent._cast(_2315.ZerolBevelGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(self) -> 'BevelGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BevelGearTeethSocket._Cast_BevelGearTeethSocket':
        return self._Cast_BevelGearTeethSocket(self)
