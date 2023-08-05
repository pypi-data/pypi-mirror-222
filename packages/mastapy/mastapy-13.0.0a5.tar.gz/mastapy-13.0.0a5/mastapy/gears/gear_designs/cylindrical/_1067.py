﻿"""_1067.py

ScuffingCoefficientOfFrictionMethods
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCUFFING_COEFFICIENT_OF_FRICTION_METHODS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ScuffingCoefficientOfFrictionMethods')


__docformat__ = 'restructuredtext en'
__all__ = ('ScuffingCoefficientOfFrictionMethods',)


class ScuffingCoefficientOfFrictionMethods(Enum):
    """ScuffingCoefficientOfFrictionMethods

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _SCUFFING_COEFFICIENT_OF_FRICTION_METHODS

    USERDEFINED_CONSTANT = 0
    CALCULATED_CONSTANT = 1
    CALCULATED_VARIABLE = 2


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ScuffingCoefficientOfFrictionMethods.__setattr__ = __enum_setattr
ScuffingCoefficientOfFrictionMethods.__delattr__ = __enum_delattr
