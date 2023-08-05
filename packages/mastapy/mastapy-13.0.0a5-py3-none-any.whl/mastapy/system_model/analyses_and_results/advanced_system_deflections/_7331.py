"""_7331.py

RingPinsAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'RingPinsAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6911
    from mastapy.system_model.analyses_and_results.system_deflections import _2776


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsAdvancedSystemDeflection',)


class RingPinsAdvancedSystemDeflection(_7319.MountableComponentAdvancedSystemDeflection):
    """RingPinsAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_RingPinsAdvancedSystemDeflection:
        """Special nested class for casting RingPinsAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'RingPinsAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(self):
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
        def ring_pins_advanced_system_deflection(self) -> 'RingPinsAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2552.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6911.RingPinsLoadCase':
        """RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2776.RingPinsSystemDeflection]':
        """List[RingPinsSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingPinsAdvancedSystemDeflection._Cast_RingPinsAdvancedSystemDeflection':
        return self._Cast_RingPinsAdvancedSystemDeflection(self)
