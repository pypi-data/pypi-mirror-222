﻿"""_746.py

ActiveProfileRangeCalculationSource
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_PROFILE_RANGE_CALCULATION_SOURCE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ActiveProfileRangeCalculationSource')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveProfileRangeCalculationSource',)


class ActiveProfileRangeCalculationSource(Enum):
    """ActiveProfileRangeCalculationSource

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _ACTIVE_PROFILE_RANGE_CALCULATION_SOURCE

    DESIGNED_GEAR_WITHOUT_TOLERANCES = 0
    MANUFACTURED_GEAR_WITH_TOLERANCES = 1


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ActiveProfileRangeCalculationSource.__setattr__ = __enum_setattr
ActiveProfileRangeCalculationSource.__delattr__ = __enum_delattr
