﻿"""_6766.py

WormGearMeshCompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6701
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'WormGearMeshCompoundCriticalSpeedAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6637


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshCompoundCriticalSpeedAnalysis',)


class WormGearMeshCompoundCriticalSpeedAnalysis(_6701.GearMeshCompoundCriticalSpeedAnalysis):
    """WormGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_WormGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting WormGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'WormGearMeshCompoundCriticalSpeedAnalysis'):
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
        def worm_gear_mesh_compound_critical_speed_analysis(self) -> 'WormGearMeshCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2312.WormGearMesh':
        """WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2312.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6637.WormGearMeshCriticalSpeedAnalysis]':
        """List[WormGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6637.WormGearMeshCriticalSpeedAnalysis]':
        """List[WormGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearMeshCompoundCriticalSpeedAnalysis._Cast_WormGearMeshCompoundCriticalSpeedAnalysis':
        return self._Cast_WormGearMeshCompoundCriticalSpeedAnalysis(self)
