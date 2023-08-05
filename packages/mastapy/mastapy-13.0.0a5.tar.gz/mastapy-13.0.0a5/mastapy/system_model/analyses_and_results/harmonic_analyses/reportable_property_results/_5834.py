﻿"""_5834.py

HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5843


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic',)


class HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(_5832.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    """HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC

    class _Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic'):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(self):
            return self._parent._cast(_5832.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic)

        @property
        def harmonic_analysis_combined_for_multiple_surfaces_within_a_harmonic(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5829
            
            return self._parent._cast(_5829.HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic)

        @property
        def harmonic_analysis_results_broken_down_by_surface_within_a_harmonic(self) -> 'HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surface_name(self) -> 'str':
        """str: 'SurfaceName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceName

        if temp is None:
            return ''

        return temp

    @property
    def airborne_sound_power(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'AirborneSoundPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AirborneSoundPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_normal_velocity(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'MaximumNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalVelocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_mean_squared_normal_acceleration(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'RootMeanSquaredNormalAcceleration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootMeanSquaredNormalAcceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_mean_squared_normal_displacement(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'RootMeanSquaredNormalDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootMeanSquaredNormalDisplacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_mean_squared_normal_velocity(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'RootMeanSquaredNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootMeanSquaredNormalVelocity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def sound_intensity(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'SoundIntensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SoundIntensity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def sound_pressure(self) -> '_5843.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'SoundPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SoundPressure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic':
        return self._Cast_HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(self)
