"""_6447.py

KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6444
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6445, _6446


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis(_6444.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(self):
            return self._parent._cast(_6444.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6410
            
            return self._parent._cast(_6410.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6436
            
            return self._parent._cast(_6436.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6474
            
            return self._parent._cast(_6474.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6376
            
            return self._parent._cast(_6376.AbstractAssemblyCompoundDynamicAnalysis)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2521.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2521.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6318.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_dynamic_analysis(self) -> 'List[_6445.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_dynamic_analysis(self) -> 'List[_6446.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6318.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis(self)
