﻿"""_1635.py

ForcePerUnitPressure
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_PRESSURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ForcePerUnitPressure')


__docformat__ = 'restructuredtext en'
__all__ = ('ForcePerUnitPressure',)


class ForcePerUnitPressure(_1596.MeasurementBase):
    """ForcePerUnitPressure

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_PRESSURE

    class _Cast_ForcePerUnitPressure:
        """Special nested class for casting ForcePerUnitPressure to subclasses."""

        def __init__(self, parent: 'ForcePerUnitPressure'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def force_per_unit_pressure(self) -> 'ForcePerUnitPressure':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForcePerUnitPressure.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ForcePerUnitPressure._Cast_ForcePerUnitPressure':
        return self._Cast_ForcePerUnitPressure(self)
