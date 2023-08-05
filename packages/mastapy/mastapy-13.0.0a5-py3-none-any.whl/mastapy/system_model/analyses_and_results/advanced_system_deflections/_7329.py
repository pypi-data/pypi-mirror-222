"""_7329.py

PowerLoadAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PowerLoadAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6907
    from mastapy.system_model.analyses_and_results.system_deflections import _2774
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7363


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadAdvancedSystemDeflection',)


class PowerLoadAdvancedSystemDeflection(_7365.VirtualComponentAdvancedSystemDeflection):
    """PowerLoadAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_PowerLoadAdvancedSystemDeflection:
        """Special nested class for casting PowerLoadAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'PowerLoadAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(self):
            return self._parent._cast(_7365.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
            
            return self._parent._cast(_7319.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
            
            return self._parent._cast(_7264.ComponentAdvancedSystemDeflection)

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
        def power_load_advanced_system_deflection(self) -> 'PowerLoadAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerLoadAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2455.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6907.PowerLoadLoadCase':
        """PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2774.PowerLoadSystemDeflection]':
        """List[PowerLoadSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def transmission_error_to_other_power_loads(self) -> 'List[_7363.TransmissionErrorToOtherPowerLoad]':
        """List[TransmissionErrorToOtherPowerLoad]: 'TransmissionErrorToOtherPowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionErrorToOtherPowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection':
        return self._Cast_PowerLoadAdvancedSystemDeflection(self)
