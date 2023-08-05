"""_1705.py

Stress
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRESS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Stress')


__docformat__ = 'restructuredtext en'
__all__ = ('Stress',)


class Stress(_1596.MeasurementBase):
    """Stress

    This is a mastapy class.
    """

    TYPE = _STRESS

    class _Cast_Stress:
        """Special nested class for casting Stress to subclasses."""

        def __init__(self, parent: 'Stress'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def pressure(self):
            from mastapy.utility.units_and_measurements.measurements import _1690
            
            return self._parent._cast(_1690.Pressure)

        @property
        def stress(self) -> 'Stress':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Stress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Stress._Cast_Stress':
        return self._Cast_Stress(self)
