"""_3830.py

PlanetaryGearSetStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'PlanetaryGearSetStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetStabilityAnalysis',)


class PlanetaryGearSetStabilityAnalysis(_3794.CylindricalGearSetStabilityAnalysis):
    """PlanetaryGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STABILITY_ANALYSIS

    class _Cast_PlanetaryGearSetStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetStabilityAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_stability_analysis(self):
            return self._parent._cast(_3794.CylindricalGearSetStabilityAnalysis)

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
        def planetary_gear_set_stability_analysis(self) -> 'PlanetaryGearSetStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2524.PlanetaryGearSet':
        """PlanetaryGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlanetaryGearSetStabilityAnalysis._Cast_PlanetaryGearSetStabilityAnalysis':
        return self._Cast_PlanetaryGearSetStabilityAnalysis(self)
