﻿"""_2179.py

PlainJournalHousing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_JOURNAL_HOUSING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainJournalHousing')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1930


__docformat__ = 'restructuredtext en'
__all__ = ('PlainJournalHousing',)


class PlainJournalHousing(_0.APIBase):
    """PlainJournalHousing

    This is a mastapy class.
    """

    TYPE = _PLAIN_JOURNAL_HOUSING

    class _Cast_PlainJournalHousing:
        """Special nested class for casting PlainJournalHousing to subclasses."""

        def __init__(self, parent: 'PlainJournalHousing'):
            self._parent = parent

        @property
        def cylindrical_housing_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2172
            
            return self._parent._cast(_2172.CylindricalHousingJournalBearing)

        @property
        def machinery_encased_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2173
            
            return self._parent._cast(_2173.MachineryEncasedJournalBearing)

        @property
        def pedestal_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2175
            
            return self._parent._cast(_2175.PedestalJournalBearing)

        @property
        def plain_journal_housing(self) -> 'PlainJournalHousing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlainJournalHousing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def heat_emitting_area(self) -> 'float':
        """float: 'HeatEmittingArea' is the original name of this property."""

        temp = self.wrapped.HeatEmittingArea

        if temp is None:
            return 0.0

        return temp

    @heat_emitting_area.setter
    def heat_emitting_area(self, value: 'float'):
        self.wrapped.HeatEmittingArea = float(value) if value is not None else 0.0

    @property
    def heat_emitting_area_method(self) -> '_1930.DefaultOrUserInput':
        """DefaultOrUserInput: 'HeatEmittingAreaMethod' is the original name of this property."""

        temp = self.wrapped.HeatEmittingAreaMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingResults.DefaultOrUserInput')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_results._1930', 'DefaultOrUserInput')(value) if value is not None else None

    @heat_emitting_area_method.setter
    def heat_emitting_area_method(self, value: '_1930.DefaultOrUserInput'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingResults.DefaultOrUserInput')
        self.wrapped.HeatEmittingAreaMethod = value

    @property
    def cast_to(self) -> 'PlainJournalHousing._Cast_PlainJournalHousing':
        return self._Cast_PlainJournalHousing(self)
