"""_5665.py

BevelDifferentialGearSetHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BevelDifferentialGearSetHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2498
    from mastapy.system_model.analyses_and_results.static_loads import _6792
    from mastapy.system_model.analyses_and_results.system_deflections import _2684
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5663, _5664


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetHarmonicAnalysis',)


class BevelDifferentialGearSetHarmonicAnalysis(_5670.BevelGearSetHarmonicAnalysis):
    """BevelDifferentialGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_HARMONIC_ANALYSIS

    class _Cast_BevelDifferentialGearSetHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearSetHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetHarmonicAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_harmonic_analysis(self):
            return self._parent._cast(_5670.BevelGearSetHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5658
            
            return self._parent._cast(_5658.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
            
            return self._parent._cast(_5687.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730
            
            return self._parent._cast(_5730.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5780
            
            return self._parent._cast(_5780.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
            
            return self._parent._cast(_5651.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5758
            
            return self._parent._cast(_5758.PartHarmonicAnalysis)

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
        def bevel_differential_gear_set_harmonic_analysis(self) -> 'BevelDifferentialGearSetHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2498.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6792.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2684.BevelDifferentialGearSetSystemDeflection':
        """BevelDifferentialGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5663.BevelDifferentialGearHarmonicAnalysis]':
        """List[BevelDifferentialGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_harmonic_analysis(self) -> 'List[_5663.BevelDifferentialGearHarmonicAnalysis]':
        """List[BevelDifferentialGearHarmonicAnalysis]: 'BevelDifferentialGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5664.BevelDifferentialGearMeshHarmonicAnalysis]':
        """List[BevelDifferentialGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_harmonic_analysis(self) -> 'List[_5664.BevelDifferentialGearMeshHarmonicAnalysis]':
        """List[BevelDifferentialGearMeshHarmonicAnalysis]: 'BevelDifferentialMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetHarmonicAnalysis._Cast_BevelDifferentialGearSetHarmonicAnalysis':
        return self._Cast_BevelDifferentialGearSetHarmonicAnalysis(self)
