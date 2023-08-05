"""_182.py

FEEntityGroupInteger
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.dev_tools_analyses import _181
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_INTEGER = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEEntityGroupInteger')


__docformat__ = 'restructuredtext en'
__all__ = ('FEEntityGroupInteger',)


class FEEntityGroupInteger(_181.FEEntityGroup[int]):
    """FEEntityGroupInteger

    This is a mastapy class.
    """

    TYPE = _FE_ENTITY_GROUP_INTEGER

    class _Cast_FEEntityGroupInteger:
        """Special nested class for casting FEEntityGroupInteger to subclasses."""

        def __init__(self, parent: 'FEEntityGroupInteger'):
            self._parent = parent

        @property
        def fe_entity_group(self):
            return self._parent._cast(_181.FEEntityGroup)

        @property
        def element_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _180
            
            return self._parent._cast(_180.ElementGroup)

        @property
        def node_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _199
            
            return self._parent._cast(_199.NodeGroup)

        @property
        def cms_node_group(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _226
            
            return self._parent._cast(_226.CMSNodeGroup)

        @property
        def fe_entity_group_integer(self) -> 'FEEntityGroupInteger':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEEntityGroupInteger.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FEEntityGroupInteger._Cast_FEEntityGroupInteger':
        return self._Cast_FEEntityGroupInteger(self)
