"""_7409.py

CouplingCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'CouplingCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7277


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundAdvancedSystemDeflection',)


class CouplingCompoundAdvancedSystemDeflection(_7470.SpecialisedAssemblyCompoundAdvancedSystemDeflection):
    """CouplingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_CouplingCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(self):
            return self._parent._cast(_7470.SpecialisedAssemblyCompoundAdvancedSystemDeflection)

        @property
        def abstract_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
            
            return self._parent._cast(_7372.AbstractAssemblyCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7451
            
            return self._parent._cast(_7451.PartCompoundAdvancedSystemDeflection)

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
        def clutch_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
            return self._parent._cast(_7393.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7398
            
            return self._parent._cast(_7398.ConceptCouplingCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7452
            
            return self._parent._cast(_7452.PartToPartShearCouplingCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7474
            
            return self._parent._cast(_7474.SpringDamperCompoundAdvancedSystemDeflection)

        @property
        def torque_converter_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7489
            
            return self._parent._cast(_7489.TorqueConverterCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(self) -> 'CouplingCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_7277.CouplingAdvancedSystemDeflection]':
        """List[CouplingAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7277.CouplingAdvancedSystemDeflection]':
        """List[CouplingAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection':
        return self._Cast_CouplingCompoundAdvancedSystemDeflection(self)
