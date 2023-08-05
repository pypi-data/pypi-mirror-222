"""_1861.py

BearingLoadCaseResultsForPST
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings import _1862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_FOR_PST = python_net_import('SMT.MastaAPI.Bearings', 'BearingLoadCaseResultsForPST')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingLoadCaseResultsForPST',)


class BearingLoadCaseResultsForPST(_1862.BearingLoadCaseResultsLightweight):
    """BearingLoadCaseResultsForPST

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_FOR_PST

    class _Cast_BearingLoadCaseResultsForPST:
        """Special nested class for casting BearingLoadCaseResultsForPST to subclasses."""

        def __init__(self, parent: 'BearingLoadCaseResultsForPST'):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(self):
            return self._parent._cast(_1862.BearingLoadCaseResultsLightweight)

        @property
        def bearing_load_case_results_for_pst(self) -> 'BearingLoadCaseResultsForPST':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingLoadCaseResultsForPST.TYPE'):
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
    def cast_to(self) -> 'BearingLoadCaseResultsForPST._Cast_BearingLoadCaseResultsForPST':
        return self._Cast_BearingLoadCaseResultsForPST(self)
