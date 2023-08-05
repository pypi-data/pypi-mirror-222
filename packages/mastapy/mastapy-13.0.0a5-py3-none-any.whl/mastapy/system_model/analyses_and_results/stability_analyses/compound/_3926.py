"""_3926.py

CylindricalGearSetCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CylindricalGearSetCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2508
    from mastapy.system_model.analyses_and_results.stability_analyses import _3794
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3924, _3925


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCompoundStabilityAnalysis',)


class CylindricalGearSetCompoundStabilityAnalysis(_3937.GearSetCompoundStabilityAnalysis):
    """CylindricalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CylindricalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting CylindricalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def gear_set_compound_stability_analysis(self):
            return self._parent._cast(_3937.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3975
            
            return self._parent._cast(_3975.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3877
            
            return self._parent._cast(_3877.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
            
            return self._parent._cast(_3956.PartCompoundStabilityAnalysis)

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
        def planetary_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3961
            
            return self._parent._cast(_3961.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(self) -> 'CylindricalGearSetCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2508.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2508.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3794.CylindricalGearSetStabilityAnalysis]':
        """List[CylindricalGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_compound_stability_analysis(self) -> 'List[_3924.CylindricalGearCompoundStabilityAnalysis]':
        """List[CylindricalGearCompoundStabilityAnalysis]: 'CylindricalGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_compound_stability_analysis(self) -> 'List[_3925.CylindricalGearMeshCompoundStabilityAnalysis]':
        """List[CylindricalGearMeshCompoundStabilityAnalysis]: 'CylindricalMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3794.CylindricalGearSetStabilityAnalysis]':
        """List[CylindricalGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearSetCompoundStabilityAnalysis._Cast_CylindricalGearSetCompoundStabilityAnalysis':
        return self._Cast_CylindricalGearSetCompoundStabilityAnalysis(self)
