﻿"""_4831.py

ZerolBevelGearMeshCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4721
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ZerolBevelGearMeshCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2314
    from mastapy.system_model.analyses_and_results.modal_analyses import _4689


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshCompoundModalAnalysis',)


class ZerolBevelGearMeshCompoundModalAnalysis(_4721.BevelGearMeshCompoundModalAnalysis):
    """ZerolBevelGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS

    class _Cast_ZerolBevelGearMeshCompoundModalAnalysis:
        """Special nested class for casting ZerolBevelGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshCompoundModalAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis(self):
            return self._parent._cast(_4721.BevelGearMeshCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4709
            
            return self._parent._cast(_4709.AGMAGleasonConicalGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4737
            
            return self._parent._cast(_4737.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
            
            return self._parent._cast(_4763.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4769
            
            return self._parent._cast(_4769.InterMountableComponentConnectionCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
            
            return self._parent._cast(_4739.ConnectionCompoundModalAnalysis)

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
        def zerol_bevel_gear_mesh_compound_modal_analysis(self) -> 'ZerolBevelGearMeshCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2314.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2314.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4689.ZerolBevelGearMeshModalAnalysis]':
        """List[ZerolBevelGearMeshModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4689.ZerolBevelGearMeshModalAnalysis]':
        """List[ZerolBevelGearMeshModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearMeshCompoundModalAnalysis._Cast_ZerolBevelGearMeshCompoundModalAnalysis':
        return self._Cast_ZerolBevelGearMeshCompoundModalAnalysis(self)
