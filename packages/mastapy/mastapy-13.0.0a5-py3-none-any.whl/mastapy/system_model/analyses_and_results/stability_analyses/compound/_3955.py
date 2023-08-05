"""_3955.py

OilSealCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'OilSealCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.stability_analyses import _3824


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCompoundStabilityAnalysis',)


class OilSealCompoundStabilityAnalysis(_3913.ConnectorCompoundStabilityAnalysis):
    """OilSealCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_STABILITY_ANALYSIS

    class _Cast_OilSealCompoundStabilityAnalysis:
        """Special nested class for casting OilSealCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'OilSealCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def connector_compound_stability_analysis(self):
            return self._parent._cast(_3913.ConnectorCompoundStabilityAnalysis)

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
        def oil_seal_compound_stability_analysis(self) -> 'OilSealCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OilSealCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2449.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3824.OilSealStabilityAnalysis]':
        """List[OilSealStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3824.OilSealStabilityAnalysis]':
        """List[OilSealStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis':
        return self._Cast_OilSealCompoundStabilityAnalysis(self)
