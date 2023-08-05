"""_780.py

ConicalMeshFlankNURBSMicroGeometryConfig
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.bevel import _779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshFlankNURBSMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFlankNURBSMicroGeometryConfig',)


class ConicalMeshFlankNURBSMicroGeometryConfig(_779.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankNURBSMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalMeshFlankNURBSMicroGeometryConfig:
        """Special nested class for casting ConicalMeshFlankNURBSMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshFlankNURBSMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_mesh_flank_micro_geometry_config(self):
            return self._parent._cast(_779.ConicalMeshFlankMicroGeometryConfig)

        @property
        def conical_mesh_flank_nurbs_micro_geometry_config(self) -> 'ConicalMeshFlankNURBSMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshFlankNURBSMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshFlankNURBSMicroGeometryConfig._Cast_ConicalMeshFlankNURBSMicroGeometryConfig':
        return self._Cast_ConicalMeshFlankNURBSMicroGeometryConfig(self)
