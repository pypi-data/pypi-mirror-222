﻿"""_7033.py

FEPartAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6975
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'FEPartAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.static_loads import _6855
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5735
    from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5827
    from mastapy.system_model.analyses_and_results.system_deflections import _2739


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartAdvancedTimeSteppingAnalysisForModulation',)


class FEPartAdvancedTimeSteppingAnalysisForModulation(_6975.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation):
    """FEPartAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FE_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_FEPartAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FEPartAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'FEPartAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(self):
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
        def fe_part_advanced_time_stepping_analysis_for_modulation(self) -> 'FEPartAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def export_accelerations(self) -> 'str':
        """str: 'ExportAccelerations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExportAccelerations

        if temp is None:
            return ''

        return temp

    @property
    def export_displacements(self) -> 'str':
        """str: 'ExportDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExportDisplacements

        if temp is None:
            return ''

        return temp

    @property
    def export_forces(self) -> 'str':
        """str: 'ExportForces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExportForces

        if temp is None:
            return ''

        return temp

    @property
    def export_velocities(self) -> 'str':
        """str: 'ExportVelocities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExportVelocities

        if temp is None:
            return ''

        return temp

    @property
    def component_design(self) -> '_2436.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6855.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def export(self) -> '_5735.HarmonicAnalysisFEExportOptions':
        """HarmonicAnalysisFEExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_5827.FEPartHarmonicAnalysisResultsPropertyAccessor':
        """FEPartHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2739.FEPartSystemDeflection':
        """FEPartSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[FEPartAdvancedTimeSteppingAnalysisForModulation]':
        """List[FEPartAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartAdvancedTimeSteppingAnalysisForModulation._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_FEPartAdvancedTimeSteppingAnalysisForModulation(self)
