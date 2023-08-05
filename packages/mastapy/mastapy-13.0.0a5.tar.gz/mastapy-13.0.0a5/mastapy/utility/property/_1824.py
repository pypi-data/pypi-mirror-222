"""_1824.py

IListWithSelectedItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_I_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'IListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = ('IListWithSelectedItem',)


class IListWithSelectedItem:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
