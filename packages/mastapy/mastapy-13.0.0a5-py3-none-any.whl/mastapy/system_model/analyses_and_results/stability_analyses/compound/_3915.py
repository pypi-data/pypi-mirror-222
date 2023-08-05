"""_3915.py

CouplingConnectionCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CouplingConnectionCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3782


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundStabilityAnalysis',)


class CouplingConnectionCompoundStabilityAnalysis(_3942.InterMountableComponentConnectionCompoundStabilityAnalysis):
    """CouplingConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS

    class _Cast_CouplingConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CouplingConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            return self._parent._cast(_3942.InterMountableComponentConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3912
            
            return self._parent._cast(_3912.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3899
            
            return self._parent._cast(_3899.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3904
            
            return self._parent._cast(_3904.ConceptCouplingConnectionCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3958
            
            return self._parent._cast(_3958.PartToPartShearCouplingConnectionCompoundStabilityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3980
            
            return self._parent._cast(_3980.SpringDamperConnectionCompoundStabilityAnalysis)

        @property
        def torque_converter_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3995
            
            return self._parent._cast(_3995.TorqueConverterConnectionCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(self) -> 'CouplingConnectionCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3782.CouplingConnectionStabilityAnalysis]':
        """List[CouplingConnectionStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3782.CouplingConnectionStabilityAnalysis]':
        """List[CouplingConnectionStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundStabilityAnalysis._Cast_CouplingConnectionCompoundStabilityAnalysis':
        return self._Cast_CouplingConnectionCompoundStabilityAnalysis(self)
