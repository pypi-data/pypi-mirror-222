"""_5837.py

ResultsForMultipleOrdersForFESurface
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_MULTIPLE_ORDERS_FOR_FE_SURFACE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForMultipleOrdersForFESurface')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5834


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForMultipleOrdersForFESurface',)


class ResultsForMultipleOrdersForFESurface(_5836.ResultsForMultipleOrders):
    """ResultsForMultipleOrdersForFESurface

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_MULTIPLE_ORDERS_FOR_FE_SURFACE

    class _Cast_ResultsForMultipleOrdersForFESurface:
        """Special nested class for casting ResultsForMultipleOrdersForFESurface to subclasses."""

        def __init__(self, parent: 'ResultsForMultipleOrdersForFESurface'):
            self._parent = parent

        @property
        def results_for_multiple_orders(self):
            return self._parent._cast(_5836.ResultsForMultipleOrders)

        @property
        def results_for_multiple_orders_for_fe_surface(self) -> 'ResultsForMultipleOrdersForFESurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ResultsForMultipleOrdersForFESurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_surfaces(self) -> 'List[_5834.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]':
        """List[HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]: 'FESurfaces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESurfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ResultsForMultipleOrdersForFESurface._Cast_ResultsForMultipleOrdersForFESurface':
        return self._Cast_ResultsForMultipleOrdersForFESurface(self)
