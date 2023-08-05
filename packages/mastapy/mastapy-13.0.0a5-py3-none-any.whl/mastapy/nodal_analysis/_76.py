﻿"""_76.py

MeshingDiameterForGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESHING_DIAMETER_FOR_GEAR = python_net_import('SMT.MastaAPI.NodalAnalysis', 'MeshingDiameterForGear')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshingDiameterForGear',)


class MeshingDiameterForGear(Enum):
    """MeshingDiameterForGear

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _MESHING_DIAMETER_FOR_GEAR

    ROOT_DIAMETER = 0
    TIP_DIAMETER = 1
    REFERENCE_DIAMETER = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


MeshingDiameterForGear.__setattr__ = __enum_setattr
MeshingDiameterForGear.__delattr__ = __enum_delattr
