﻿"""_6779.py

AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6772
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_STATIC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AdvancedTimeSteppingAnalysisForModulationStaticLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedTimeSteppingAnalysisForModulationStaticLoadCase',)


class AdvancedTimeSteppingAnalysisForModulationStaticLoadCase(_6772.StaticLoadCase):
    """AdvancedTimeSteppingAnalysisForModulationStaticLoadCase

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_STATIC_LOAD_CASE

    class _Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulationStaticLoadCase to subclasses."""

        def __init__(self, parent: 'AdvancedTimeSteppingAnalysisForModulationStaticLoadCase'):
            self._parent = parent

        @property
        def static_load_case(self):
            return self._parent._cast(_6772.StaticLoadCase)

        @property
        def load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.LoadCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.Context)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(self) -> 'AdvancedTimeSteppingAnalysisForModulationStaticLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedTimeSteppingAnalysisForModulationStaticLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_analysis_options(self) -> '_5736.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AdvancedTimeSteppingAnalysisForModulationStaticLoadCase._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase':
        return self._Cast_AdvancedTimeSteppingAnalysisForModulationStaticLoadCase(self)
