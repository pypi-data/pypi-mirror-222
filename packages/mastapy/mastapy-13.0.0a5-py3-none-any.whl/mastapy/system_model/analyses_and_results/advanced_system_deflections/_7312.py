"""_7312.py

KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.static_loads import _6885
    from mastapy.gears.rating.klingelnberg_hypoid import _408
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310, _7311


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection',)


class KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection(_7309.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection):
    """KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(self):
            return self._parent._cast(_7309.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(self) -> 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2521.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6885.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_408.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_408.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2754.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_advanced_system_deflection(self) -> 'List[_7310.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_advanced_system_deflection(self) -> 'List[_7311.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection(self)
