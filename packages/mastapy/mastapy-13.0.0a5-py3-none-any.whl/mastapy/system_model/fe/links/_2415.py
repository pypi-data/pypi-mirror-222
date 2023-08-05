﻿"""_2415.py

SingleNodeFELink
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.fe.links import _2401
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_NODE_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'SingleNodeFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleNodeFELink',)


class SingleNodeFELink(_2401.FELink):
    """SingleNodeFELink

    This is a mastapy class.
    """

    TYPE = _SINGLE_NODE_FE_LINK

    class _Cast_SingleNodeFELink:
        """Special nested class for casting SingleNodeFELink to subclasses."""

        def __init__(self, parent: 'SingleNodeFELink'):
            self._parent = parent

        @property
        def fe_link(self):
            return self._parent._cast(_2401.FELink)

        @property
        def single_node_fe_link(self) -> 'SingleNodeFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingleNodeFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SingleNodeFELink._Cast_SingleNodeFELink':
        return self._Cast_SingleNodeFELink(self)
