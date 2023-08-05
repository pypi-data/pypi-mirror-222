"""_7343.py

SpiralBevelGearSetAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'SpiralBevelGearSetAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.gears.rating.spiral_bevel import _402
    from mastapy.system_model.analyses_and_results.system_deflections import _2790
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7341, _7342


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetAdvancedSystemDeflection',)


class SpiralBevelGearSetAdvancedSystemDeflection(_7257.BevelGearSetAdvancedSystemDeflection):
    """SpiralBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_SpiralBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting SpiralBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_system_deflection(self):
            return self._parent._cast(_7257.BevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7245
            
            return self._parent._cast(_7245.AGMAGleasonConicalGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7273
            
            return self._parent._cast(_7273.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7301
            
            return self._parent._cast(_7301.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
            
            return self._parent._cast(_7340.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7236
            
            return self._parent._cast(_7236.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
            
            return self._parent._cast(_7321.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(self) -> 'SpiralBevelGearSetAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2526.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6923.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_402.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_402.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2790.SpiralBevelGearSetSystemDeflection]':
        """List[SpiralBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_advanced_system_deflection(self) -> 'List[_7341.SpiralBevelGearAdvancedSystemDeflection]':
        """List[SpiralBevelGearAdvancedSystemDeflection]: 'SpiralBevelGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_advanced_system_deflection(self) -> 'List[_7342.SpiralBevelGearMeshAdvancedSystemDeflection]':
        """List[SpiralBevelGearMeshAdvancedSystemDeflection]: 'SpiralBevelMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetAdvancedSystemDeflection._Cast_SpiralBevelGearSetAdvancedSystemDeflection':
        return self._Cast_SpiralBevelGearSetAdvancedSystemDeflection(self)
