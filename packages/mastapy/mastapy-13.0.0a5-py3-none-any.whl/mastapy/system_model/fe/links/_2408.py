﻿"""_2408.py

MultiNodeFELink
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.fe.links import _2401
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'MultiNodeFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiNodeFELink',)


class MultiNodeFELink(_2401.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_FE_LINK

    class _Cast_MultiNodeFELink:
        """Special nested class for casting MultiNodeFELink to subclasses."""

        def __init__(self, parent: 'MultiNodeFELink'):
            self._parent = parent

        @property
        def fe_link(self):
            return self._parent._cast(_2401.FELink)

        @property
        def electric_machine_stator_fe_link(self):
            from mastapy.system_model.fe.links import _2402
            
            return self._parent._cast(_2402.ElectricMachineStatorFELink)

        @property
        def gear_mesh_fe_link(self):
            from mastapy.system_model.fe.links import _2404
            
            return self._parent._cast(_2404.GearMeshFELink)

        @property
        def gear_with_duplicated_meshes_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.GearWithDuplicatedMeshesFELink)

        @property
        def multi_angle_connection_fe_link(self):
            from mastapy.system_model.fe.links import _2406
            
            return self._parent._cast(_2406.MultiAngleConnectionFELink)

        @property
        def multi_node_connector_fe_link(self):
            from mastapy.system_model.fe.links import _2407
            
            return self._parent._cast(_2407.MultiNodeConnectorFELink)

        @property
        def planetary_connector_multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2409
            
            return self._parent._cast(_2409.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_based_fe_link(self):
            from mastapy.system_model.fe.links import _2410
            
            return self._parent._cast(_2410.PlanetBasedFELink)

        @property
        def planet_carrier_fe_link(self):
            from mastapy.system_model.fe.links import _2411
            
            return self._parent._cast(_2411.PlanetCarrierFELink)

        @property
        def point_load_fe_link(self):
            from mastapy.system_model.fe.links import _2412
            
            return self._parent._cast(_2412.PointLoadFELink)

        @property
        def rolling_ring_connection_fe_link(self):
            from mastapy.system_model.fe.links import _2413
            
            return self._parent._cast(_2413.RollingRingConnectionFELink)

        @property
        def shaft_hub_connection_fe_link(self):
            from mastapy.system_model.fe.links import _2414
            
            return self._parent._cast(_2414.ShaftHubConnectionFELink)

        @property
        def multi_node_fe_link(self) -> 'MultiNodeFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MultiNodeFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MultiNodeFELink._Cast_MultiNodeFELink':
        return self._Cast_MultiNodeFELink(self)
