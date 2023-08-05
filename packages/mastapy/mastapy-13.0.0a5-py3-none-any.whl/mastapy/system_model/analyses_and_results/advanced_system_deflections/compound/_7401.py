"""_7401.py

ConceptGearCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7430
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'ConceptGearCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2503
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundAdvancedSystemDeflection',)


class ConceptGearCompoundAdvancedSystemDeflection(_7430.GearCompoundAdvancedSystemDeflection):
    """ConceptGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ConceptGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConceptGearCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def gear_compound_advanced_system_deflection(self):
            return self._parent._cast(_7430.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7449
            
            return self._parent._cast(_7449.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7397
            
            return self._parent._cast(_7397.ComponentCompoundAdvancedSystemDeflection)

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
        def concept_gear_compound_advanced_system_deflection(self) -> 'ConceptGearCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2503.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7268.ConceptGearAdvancedSystemDeflection]':
        """List[ConceptGearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7268.ConceptGearAdvancedSystemDeflection]':
        """List[ConceptGearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearCompoundAdvancedSystemDeflection._Cast_ConceptGearCompoundAdvancedSystemDeflection':
        return self._Cast_ConceptGearCompoundAdvancedSystemDeflection(self)
