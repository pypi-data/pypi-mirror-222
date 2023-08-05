﻿"""_673.py

HobManufactureError
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOB_MANUFACTURE_ERROR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobManufactureError')


__docformat__ = 'restructuredtext en'
__all__ = ('HobManufactureError',)


class HobManufactureError(_686.RackManufactureError):
    """HobManufactureError

    This is a mastapy class.
    """

    TYPE = _HOB_MANUFACTURE_ERROR

    class _Cast_HobManufactureError:
        """Special nested class for casting HobManufactureError to subclasses."""

        def __init__(self, parent: 'HobManufactureError'):
            self._parent = parent

        @property
        def rack_manufacture_error(self):
            return self._parent._cast(_686.RackManufactureError)

        @property
        def hob_manufacture_error(self) -> 'HobManufactureError':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobManufactureError.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_relief_variation(self) -> 'float':
        """float: 'TotalReliefVariation' is the original name of this property."""

        temp = self.wrapped.TotalReliefVariation

        if temp is None:
            return 0.0

        return temp

    @total_relief_variation.setter
    def total_relief_variation(self, value: 'float'):
        self.wrapped.TotalReliefVariation = float(value) if value is not None else 0.0

    @property
    def use_sin_curve_for_top_relief(self) -> 'bool':
        """bool: 'UseSinCurveForTopRelief' is the original name of this property."""

        temp = self.wrapped.UseSinCurveForTopRelief

        if temp is None:
            return False

        return temp

    @use_sin_curve_for_top_relief.setter
    def use_sin_curve_for_top_relief(self, value: 'bool'):
        self.wrapped.UseSinCurveForTopRelief = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'HobManufactureError._Cast_HobManufactureError':
        return self._Cast_HobManufactureError(self)
