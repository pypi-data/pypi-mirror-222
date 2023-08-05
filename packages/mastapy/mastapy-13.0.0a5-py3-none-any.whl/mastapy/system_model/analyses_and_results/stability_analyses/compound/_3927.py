"""_3927.py

CylindricalPlanetGearCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3924
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CylindricalPlanetGearCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3796


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearCompoundStabilityAnalysis',)


class CylindricalPlanetGearCompoundStabilityAnalysis(_3924.CylindricalGearCompoundStabilityAnalysis):
    """CylindricalPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CylindricalPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_compound_stability_analysis(self):
            return self._parent._cast(_3924.CylindricalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3935
            
            return self._parent._cast(_3935.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
            
            return self._parent._cast(_3954.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3902
            
            return self._parent._cast(_3902.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3956
            
            return self._parent._cast(_3956.PartCompoundStabilityAnalysis)

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
        def cylindrical_planet_gear_compound_stability_analysis(self) -> 'CylindricalPlanetGearCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_3796.CylindricalPlanetGearStabilityAnalysis]':
        """List[CylindricalPlanetGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3796.CylindricalPlanetGearStabilityAnalysis]':
        """List[CylindricalPlanetGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalPlanetGearCompoundStabilityAnalysis._Cast_CylindricalPlanetGearCompoundStabilityAnalysis':
        return self._Cast_CylindricalPlanetGearCompoundStabilityAnalysis(self)
