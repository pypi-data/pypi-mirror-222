"""_1696.py

QuadraticAngularDamping
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUADRATIC_ANGULAR_DAMPING = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'QuadraticAngularDamping')


__docformat__ = 'restructuredtext en'
__all__ = ('QuadraticAngularDamping',)


class QuadraticAngularDamping(_1596.MeasurementBase):
    """QuadraticAngularDamping

    This is a mastapy class.
    """

    TYPE = _QUADRATIC_ANGULAR_DAMPING

    class _Cast_QuadraticAngularDamping:
        """Special nested class for casting QuadraticAngularDamping to subclasses."""

        def __init__(self, parent: 'QuadraticAngularDamping'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def quadratic_angular_damping(self) -> 'QuadraticAngularDamping':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'QuadraticAngularDamping.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'QuadraticAngularDamping._Cast_QuadraticAngularDamping':
        return self._Cast_QuadraticAngularDamping(self)
