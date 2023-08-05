"""_146.py

RigidBar
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.nodal_entities import _142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_BAR = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'RigidBar')


__docformat__ = 'restructuredtext en'
__all__ = ('RigidBar',)


class RigidBar(_142.NodalComponent):
    """RigidBar

    This is a mastapy class.
    """

    TYPE = _RIGID_BAR

    class _Cast_RigidBar:
        """Special nested class for casting RigidBar to subclasses."""

        def __init__(self, parent: 'RigidBar'):
            self._parent = parent

        @property
        def nodal_component(self):
            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def rigid_bar(self) -> 'RigidBar':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidBar.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RigidBar._Cast_RigidBar':
        return self._Cast_RigidBar(self)
