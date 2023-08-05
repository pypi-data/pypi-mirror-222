"""_2283.py

AGMAGleasonConicalGearTeethSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2291
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'AGMAGleasonConicalGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearTeethSocket',)


class AGMAGleasonConicalGearTeethSocket(_2291.ConicalGearTeethSocket):
    """AGMAGleasonConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET

    class _Cast_AGMAGleasonConicalGearTeethSocket:
        """Special nested class for casting AGMAGleasonConicalGearTeethSocket to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearTeethSocket'):
            self._parent = parent

        @property
        def conical_gear_teeth_socket(self):
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
        def bevel_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2287
            
            return self._parent._cast(_2287.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(self):
            from mastapy.system_model.connections_and_sockets.gears import _2299
            
            return self._parent._cast(_2299.HypoidGearTeethSocket)

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
        def agma_gleason_conical_gear_teeth_socket(self) -> 'AGMAGleasonConicalGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket':
        return self._Cast_AGMAGleasonConicalGearTeethSocket(self)
