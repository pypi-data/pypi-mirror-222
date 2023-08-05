"""_5033.py

KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5030
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2302
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4903


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness',)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness(_5030.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5030.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4996
            
            return self._parent._cast(_4996.ConicalGearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5022
            
            return self._parent._cast(_5022.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5028
            
            return self._parent._cast(_5028.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4998
            
            return self._parent._cast(_4998.ConnectionCompoundModalAnalysisAtAStiffness)

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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2302.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2302.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4903.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4903.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness(self)
