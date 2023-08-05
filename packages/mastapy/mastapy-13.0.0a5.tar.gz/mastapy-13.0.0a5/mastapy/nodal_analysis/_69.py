﻿"""_69.py

GearMeshContactStatus
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_CONTACT_STATUS = python_net_import('SMT.MastaAPI.NodalAnalysis', 'GearMeshContactStatus')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshContactStatus',)


class GearMeshContactStatus(Enum):
    """GearMeshContactStatus

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _GEAR_MESH_CONTACT_STATUS

    NO_CONTACT = 0
    LEFT_FLANK = 1
    BOTH_FLANKS = 2
    RIGHT_FLANK = -1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


GearMeshContactStatus.__setattr__ = __enum_setattr
GearMeshContactStatus.__delattr__ = __enum_delattr
