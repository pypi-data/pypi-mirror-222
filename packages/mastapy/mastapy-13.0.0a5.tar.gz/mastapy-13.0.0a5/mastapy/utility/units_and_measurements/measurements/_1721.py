﻿"""_1721.py

TorquePerUnitTemperature
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_PER_UNIT_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TorquePerUnitTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('TorquePerUnitTemperature',)


class TorquePerUnitTemperature(_1596.MeasurementBase):
    """TorquePerUnitTemperature

    This is a mastapy class.
    """

    TYPE = _TORQUE_PER_UNIT_TEMPERATURE

    class _Cast_TorquePerUnitTemperature:
        """Special nested class for casting TorquePerUnitTemperature to subclasses."""

        def __init__(self, parent: 'TorquePerUnitTemperature'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def torque_per_unit_temperature(self) -> 'TorquePerUnitTemperature':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorquePerUnitTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'TorquePerUnitTemperature._Cast_TorquePerUnitTemperature':
        return self._Cast_TorquePerUnitTemperature(self)
