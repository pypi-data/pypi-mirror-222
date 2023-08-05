"""_2106.py

LoadedFluidFilmBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1941
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FLUID_FILM_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedFluidFilmBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFluidFilmBearingResults',)


class LoadedFluidFilmBearingResults(_1941.LoadedDetailedBearingResults):
    """LoadedFluidFilmBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FLUID_FILM_BEARING_RESULTS

    class _Cast_LoadedFluidFilmBearingResults:
        """Special nested class for casting LoadedFluidFilmBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedFluidFilmBearingResults'):
            self._parent = parent

        @property
        def loaded_detailed_bearing_results(self):
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
        def loaded_grease_filled_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2107
            
            return self._parent._cast(_2107.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2108
            
            return self._parent._cast(_2108.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2109
            
            return self._parent._cast(_2109.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_results.fluid_film import _2111
            
            return self._parent._cast(_2111.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2114
            
            return self._parent._cast(_2114.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2115
            
            return self._parent._cast(_2115.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self) -> 'LoadedFluidFilmBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedFluidFilmBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self) -> 'float':
        """float: 'RelativeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults':
        return self._Cast_LoadedFluidFilmBearingResults(self)
