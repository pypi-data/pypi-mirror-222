"""_3809.py

HypoidGearSetStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'HypoidGearSetStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.static_loads import _6875
    from mastapy.system_model.analyses_and_results.stability_analyses import _3810, _3808


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetStabilityAnalysis',)


class HypoidGearSetStabilityAnalysis(_3750.AGMAGleasonConicalGearSetStabilityAnalysis):
    """HypoidGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STABILITY_ANALYSIS

    class _Cast_HypoidGearSetStabilityAnalysis:
        """Special nested class for casting HypoidGearSetStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'HypoidGearSetStabilityAnalysis'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_stability_analysis(self):
            return self._parent._cast(_3750.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3778
            
            return self._parent._cast(_3778.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3805
            
            return self._parent._cast(_3805.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3844
            
            return self._parent._cast(_3844.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3745
            
            return self._parent._cast(_3745.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

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
        def hypoid_gear_set_stability_analysis(self) -> 'HypoidGearSetStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2517.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6875.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears_stability_analysis(self) -> 'List[_3810.HypoidGearStabilityAnalysis]':
        """List[HypoidGearStabilityAnalysis]: 'HypoidGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_stability_analysis(self) -> 'List[_3808.HypoidGearMeshStabilityAnalysis]':
        """List[HypoidGearMeshStabilityAnalysis]: 'HypoidMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearSetStabilityAnalysis._Cast_HypoidGearSetStabilityAnalysis':
        return self._Cast_HypoidGearSetStabilityAnalysis(self)
