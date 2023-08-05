﻿"""_1687.py

PowerSmallPerUnitAreaPerUnitTime
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_UNIT_AREA_PER_UNIT_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerSmallPerUnitAreaPerUnitTime')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerSmallPerUnitAreaPerUnitTime',)


class PowerSmallPerUnitAreaPerUnitTime(_1596.MeasurementBase):
    """PowerSmallPerUnitAreaPerUnitTime

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_UNIT_AREA_PER_UNIT_TIME

    class _Cast_PowerSmallPerUnitAreaPerUnitTime:
        """Special nested class for casting PowerSmallPerUnitAreaPerUnitTime to subclasses."""

        def __init__(self, parent: 'PowerSmallPerUnitAreaPerUnitTime'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def power_small_per_unit_area_per_unit_time(self) -> 'PowerSmallPerUnitAreaPerUnitTime':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerSmallPerUnitAreaPerUnitTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PowerSmallPerUnitAreaPerUnitTime._Cast_PowerSmallPerUnitAreaPerUnitTime':
        return self._Cast_PowerSmallPerUnitAreaPerUnitTime(self)
