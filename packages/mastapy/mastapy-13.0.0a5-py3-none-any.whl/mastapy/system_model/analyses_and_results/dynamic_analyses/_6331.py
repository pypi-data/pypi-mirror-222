"""_6331.py

PlanetaryGearSetDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'PlanetaryGearSetDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetDynamicAnalysis',)


class PlanetaryGearSetDynamicAnalysis(_6295.CylindricalGearSetDynamicAnalysis):
    """PlanetaryGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_DYNAMIC_ANALYSIS

    class _Cast_PlanetaryGearSetDynamicAnalysis:
        """Special nested class for casting PlanetaryGearSetDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetDynamicAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_dynamic_analysis(self):
            return self._parent._cast(_6295.CylindricalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
            
            return self._parent._cast(_6307.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345
            
            return self._parent._cast(_6345.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6246
            
            return self._parent._cast(_6246.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326
            
            return self._parent._cast(_6326.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

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
        def planetary_gear_set_dynamic_analysis(self) -> 'PlanetaryGearSetDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetDynamicAnalysis.TYPE'):
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
    def cast_to(self) -> 'PlanetaryGearSetDynamicAnalysis._Cast_PlanetaryGearSetDynamicAnalysis':
        return self._Cast_PlanetaryGearSetDynamicAnalysis(self)
