﻿"""_2410.py

PlanetBasedFELink
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.fe.links import _2408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_BASED_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'PlanetBasedFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetBasedFELink',)


class PlanetBasedFELink(_2408.MultiNodeFELink):
    """PlanetBasedFELink

    This is a mastapy class.
    """

    TYPE = _PLANET_BASED_FE_LINK

    class _Cast_PlanetBasedFELink:
        """Special nested class for casting PlanetBasedFELink to subclasses."""

        def __init__(self, parent: 'PlanetBasedFELink'):
            self._parent = parent

        @property
        def multi_node_fe_link(self):
            return self._parent._cast(_2408.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2401
            
            return self._parent._cast(_2401.FELink)

        @property
        def gear_with_duplicated_meshes_fe_link(self):
            from mastapy.system_model.fe.links import _2405
            
            return self._parent._cast(_2405.GearWithDuplicatedMeshesFELink)

        @property
        def planetary_connector_multi_node_fe_link(self):
            from mastapy.system_model.fe.links import _2409
            
            return self._parent._cast(_2409.PlanetaryConnectorMultiNodeFELink)

        @property
        def planet_carrier_fe_link(self):
            from mastapy.system_model.fe.links import _2411
            
            return self._parent._cast(_2411.PlanetCarrierFELink)

        @property
        def planet_based_fe_link(self) -> 'PlanetBasedFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetBasedFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlanetBasedFELink._Cast_PlanetBasedFELink':
        return self._Cast_PlanetBasedFELink(self)
