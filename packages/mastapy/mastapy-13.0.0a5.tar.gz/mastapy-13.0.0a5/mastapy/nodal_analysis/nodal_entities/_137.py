"""_137.py

GearMeshNodalComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.nodal_entities import _143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'GearMeshNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshNodalComponent',)


class GearMeshNodalComponent(_143.NodalComposite):
    """GearMeshNodalComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_NODAL_COMPONENT

    class _Cast_GearMeshNodalComponent:
        """Special nested class for casting GearMeshNodalComponent to subclasses."""

        def __init__(self, parent: 'GearMeshNodalComponent'):
            self._parent = parent

        @property
        def nodal_composite(self):
            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def gear_mesh_nodal_component(self) -> 'GearMeshNodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearMeshNodalComponent._Cast_GearMeshNodalComponent':
        return self._Cast_GearMeshNodalComponent(self)
