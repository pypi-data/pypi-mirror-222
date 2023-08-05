﻿"""_1654.py

KinematicViscosity
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.utility.units_and_measurements import _1596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KINEMATIC_VISCOSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'KinematicViscosity')


__docformat__ = 'restructuredtext en'
__all__ = ('KinematicViscosity',)


class KinematicViscosity(_1596.MeasurementBase):
    """KinematicViscosity

    This is a mastapy class.
    """

    TYPE = _KINEMATIC_VISCOSITY

    class _Cast_KinematicViscosity:
        """Special nested class for casting KinematicViscosity to subclasses."""

        def __init__(self, parent: 'KinematicViscosity'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1596.MeasurementBase)

        @property
        def kinematic_viscosity(self) -> 'KinematicViscosity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KinematicViscosity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KinematicViscosity._Cast_KinematicViscosity':
        return self._Cast_KinematicViscosity(self)
