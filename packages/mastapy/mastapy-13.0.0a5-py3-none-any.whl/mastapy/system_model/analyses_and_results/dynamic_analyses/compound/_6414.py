"""_6414.py

CouplingConnectionCompoundDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'CouplingConnectionCompoundDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundDynamicAnalysis',)


class CouplingConnectionCompoundDynamicAnalysis(_6441.InterMountableComponentConnectionCompoundDynamicAnalysis):
    """CouplingConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_CouplingConnectionCompoundDynamicAnalysis:
        """Special nested class for casting CouplingConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self):
            return self._parent._cast(_6441.InterMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6411
            
            return self._parent._cast(_6411.ConnectionCompoundDynamicAnalysis)

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
        def clutch_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6398
            
            return self._parent._cast(_6398.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6403
            
            return self._parent._cast(_6403.ConceptCouplingConnectionCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6457
            
            return self._parent._cast(_6457.PartToPartShearCouplingConnectionCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6479
            
            return self._parent._cast(_6479.SpringDamperConnectionCompoundDynamicAnalysis)

        @property
        def torque_converter_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6494
            
            return self._parent._cast(_6494.TorqueConverterConnectionCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(self) -> 'CouplingConnectionCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6283.CouplingConnectionDynamicAnalysis]':
        """List[CouplingConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6283.CouplingConnectionDynamicAnalysis]':
        """List[CouplingConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundDynamicAnalysis._Cast_CouplingConnectionCompoundDynamicAnalysis':
        return self._Cast_CouplingConnectionCompoundDynamicAnalysis(self)
