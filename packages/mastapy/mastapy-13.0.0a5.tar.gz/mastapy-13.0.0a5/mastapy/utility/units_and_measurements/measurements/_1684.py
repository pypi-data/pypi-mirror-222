﻿"""_1684.py

PowerSmall
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_SMALL = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerSmall')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerSmall',)


class PowerSmall(_1596.MeasurementBase):
    """PowerSmall

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL

    class _Cast_PowerSmall:
        """Special nested class for casting PowerSmall to subclasses."""

        def __init__(self, parent: 'PowerSmall'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def power_small(self) -> 'PowerSmall':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerSmall.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PowerSmall._Cast_PowerSmall':
        return self._Cast_PowerSmall(self)
