﻿"""_2108.py

LoadedPadFluidFilmBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2106
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_PAD_FLUID_FILM_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedPadFluidFilmBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedPadFluidFilmBearingResults',)


class LoadedPadFluidFilmBearingResults(_2106.LoadedFluidFilmBearingResults):
    """LoadedPadFluidFilmBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_PAD_FLUID_FILM_BEARING_RESULTS

    class _Cast_LoadedPadFluidFilmBearingResults:
        """Special nested class for casting LoadedPadFluidFilmBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedPadFluidFilmBearingResults'):
            self._parent = parent

        @property
        def loaded_fluid_film_bearing_results(self):
            return self._parent._cast(_2106.LoadedFluidFilmBearingResults)

        @property
        def loaded_detailed_bearing_results(self):
            from mastapy.bearings.bearing_results import _1941
            
            return self._parent._cast(_1941.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1944
            
            return self._parent._cast(_1944.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(self):
            from mastapy.bearings.bearing_results import _1936
            
            return self._parent._cast(_1936.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1862
            
            return self._parent._cast(_1862.BearingLoadCaseResultsLightweight)

        @property
        def loaded_tilting_pad_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2114
            
            return self._parent._cast(_2114.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2115
            
            return self._parent._cast(_2115.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(self) -> 'LoadedPadFluidFilmBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedPadFluidFilmBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_film_thickness(self) -> 'float':
        """float: 'MinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFilmThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_inlet_temperature(self) -> 'float':
        """float: 'OilInletTemperature' is the original name of this property."""

        temp = self.wrapped.OilInletTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_inlet_temperature.setter
    def oil_inlet_temperature(self, value: 'float'):
        self.wrapped.OilInletTemperature = float(value) if value is not None else 0.0

    @property
    def reynolds_number(self) -> 'float':
        """float: 'ReynoldsNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReynoldsNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_speed(self) -> 'float':
        """float: 'SlidingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedPadFluidFilmBearingResults._Cast_LoadedPadFluidFilmBearingResults':
        return self._Cast_LoadedPadFluidFilmBearingResults(self)
