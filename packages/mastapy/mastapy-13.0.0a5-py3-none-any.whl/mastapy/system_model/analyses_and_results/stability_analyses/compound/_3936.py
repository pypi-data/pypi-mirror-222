"""_3936.py

GearMeshCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'GearMeshCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3804


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundStabilityAnalysis',)


class GearMeshCompoundStabilityAnalysis(_3942.InterMountableComponentConnectionCompoundStabilityAnalysis):
    """GearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STABILITY_ANALYSIS

    class _Cast_GearMeshCompoundStabilityAnalysis:
        """Special nested class for casting GearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundStabilityAnalysis'):
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
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3882
            
            return self._parent._cast(_3882.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3889
            
            return self._parent._cast(_3889.BevelDifferentialGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3894
            
            return self._parent._cast(_3894.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3907
            
            return self._parent._cast(_3907.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
            
            return self._parent._cast(_3910.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3925
            
            return self._parent._cast(_3925.CylindricalGearMeshCompoundStabilityAnalysis)

        @property
        def face_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3931
            
            return self._parent._cast(_3931.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3940
            
            return self._parent._cast(_3940.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3944
            
            return self._parent._cast(_3944.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3947
            
            return self._parent._cast(_3947.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3950
            
            return self._parent._cast(_3950.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3977
            
            return self._parent._cast(_3977.SpiralBevelGearMeshCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3983
            
            return self._parent._cast(_3983.StraightBevelDiffGearMeshCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3986
            
            return self._parent._cast(_3986.StraightBevelGearMeshCompoundStabilityAnalysis)

        @property
        def worm_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4001
            
            return self._parent._cast(_4001.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4004
            
            return self._parent._cast(_4004.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(self) -> 'GearMeshCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3804.GearMeshStabilityAnalysis]':
        """List[GearMeshStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3804.GearMeshStabilityAnalysis]':
        """List[GearMeshStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis':
        return self._Cast_GearMeshCompoundStabilityAnalysis(self)
