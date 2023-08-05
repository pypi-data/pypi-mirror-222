"""_3945.py

KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3813


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis',)


class KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis(_3911.ConicalGearSetCompoundStabilityAnalysis):
    """KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(self):
            return self._parent._cast(_3911.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3937
            
            return self._parent._cast(_3937.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3975
            
            return self._parent._cast(_3975.SpecialisedAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3877
            
            return self._parent._cast(_3877.AbstractAssemblyCompoundStabilityAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3948
            
            return self._parent._cast(_3948.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3951
            
            return self._parent._cast(_3951.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3813.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3813.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis(self)
