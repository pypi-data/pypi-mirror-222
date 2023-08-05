﻿"""_1715.py

TimeVeryShort
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TIME_VERY_SHORT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TimeVeryShort')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeVeryShort',)


class TimeVeryShort(_1596.MeasurementBase):
    """TimeVeryShort

    This is a mastapy class.
    """

    TYPE = _TIME_VERY_SHORT

    class _Cast_TimeVeryShort:
        """Special nested class for casting TimeVeryShort to subclasses."""

        def __init__(self, parent: 'TimeVeryShort'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def time_very_short(self) -> 'TimeVeryShort':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TimeVeryShort.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TimeVeryShort._Cast_TimeVeryShort':
        return self._Cast_TimeVeryShort(self)
