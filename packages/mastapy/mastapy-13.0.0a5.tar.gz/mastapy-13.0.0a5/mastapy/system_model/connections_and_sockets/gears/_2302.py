﻿"""_2302.py

KlingelnbergCycloPalloidHypoidGearMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidHypoidGearMesh')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _975


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMesh',)


class KlingelnbergCycloPalloidHypoidGearMesh(_2301.KlingelnbergCycloPalloidConicalGearMesh):
    """KlingelnbergCycloPalloidHypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH

    class _Cast_KlingelnbergCycloPalloidHypoidGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMesh to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMesh'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(self):
            return self._parent._cast(_2301.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def conical_gear_mesh(self):
            from mastapy.system_model.connections_and_sockets.gears import _2290
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> 'KlingelnbergCycloPalloidHypoidGearMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self) -> '_975.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> '_975.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'KlingelnbergCycloPalloidHypoidGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMesh(self)
