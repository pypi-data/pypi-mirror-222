﻿"""_1455.py

AxialLoadType
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_LOAD_TYPE = python_net_import('SMT.MastaAPI.Bolts', 'AxialLoadType')


__docformat__ = 'restructuredtext en'
__all__ = ('AxialLoadType',)


class AxialLoadType(Enum):
    """AxialLoadType

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _AXIAL_LOAD_TYPE

    DYNAMIC_AND_ECCENTRIC = 0
    DYNAMIC_AND_CONCENTRIC = 1
    STATIC_AND_ECCENTRIC = 2
    STATIC_AND_CONCENTRIC = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


AxialLoadType.__setattr__ = __enum_setattr
AxialLoadType.__delattr__ = __enum_delattr
