"""_6405.py

ConceptGearCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ConceptGearCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2503
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6275


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundDynamicAnalysis',)


class ConceptGearCompoundDynamicAnalysis(_6434.GearCompoundDynamicAnalysis):
    """ConceptGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_ConceptGearCompoundDynamicAnalysis:
        """Special nested class for casting ConceptGearCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptGearCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def gear_compound_dynamic_analysis(self):
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
        def concept_gear_compound_dynamic_analysis(self) -> 'ConceptGearCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2503.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6275.ConceptGearDynamicAnalysis]':
        """List[ConceptGearDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6275.ConceptGearDynamicAnalysis]':
        """List[ConceptGearDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearCompoundDynamicAnalysis._Cast_ConceptGearCompoundDynamicAnalysis':
        return self._Cast_ConceptGearCompoundDynamicAnalysis(self)
