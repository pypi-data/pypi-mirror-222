"""_2309.py

StraightBevelDiffGearTeethSocket
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearTeethSocket',)


class StraightBevelDiffGearTeethSocket(_2287.BevelGearTeethSocket):
    """StraightBevelDiffGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET

    class _Cast_StraightBevelDiffGearTeethSocket:
        """Special nested class for casting StraightBevelDiffGearTeethSocket to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearTeethSocket'):
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
        def straight_bevel_diff_gear_teeth_socket(self) -> 'StraightBevelDiffGearTeethSocket':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StraightBevelDiffGearTeethSocket._Cast_StraightBevelDiffGearTeethSocket':
        return self._Cast_StraightBevelDiffGearTeethSocket(self)
