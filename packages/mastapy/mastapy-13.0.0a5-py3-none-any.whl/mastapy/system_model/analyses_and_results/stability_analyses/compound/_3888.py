"""_3888.py

BevelDifferentialGearCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'BevelDifferentialGearCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2497
    from mastapy.system_model.analyses_and_results.stability_analyses import _3758


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearCompoundStabilityAnalysis',)


class BevelDifferentialGearCompoundStabilityAnalysis(_3893.BevelGearCompoundStabilityAnalysis):
    """BevelDifferentialGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_STABILITY_ANALYSIS

    class _Cast_BevelDifferentialGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelDifferentialGearCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(self):
            return self._parent._cast(_3893.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3881
            
            return self._parent._cast(_3881.AGMAGleasonConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3909
            
            return self._parent._cast(_3909.ConicalGearCompoundStabilityAnalysis)

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
        def bevel_differential_planet_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3891
            
            return self._parent._cast(_3891.BevelDifferentialPlanetGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3892
            
            return self._parent._cast(_3892.BevelDifferentialSunGearCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(self) -> 'BevelDifferentialGearCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2497.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3758.BevelDifferentialGearStabilityAnalysis]':
        """List[BevelDifferentialGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3758.BevelDifferentialGearStabilityAnalysis]':
        """List[BevelDifferentialGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearCompoundStabilityAnalysis._Cast_BevelDifferentialGearCompoundStabilityAnalysis':
        return self._Cast_BevelDifferentialGearCompoundStabilityAnalysis(self)
