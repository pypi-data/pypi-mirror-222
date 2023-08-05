﻿"""_1673.py

Mass
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Mass')


__docformat__ = 'restructuredtext en'
__all__ = ('Mass',)


class Mass(_1596.MeasurementBase):
    """Mass

    This is a mastapy class.
    """

    TYPE = _MASS

    class _Cast_Mass:
        """Special nested class for casting Mass to subclasses."""

        def __init__(self, parent: 'Mass'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def mass(self) -> 'Mass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Mass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Mass._Cast_Mass':
        return self._Cast_Mass(self)
