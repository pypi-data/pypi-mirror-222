﻿"""_1702.py

SpecificHeat
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIC_HEAT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'SpecificHeat')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecificHeat',)


class SpecificHeat(_1596.MeasurementBase):
    """SpecificHeat

    This is a mastapy class.
    """

    TYPE = _SPECIFIC_HEAT

    class _Cast_SpecificHeat:
        """Special nested class for casting SpecificHeat to subclasses."""

        def __init__(self, parent: 'SpecificHeat'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def specific_heat(self) -> 'SpecificHeat':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecificHeat.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SpecificHeat._Cast_SpecificHeat':
        return self._Cast_SpecificHeat(self)
