"""_6678.py

ConnectorCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6719
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'ConnectorCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundCriticalSpeedAnalysis',)


class ConnectorCompoundCriticalSpeedAnalysis(_6719.MountableComponentCompoundCriticalSpeedAnalysis):
    """ConnectorCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_ConnectorCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConnectorCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ConnectorCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(self):
            return self._parent._cast(_6719.MountableComponentCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6667
            
            return self._parent._cast(_6667.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6721
            
            return self._parent._cast(_6721.PartCompoundCriticalSpeedAnalysis)

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
        def bearing_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6650
            
            return self._parent._cast(_6650.BearingCompoundCriticalSpeedAnalysis)

        @property
        def oil_seal_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6720
            
            return self._parent._cast(_6720.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6738
            
            return self._parent._cast(_6738.ShaftHubConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(self) -> 'ConnectorCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6547.ConnectorCriticalSpeedAnalysis]':
        """List[ConnectorCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6547.ConnectorCriticalSpeedAnalysis]':
        """List[ConnectorCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConnectorCompoundCriticalSpeedAnalysis._Cast_ConnectorCompoundCriticalSpeedAnalysis':
        return self._Cast_ConnectorCompoundCriticalSpeedAnalysis(self)
