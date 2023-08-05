"""_1970.py

LoadedAngularContactBallBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.bearings.bearing_results.rolling import _1989
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactBallBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactBallBearingResults',)


class LoadedAngularContactBallBearingResults(_1989.LoadedBallBearingResults):
    """LoadedAngularContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS

    class _Cast_LoadedAngularContactBallBearingResults:
        """Special nested class for casting LoadedAngularContactBallBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedAngularContactBallBearingResults'):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(self):
            return self._parent._cast(_1989.LoadedBallBearingResults)

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
        def loaded_angular_contact_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1973
            
            return self._parent._cast(_1973.LoadedAngularContactThrustBallBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(self) -> 'LoadedAngularContactBallBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactBallBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults':
        return self._Cast_LoadedAngularContactBallBearingResults(self)
