"""_1938.py

LoadedConceptAxialClearanceBearingResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1939
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CONCEPT_AXIAL_CLEARANCE_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedConceptAxialClearanceBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedConceptAxialClearanceBearingResults',)


class LoadedConceptAxialClearanceBearingResults(_1939.LoadedConceptClearanceBearingResults):
    """LoadedConceptAxialClearanceBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CONCEPT_AXIAL_CLEARANCE_BEARING_RESULTS

    class _Cast_LoadedConceptAxialClearanceBearingResults:
        """Special nested class for casting LoadedConceptAxialClearanceBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedConceptAxialClearanceBearingResults'):
            self._parent = parent

        @property
        def loaded_concept_clearance_bearing_results(self):
            return self._parent._cast(_1939.LoadedConceptClearanceBearingResults)

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
        def loaded_concept_axial_clearance_bearing_results(self) -> 'LoadedConceptAxialClearanceBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedConceptAxialClearanceBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lower_angle_of_contact(self) -> 'float':
        """float: 'LowerAngleOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowerAngleOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def upper_angle_of_contact(self) -> 'float':
        """float: 'UpperAngleOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UpperAngleOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedConceptAxialClearanceBearingResults._Cast_LoadedConceptAxialClearanceBearingResults':
        return self._Cast_LoadedConceptAxialClearanceBearingResults(self)
