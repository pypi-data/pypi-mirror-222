"""_7378.py

AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7406
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7245


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection',)


class AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(_7406.ConicalGearSetCompoundAdvancedSystemDeflection):
    """AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_system_deflection(self):
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
        def bevel_differential_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7385
            
            return self._parent._cast(_7385.BevelDifferentialGearSetCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7390
            
            return self._parent._cast(_7390.BevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7436
            
            return self._parent._cast(_7436.HypoidGearSetCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7473
            
            return self._parent._cast(_7473.SpiralBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7479
            
            return self._parent._cast(_7479.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7482
            
            return self._parent._cast(_7482.StraightBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7500
            
            return self._parent._cast(_7500.ZerolBevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(self) -> 'AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_7245.AGMAGleasonConicalGearSetAdvancedSystemDeflection]':
        """List[AGMAGleasonConicalGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7245.AGMAGleasonConicalGearSetAdvancedSystemDeflection]':
        """List[AGMAGleasonConicalGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(self)
