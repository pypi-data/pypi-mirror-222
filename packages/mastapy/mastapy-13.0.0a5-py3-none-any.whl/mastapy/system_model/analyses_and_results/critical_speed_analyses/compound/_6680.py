"""_6680.py

CouplingConnectionCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6707
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CouplingConnectionCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6548


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundCriticalSpeedAnalysis',)


class CouplingConnectionCompoundCriticalSpeedAnalysis(_6707.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis):
    """CouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            return self._parent._cast(_6707.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6677
            
            return self._parent._cast(_6677.ConnectionCompoundCriticalSpeedAnalysis)

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
        def clutch_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6664
            
            return self._parent._cast(_6664.ClutchConnectionCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6669
            
            return self._parent._cast(_6669.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6723
            
            return self._parent._cast(_6723.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6745
            
            return self._parent._cast(_6745.SpringDamperConnectionCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6760
            
            return self._parent._cast(_6760.TorqueConverterConnectionCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(self) -> 'CouplingConnectionCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6548.CouplingConnectionCriticalSpeedAnalysis]':
        """List[CouplingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6548.CouplingConnectionCriticalSpeedAnalysis]':
        """List[CouplingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis':
        return self._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis(self)
