﻿"""_1786.py

StatusItemSeverity
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATUS_ITEM_SEVERITY = python_net_import('SMT.MastaAPI.Utility.ModelValidation', 'StatusItemSeverity')


__docformat__ = 'restructuredtext en'
__all__ = ('StatusItemSeverity',)


class StatusItemSeverity(Enum):
    """StatusItemSeverity

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _STATUS_ITEM_SEVERITY

    HEADER = 1
    INFORMATION = 16
    WARNING = 256
    ERROR = 4096


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


StatusItemSeverity.__setattr__ = __enum_setattr
StatusItemSeverity.__delattr__ = __enum_delattr
