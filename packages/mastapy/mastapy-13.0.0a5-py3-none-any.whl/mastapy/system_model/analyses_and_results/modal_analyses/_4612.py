"""_4612.py

GearMeshModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'GearMeshModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296
    from mastapy.system_model.analyses_and_results.system_deflections import _2741


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshModalAnalysis',)


class GearMeshModalAnalysis(_4619.InterMountableComponentConnectionModalAnalysis):
    """GearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS

    class _Cast_GearMeshModalAnalysis:
        """Special nested class for casting GearMeshModalAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshModalAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(self):
            return self._parent._cast(_4619.InterMountableComponentConnectionModalAnalysis)

        @property
        def connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585
            
            return self._parent._cast(_4585.ConnectionModalAnalysis)

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
        def agma_gleason_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4554
            
            return self._parent._cast(_4554.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4561
            
            return self._parent._cast(_4561.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4566
            
            return self._parent._cast(_4566.BevelGearMeshModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579
            
            return self._parent._cast(_4579.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582
            
            return self._parent._cast(_4582.ConicalGearMeshModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598
            
            return self._parent._cast(_4598.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606
            
            return self._parent._cast(_4606.FaceGearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616
            
            return self._parent._cast(_4616.HypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620
            
            return self._parent._cast(_4620.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623
            
            return self._parent._cast(_4623.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626
            
            return self._parent._cast(_4626.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659
            
            return self._parent._cast(_4659.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665
            
            return self._parent._cast(_4665.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668
            
            return self._parent._cast(_4668.StraightBevelGearMeshModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686
            
            return self._parent._cast(_4686.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689
            
            return self._parent._cast(_4689.ZerolBevelGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(self) -> 'GearMeshModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2296.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2741.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshModalAnalysis._Cast_GearMeshModalAnalysis':
        return self._Cast_GearMeshModalAnalysis(self)
