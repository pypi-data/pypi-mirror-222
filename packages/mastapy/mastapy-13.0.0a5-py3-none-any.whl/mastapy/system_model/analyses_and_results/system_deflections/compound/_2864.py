"""_2864.py

ConceptGearSetCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ConceptGearSetCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2504
    from mastapy.system_model.analyses_and_results.system_deflections import _2703
    from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862, _2863


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundSystemDeflection',)


class ConceptGearSetCompoundSystemDeflection(_2894.GearSetCompoundSystemDeflection):
    """ConceptGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_ConceptGearSetCompoundSystemDeflection:
        """Special nested class for casting ConceptGearSetCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConceptGearSetCompoundSystemDeflection'):
            self._parent = parent

        @property
        def gear_set_compound_system_deflection(self):
            return self._parent._cast(_2894.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
            
            return self._parent._cast(_2933.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2833
            
            return self._parent._cast(_2833.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
            
            return self._parent._cast(_2913.PartCompoundSystemDeflection)

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
        def concept_gear_set_compound_system_deflection(self) -> 'ConceptGearSetCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundSystemDeflection.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_2703.ConceptGearSetSystemDeflection]':
        """List[ConceptGearSetSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_system_deflection(self) -> 'List[_2862.ConceptGearCompoundSystemDeflection]':
        """List[ConceptGearCompoundSystemDeflection]: 'ConceptGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_system_deflection(self) -> 'List[_2863.ConceptGearMeshCompoundSystemDeflection]':
        """List[ConceptGearMeshCompoundSystemDeflection]: 'ConceptMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2703.ConceptGearSetSystemDeflection]':
        """List[ConceptGearSetSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetCompoundSystemDeflection._Cast_ConceptGearSetCompoundSystemDeflection':
        return self._Cast_ConceptGearSetCompoundSystemDeflection(self)
