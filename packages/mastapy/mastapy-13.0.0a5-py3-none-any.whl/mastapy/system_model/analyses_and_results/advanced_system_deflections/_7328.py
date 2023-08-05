"""_7328.py

PointLoadAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PointLoadAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.static_loads import _6906
    from mastapy.system_model.analyses_and_results.system_deflections import _2773


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadAdvancedSystemDeflection',)


class PointLoadAdvancedSystemDeflection(_7365.VirtualComponentAdvancedSystemDeflection):
    """PointLoadAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_PointLoadAdvancedSystemDeflection:
        """Special nested class for casting PointLoadAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'PointLoadAdvancedSystemDeflection'):
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
        def point_load_advanced_system_deflection(self) -> 'PointLoadAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2454.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6906.PointLoadLoadCase':
        """PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2773.PointLoadSystemDeflection]':
        """List[PointLoadSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PointLoadAdvancedSystemDeflection._Cast_PointLoadAdvancedSystemDeflection':
        return self._Cast_PointLoadAdvancedSystemDeflection(self)
