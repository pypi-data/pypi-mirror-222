"""_2008.py

LoadedNeedleRollerBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_results.rolling import _1996
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NEEDLE_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNeedleRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNeedleRollerBearingResults',)


class LoadedNeedleRollerBearingResults(_1996.LoadedCylindricalRollerBearingResults):
    """LoadedNeedleRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NEEDLE_ROLLER_BEARING_RESULTS

    class _Cast_LoadedNeedleRollerBearingResults:
        """Special nested class for casting LoadedNeedleRollerBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedNeedleRollerBearingResults'):
            self._parent = parent

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            return self._parent._cast(_1996.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2011
            
            return self._parent._cast(_2011.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2016
            
            return self._parent._cast(_2016.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2020
            
            return self._parent._cast(_2020.LoadedRollingBearingResults)

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
        def loaded_needle_roller_bearing_results(self) -> 'LoadedNeedleRollerBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNeedleRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedNeedleRollerBearingResults._Cast_LoadedNeedleRollerBearingResults':
        return self._Cast_LoadedNeedleRollerBearingResults(self)
