"""_6675.py

ConicalGearMeshCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'ConicalGearMeshCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshCompoundCriticalSpeedAnalysis',)


class ConicalGearMeshCompoundCriticalSpeedAnalysis(_6701.GearMeshCompoundCriticalSpeedAnalysis):
    """ConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_compound_critical_speed_analysis(self):
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
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6647
            
            return self._parent._cast(_6647.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6654
            
            return self._parent._cast(_6654.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6659
            
            return self._parent._cast(_6659.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6705
            
            return self._parent._cast(_6705.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6709
            
            return self._parent._cast(_6709.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6712
            
            return self._parent._cast(_6712.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6715
            
            return self._parent._cast(_6715.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6742
            
            return self._parent._cast(_6742.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6748
            
            return self._parent._cast(_6748.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6751
            
            return self._parent._cast(_6751.StraightBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6769
            
            return self._parent._cast(_6769.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(self) -> 'ConicalGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearMeshCompoundCriticalSpeedAnalysis]':
        """List[ConicalGearMeshCompoundCriticalSpeedAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6544.ConicalGearMeshCriticalSpeedAnalysis]':
        """List[ConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6544.ConicalGearMeshCriticalSpeedAnalysis]':
        """List[ConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshCompoundCriticalSpeedAnalysis._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_ConicalGearMeshCompoundCriticalSpeedAnalysis(self)
