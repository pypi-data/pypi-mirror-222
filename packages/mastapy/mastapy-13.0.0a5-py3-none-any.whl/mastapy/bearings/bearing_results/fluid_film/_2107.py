"""_2107.py

LoadedGreaseFilledJournalBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_results.fluid_film import _2109
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedGreaseFilledJournalBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedGreaseFilledJournalBearingResults',)


class LoadedGreaseFilledJournalBearingResults(_2109.LoadedPlainJournalBearingResults):
    """LoadedGreaseFilledJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_GREASE_FILLED_JOURNAL_BEARING_RESULTS

    class _Cast_LoadedGreaseFilledJournalBearingResults:
        """Special nested class for casting LoadedGreaseFilledJournalBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedGreaseFilledJournalBearingResults'):
            self._parent = parent

        @property
        def loaded_plain_journal_bearing_results(self):
            return self._parent._cast(_2109.LoadedPlainJournalBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2106
            
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
        def loaded_grease_filled_journal_bearing_results(self) -> 'LoadedGreaseFilledJournalBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedGreaseFilledJournalBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedGreaseFilledJournalBearingResults._Cast_LoadedGreaseFilledJournalBearingResults':
        return self._Cast_LoadedGreaseFilledJournalBearingResults(self)
