"""_7365.py

VirtualComponentAdvancedSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'VirtualComponentAdvancedSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentAdvancedSystemDeflection',)


class VirtualComponentAdvancedSystemDeflection(_7319.MountableComponentAdvancedSystemDeflection):
    """VirtualComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_VirtualComponentAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'VirtualComponentAdvancedSystemDeflection'):
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
        def mass_disc_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7318
            
            return self._parent._cast(_7318.MeasurementComponentAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7328
            
            return self._parent._cast(_7328.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7329
            
            return self._parent._cast(_7329.PowerLoadAdvancedSystemDeflection)

        @property
        def unbalanced_mass_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7364
            
            return self._parent._cast(_7364.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(self) -> 'VirtualComponentAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2462.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualComponentAdvancedSystemDeflection._Cast_VirtualComponentAdvancedSystemDeflection':
        return self._Cast_VirtualComponentAdvancedSystemDeflection(self)
