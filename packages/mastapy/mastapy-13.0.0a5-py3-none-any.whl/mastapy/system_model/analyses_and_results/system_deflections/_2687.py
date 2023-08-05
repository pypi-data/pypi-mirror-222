"""_2687.py

BevelDifferentialSunGearSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelDifferentialSunGearSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2500
    from mastapy.system_model.analyses_and_results.power_flows import _4027


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearSystemDeflection',)


class BevelDifferentialSunGearSystemDeflection(_2685.BevelDifferentialGearSystemDeflection):
    """BevelDifferentialSunGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_SYSTEM_DEFLECTION

    class _Cast_BevelDifferentialSunGearSystemDeflection:
        """Special nested class for casting BevelDifferentialSunGearSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelDifferentialSunGearSystemDeflection'):
            self._parent = parent

        @property
        def bevel_differential_gear_system_deflection(self):
            return self._parent._cast(_2685.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2690
            
            return self._parent._cast(_2690.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2673
            
            return self._parent._cast(_2673.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2708
            
            return self._parent._cast(_2708.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2743
            
            return self._parent._cast(_2743.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

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
        def bevel_differential_sun_gear_system_deflection(self) -> 'BevelDifferentialSunGearSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2500.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4027.BevelDifferentialSunGearPowerFlow':
        """BevelDifferentialSunGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelDifferentialSunGearSystemDeflection._Cast_BevelDifferentialSunGearSystemDeflection':
        return self._Cast_BevelDifferentialSunGearSystemDeflection(self)
