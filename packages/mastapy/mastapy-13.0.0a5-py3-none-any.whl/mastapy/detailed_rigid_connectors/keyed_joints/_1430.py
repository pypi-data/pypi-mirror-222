﻿"""_1430.py

NumberOfKeys
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NUMBER_OF_KEYS = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints', 'NumberOfKeys')


__docformat__ = 'restructuredtext en'
__all__ = ('NumberOfKeys',)


class NumberOfKeys(Enum):
    """NumberOfKeys

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _NUMBER_OF_KEYS

    _1 = 0
    _2 = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


NumberOfKeys.__setattr__ = __enum_setattr
NumberOfKeys.__delattr__ = __enum_delattr
