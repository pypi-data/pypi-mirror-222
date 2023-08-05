"""_1668.py

MagneticFieldStrength
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FIELD_STRENGTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagneticFieldStrength')


__docformat__ = 'restructuredtext en'
__all__ = ('MagneticFieldStrength',)


class MagneticFieldStrength(_1596.MeasurementBase):
    """MagneticFieldStrength

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FIELD_STRENGTH

    class _Cast_MagneticFieldStrength:
        """Special nested class for casting MagneticFieldStrength to subclasses."""

        def __init__(self, parent: 'MagneticFieldStrength'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def magnetic_field_strength(self) -> 'MagneticFieldStrength':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagneticFieldStrength.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MagneticFieldStrength._Cast_MagneticFieldStrength':
        return self._Cast_MagneticFieldStrength(self)
