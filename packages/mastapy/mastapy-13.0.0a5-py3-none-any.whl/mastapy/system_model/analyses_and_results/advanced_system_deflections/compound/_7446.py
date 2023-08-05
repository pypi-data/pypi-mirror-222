"""_7446.py

KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7315
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7444, _7445


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection',)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection(_7440.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(self):
            return self._parent._cast(_7440.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7406
            
            return self._parent._cast(_7406.ConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7432
            
            return self._parent._cast(_7432.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7470
            
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
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2523.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2523.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7315.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_advanced_system_deflection(self) -> 'List[_7444.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_advanced_system_deflection(self) -> 'List[_7445.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7315.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection(self)
