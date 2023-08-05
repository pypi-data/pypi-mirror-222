"""_2870.py

CouplingCompoundSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CouplingCompoundSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2713


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundSystemDeflection',)


class CouplingCompoundSystemDeflection(_2933.SpecialisedAssemblyCompoundSystemDeflection):
    """CouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_CouplingCompoundSystemDeflection:
        """Special nested class for casting CouplingCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingCompoundSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(self):
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
        def clutch_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2854
            
            return self._parent._cast(_2854.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2859
            
            return self._parent._cast(_2859.ConceptCouplingCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2914
            
            return self._parent._cast(_2914.PartToPartShearCouplingCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
            
            return self._parent._cast(_2937.SpringDamperCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
            
            return self._parent._cast(_2952.TorqueConverterCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(self) -> 'CouplingCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2713.CouplingSystemDeflection]':
        """List[CouplingSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2713.CouplingSystemDeflection]':
        """List[CouplingSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection':
        return self._Cast_CouplingCompoundSystemDeflection(self)
