"""_136.py

FrictionNodalComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.nodal_entities import _142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRICTION_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'FrictionNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('FrictionNodalComponent',)


class FrictionNodalComponent(_142.NodalComponent):
    """FrictionNodalComponent

    This is a mastapy class.
    """

    TYPE = _FRICTION_NODAL_COMPONENT

    class _Cast_FrictionNodalComponent:
        """Special nested class for casting FrictionNodalComponent to subclasses."""

        def __init__(self, parent: 'FrictionNodalComponent'):
            self._parent = parent

        @property
        def nodal_component(self):
            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def friction_nodal_component(self) -> 'FrictionNodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FrictionNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FrictionNodalComponent._Cast_FrictionNodalComponent':
        return self._Cast_FrictionNodalComponent(self)
