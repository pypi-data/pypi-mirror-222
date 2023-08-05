"""_2384.py

NodeGroupWithSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.fe import _2360
from mastapy.nodal_analysis.component_mode_synthesis import _226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_GROUP_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'NodeGroupWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('NodeGroupWithSelection',)


class NodeGroupWithSelection(_2360.FEEntityGroupWithSelection['_226.CMSNodeGroup', int]):
    """NodeGroupWithSelection

    This is a mastapy class.
    """

    TYPE = _NODE_GROUP_WITH_SELECTION

    class _Cast_NodeGroupWithSelection:
        """Special nested class for casting NodeGroupWithSelection to subclasses."""

        def __init__(self, parent: 'NodeGroupWithSelection'):
            self._parent = parent

        @property
        def fe_entity_group_with_selection(self):
            return self._parent._cast(_2360.FEEntityGroupWithSelection)

        @property
        def node_group_with_selection(self) -> 'NodeGroupWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodeGroupWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodeGroupWithSelection._Cast_NodeGroupWithSelection':
        return self._Cast_NodeGroupWithSelection(self)
