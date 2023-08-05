"""_6460.py

PlanetaryGearSetCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'PlanetaryGearSetCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundDynamicAnalysis',)


class PlanetaryGearSetCompoundDynamicAnalysis(_6425.CylindricalGearSetCompoundDynamicAnalysis):
    """PlanetaryGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_PlanetaryGearSetCompoundDynamicAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(self):
            return self._parent._cast(_6425.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6436
            
            return self._parent._cast(_6436.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
            
            return self._parent._cast(_6474.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(self) -> 'PlanetaryGearSetCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6331.PlanetaryGearSetDynamicAnalysis]':
        """List[PlanetaryGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6331.PlanetaryGearSetDynamicAnalysis]':
        """List[PlanetaryGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundDynamicAnalysis._Cast_PlanetaryGearSetCompoundDynamicAnalysis':
        return self._Cast_PlanetaryGearSetCompoundDynamicAnalysis(self)
