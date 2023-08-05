"""_3986.py

StraightBevelGearMeshCompoundStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'StraightBevelGearMeshCompoundStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.system_model.analyses_and_results.stability_analyses import _3856


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshCompoundStabilityAnalysis',)


class StraightBevelGearMeshCompoundStabilityAnalysis(_3894.BevelGearMeshCompoundStabilityAnalysis):
    """StraightBevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS

    class _Cast_StraightBevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelGearMeshCompoundStabilityAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(self):
            return self._parent._cast(_3894.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3882
            
            return self._parent._cast(_3882.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
            
            return self._parent._cast(_3910.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
            
            return self._parent._cast(_3936.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3942
            
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
        def straight_bevel_gear_mesh_compound_stability_analysis(self) -> 'StraightBevelGearMeshCompoundStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2310.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2310.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3856.StraightBevelGearMeshStabilityAnalysis]':
        """List[StraightBevelGearMeshStabilityAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_3856.StraightBevelGearMeshStabilityAnalysis]':
        """List[StraightBevelGearMeshStabilityAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis':
        return self._Cast_StraightBevelGearMeshCompoundStabilityAnalysis(self)
