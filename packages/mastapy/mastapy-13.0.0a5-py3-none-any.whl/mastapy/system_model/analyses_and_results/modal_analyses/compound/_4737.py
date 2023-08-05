"""_4737.py

ConicalGearMeshCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ConicalGearMeshCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4582


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshCompoundModalAnalysis',)


class ConicalGearMeshCompoundModalAnalysis(_4763.GearMeshCompoundModalAnalysis):
    """ConicalGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS

    class _Cast_ConicalGearMeshCompoundModalAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshCompoundModalAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis(self):
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
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4709
            
            return self._parent._cast(_4709.AGMAGleasonConicalGearMeshCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4716
            
            return self._parent._cast(_4716.BevelDifferentialGearMeshCompoundModalAnalysis)

        @property
        def bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4721
            
            return self._parent._cast(_4721.BevelGearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4767
            
            return self._parent._cast(_4767.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4771
            
            return self._parent._cast(_4771.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4774
            
            return self._parent._cast(_4774.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4777
            
            return self._parent._cast(_4777.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4804
            
            return self._parent._cast(_4804.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4810
            
            return self._parent._cast(_4810.StraightBevelDiffGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
            
            return self._parent._cast(_4813.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4831
            
            return self._parent._cast(_4831.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(self) -> 'ConicalGearMeshCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearMeshCompoundModalAnalysis]':
        """List[ConicalGearMeshCompoundModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4582.ConicalGearMeshModalAnalysis]':
        """List[ConicalGearMeshModalAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4582.ConicalGearMeshModalAnalysis]':
        """List[ConicalGearMeshModalAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshCompoundModalAnalysis._Cast_ConicalGearMeshCompoundModalAnalysis':
        return self._Cast_ConicalGearMeshCompoundModalAnalysis(self)
