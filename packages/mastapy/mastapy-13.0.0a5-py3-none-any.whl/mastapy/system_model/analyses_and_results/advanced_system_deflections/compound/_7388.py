"""_7388.py

BevelGearCompoundAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'BevelGearCompoundAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7255


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundAdvancedSystemDeflection',)


class BevelGearCompoundAdvancedSystemDeflection(_7376.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection):
    """BevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelGearCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            return self._parent._cast(_7376.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7404
            
            return self._parent._cast(_7404.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7430
            
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
        def bevel_differential_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7383
            
            return self._parent._cast(_7383.BevelDifferentialGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7386
            
            return self._parent._cast(_7386.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7387
            
            return self._parent._cast(_7387.BevelDifferentialSunGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7471
            
            return self._parent._cast(_7471.SpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7477
            
            return self._parent._cast(_7477.StraightBevelDiffGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7480
            
            return self._parent._cast(_7480.StraightBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7483
            
            return self._parent._cast(_7483.StraightBevelPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7484
            
            return self._parent._cast(_7484.StraightBevelSunGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7498
            
            return self._parent._cast(_7498.ZerolBevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_compound_advanced_system_deflection(self) -> 'BevelGearCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7255.BevelGearAdvancedSystemDeflection]':
        """List[BevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7255.BevelGearAdvancedSystemDeflection]':
        """List[BevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection':
        return self._Cast_BevelGearCompoundAdvancedSystemDeflection(self)
