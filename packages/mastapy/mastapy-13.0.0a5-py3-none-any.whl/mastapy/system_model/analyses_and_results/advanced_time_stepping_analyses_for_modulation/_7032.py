﻿"""_7032.py

FaceGearSetAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'FaceGearSetAdvancedTimeSteppingAnalysisForModulation')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.static_loads import _6854
    from mastapy.system_model.analyses_and_results.system_deflections import _2737
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7030, _7031


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetAdvancedTimeSteppingAnalysisForModulation',)


class FaceGearSetAdvancedTimeSteppingAnalysisForModulation(_7037.GearSetAdvancedTimeSteppingAnalysisForModulation):
    """FaceGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting FaceGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'FaceGearSetAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7037.GearSetAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7076
            
            return self._parent._cast(_7076.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6973
            
            return self._parent._cast(_6973.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation)

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
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(self) -> 'FaceGearSetAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2511.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6854.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2737.FaceGearSetSystemDeflection':
        """FaceGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7030.FaceGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[FaceGearAdvancedTimeSteppingAnalysisForModulation]: 'FaceGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7031.FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[FaceGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'FaceMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_FaceGearSetAdvancedTimeSteppingAnalysisForModulation(self)
