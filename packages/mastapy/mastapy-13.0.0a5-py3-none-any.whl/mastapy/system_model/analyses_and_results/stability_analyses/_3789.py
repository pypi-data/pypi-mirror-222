"""_3789.py

CycloidalAssemblyStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CycloidalAssemblyStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2550
    from mastapy.system_model.analyses_and_results.static_loads import _6825


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyStabilityAnalysis',)


class CycloidalAssemblyStabilityAnalysis(_3844.SpecialisedAssemblyStabilityAnalysis):
    """CycloidalAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_STABILITY_ANALYSIS

    class _Cast_CycloidalAssemblyStabilityAnalysis:
        """Special nested class for casting CycloidalAssemblyStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CycloidalAssemblyStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(self):
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
        def cycloidal_assembly_stability_analysis(self) -> 'CycloidalAssemblyStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2550.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6825.CycloidalAssemblyLoadCase':
        """CycloidalAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CycloidalAssemblyStabilityAnalysis._Cast_CycloidalAssemblyStabilityAnalysis':
        return self._Cast_CycloidalAssemblyStabilityAnalysis(self)
