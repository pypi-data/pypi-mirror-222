"""_6619.py

StraightBevelDiffGearMeshCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6528
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'StraightBevelDiffGearMeshCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.static_loads import _6928


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshCriticalSpeedAnalysis',)


class StraightBevelDiffGearMeshCriticalSpeedAnalysis(_6528.BevelGearMeshCriticalSpeedAnalysis):
    """StraightBevelDiffGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_CRITICAL_SPEED_ANALYSIS

    class _Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMeshCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(self):
            return self._parent._cast(_6528.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6516
            
            return self._parent._cast(_6516.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6544
            
            return self._parent._cast(_6544.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
            
            return self._parent._cast(_6572.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6578
            
            return self._parent._cast(_6578.InterMountableComponentConnectionCriticalSpeedAnalysis)

        @property
        def connection_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
            
            return self._parent._cast(_6546.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(self) -> 'StraightBevelDiffGearMeshCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2308.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6928.StraightBevelDiffGearMeshLoadCase':
        """StraightBevelDiffGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis':
        return self._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis(self)
