"""_6445.py

KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6442
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis',)


class KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis(_6442.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis):
    """KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(self):
            return self._parent._cast(_6442.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6434
            
            return self._parent._cast(_6434.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6453
            
            return self._parent._cast(_6453.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6401
            
            return self._parent._cast(_6401.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
            
            return self._parent._cast(_6455.PartCompoundDynamicAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2520.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6316.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6316.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis(self)
