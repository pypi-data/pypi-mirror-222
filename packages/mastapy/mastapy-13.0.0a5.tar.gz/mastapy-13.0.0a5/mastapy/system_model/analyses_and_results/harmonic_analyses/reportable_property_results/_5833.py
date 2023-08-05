"""_5833.py

HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5844


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic',)


class HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic(_5832.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    """HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC

    class _Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic'):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(self):
            return self._parent._cast(_5832.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic)

        @property
        def harmonic_analysis_results_broken_down_by_node_within_a_harmonic(self) -> 'HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_name(self) -> 'str':
        """str: 'NodeName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeName

        if temp is None:
            return ''

        return temp

    @property
    def acceleration(self) -> '_5844.ResultsForResponseOfANodeOnAHarmonic':
        """ResultsForResponseOfANodeOnAHarmonic: 'Acceleration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Acceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def displacement(self) -> '_5844.ResultsForResponseOfANodeOnAHarmonic':
        """ResultsForResponseOfANodeOnAHarmonic: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Displacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force(self) -> '_5844.ResultsForResponseOfANodeOnAHarmonic':
        """ResultsForResponseOfANodeOnAHarmonic: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def velocity(self) -> '_5844.ResultsForResponseOfANodeOnAHarmonic':
        """ResultsForResponseOfANodeOnAHarmonic: 'Velocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Velocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic':
        return self._Cast_HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic(self)
