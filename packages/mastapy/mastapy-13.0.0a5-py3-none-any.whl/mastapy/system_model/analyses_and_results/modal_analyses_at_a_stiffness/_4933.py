"""_4933.py

SpiralBevelGearMeshModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'SpiralBevelGearMeshModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2306
    from mastapy.system_model.analyses_and_results.static_loads import _6922


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMeshModalAnalysisAtAStiffness',)


class SpiralBevelGearMeshModalAnalysisAtAStiffness(_4849.BevelGearMeshModalAnalysisAtAStiffness):
    """SpiralBevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_SpiralBevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting SpiralBevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearMeshModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4849.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4837
            
            return self._parent._cast(_4837.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4865
            
            return self._parent._cast(_4865.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4892
            
            return self._parent._cast(_4892.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4899
            
            return self._parent._cast(_4899.InterMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4868
            
            return self._parent._cast(_4868.ConnectionModalAnalysisAtAStiffness)

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
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(self) -> 'SpiralBevelGearMeshModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMeshModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2306.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6922.SpiralBevelGearMeshLoadCase':
        """SpiralBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpiralBevelGearMeshModalAnalysisAtAStiffness._Cast_SpiralBevelGearMeshModalAnalysisAtAStiffness':
        return self._Cast_SpiralBevelGearMeshModalAnalysisAtAStiffness(self)
