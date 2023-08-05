﻿"""_7073.py

ShaftAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ShaftAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2465
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2786


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAdvancedTimeSteppingAnalysisForModulation',)


class ShaftAdvancedTimeSteppingAnalysisForModulation(_6974.AbstractShaftAdvancedTimeSteppingAnalysisForModulation):
    """ShaftAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SHAFT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_ShaftAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ShaftAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'ShaftAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_6974.AbstractShaftAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6975
            
            return self._parent._cast(_6975.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation)

        @property
        def component_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7002
            
            return self._parent._cast(_7002.ComponentAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7057
            
            return self._parent._cast(_7057.PartAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(self) -> 'ShaftAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2465.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6918.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2786.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftAdvancedTimeSteppingAnalysisForModulation]':
        """List[ShaftAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_ShaftAdvancedTimeSteppingAnalysisForModulation(self)
