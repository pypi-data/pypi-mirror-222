"""_6709.py

KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6675
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis',)


class KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis(_6675.ConicalGearMeshCompoundCriticalSpeedAnalysis):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self):
            return self._parent._cast(_6675.ConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
            
            return self._parent._cast(_6701.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6707
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6712
            
            return self._parent._cast(_6712.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6715
            
            return self._parent._cast(_6715.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self) -> 'KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6580.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6580.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis]':
        """List[KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis(self)
