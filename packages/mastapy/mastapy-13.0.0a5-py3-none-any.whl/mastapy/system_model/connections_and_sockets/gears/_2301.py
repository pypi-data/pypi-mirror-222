"""_2301.py

KlingelnbergCycloPalloidConicalGearMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.connections_and_sockets.gears import _2290
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidConicalGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMesh',)


class KlingelnbergCycloPalloidConicalGearMesh(_2290.ConicalGearMesh):
    """KlingelnbergCycloPalloidConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH

    class _Cast_KlingelnbergCycloPalloidConicalGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMesh to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMesh'):
            self._parent = parent

        @property
        def conical_gear_mesh(self):
            return self._parent._cast(_2290.ConicalGearMesh)

        @property
        def gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2296
            
            return self._parent._cast(_2296.GearMesh)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2302
            
            return self._parent._cast(_2302.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2303
            
            return self._parent._cast(_2303.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> 'KlingelnbergCycloPalloidConicalGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMesh(self)
