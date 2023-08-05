"""_1637.py

FractionMeasurementBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRACTION_MEASUREMENT_BASE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FractionMeasurementBase')


__docformat__ = 'restructuredtext en'
__all__ = ('FractionMeasurementBase',)


class FractionMeasurementBase(_1596.MeasurementBase):
    """FractionMeasurementBase

    This is a mastapy class.
    """

    TYPE = _FRACTION_MEASUREMENT_BASE

    class _Cast_FractionMeasurementBase:
        """Special nested class for casting FractionMeasurementBase to subclasses."""

        def __init__(self, parent: 'FractionMeasurementBase'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def damage(self):
            from mastapy.utility.units_and_measurements.measurements import _1619
            
            return self._parent._cast(_1619.Damage)

        @property
        def percentage(self):
            from mastapy.utility.units_and_measurements.measurements import _1680
            
            return self._parent._cast(_1680.Percentage)

        @property
        def fraction_measurement_base(self) -> 'FractionMeasurementBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FractionMeasurementBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'FractionMeasurementBase._Cast_FractionMeasurementBase':
        return self._Cast_FractionMeasurementBase(self)
