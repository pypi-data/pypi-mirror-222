"""_6673.py

ConceptGearSetCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'ConceptGearSetCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2504
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6542
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6671, _6672


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundCriticalSpeedAnalysis',)


class ConceptGearSetCompoundCriticalSpeedAnalysis(_6702.GearSetCompoundCriticalSpeedAnalysis):
    """ConceptGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_ConceptGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConceptGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptGearSetCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def gear_set_compound_critical_speed_analysis(self):
            return self._parent._cast(_6702.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6740
            
            return self._parent._cast(_6740.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6642
            
            return self._parent._cast(_6642.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def concept_gear_set_compound_critical_speed_analysis(self) -> 'ConceptGearSetCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2504.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2504.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6542.ConceptGearSetCriticalSpeedAnalysis]':
        """List[ConceptGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_critical_speed_analysis(self) -> 'List[_6671.ConceptGearCompoundCriticalSpeedAnalysis]':
        """List[ConceptGearCompoundCriticalSpeedAnalysis]: 'ConceptGearsCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_critical_speed_analysis(self) -> 'List[_6672.ConceptGearMeshCompoundCriticalSpeedAnalysis]':
        """List[ConceptGearMeshCompoundCriticalSpeedAnalysis]: 'ConceptMeshesCompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6542.ConceptGearSetCriticalSpeedAnalysis]':
        """List[ConceptGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetCompoundCriticalSpeedAnalysis._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis':
        return self._Cast_ConceptGearSetCompoundCriticalSpeedAnalysis(self)
