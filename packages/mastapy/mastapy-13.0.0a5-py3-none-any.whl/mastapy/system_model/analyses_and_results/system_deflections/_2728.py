"""_2728.py

CylindricalGearSystemDeflectionTimestep
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.system_deflections import _2727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSystemDeflectionTimestep')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSystemDeflectionTimestep',)


class CylindricalGearSystemDeflectionTimestep(_2727.CylindricalGearSystemDeflection):
    """CylindricalGearSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP

    class _Cast_CylindricalGearSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearSystemDeflectionTimestep to subclasses."""

        def __init__(self, parent: 'CylindricalGearSystemDeflectionTimestep'):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection(self):
            return self._parent._cast(_2727.CylindricalGearSystemDeflection)

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
        def cylindrical_gear_system_deflection_timestep(self) -> 'CylindricalGearSystemDeflectionTimestep':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSystemDeflectionTimestep.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep':
        return self._Cast_CylindricalGearSystemDeflectionTimestep(self)
