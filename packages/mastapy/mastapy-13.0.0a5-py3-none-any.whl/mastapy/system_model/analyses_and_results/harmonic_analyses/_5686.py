"""_5686.py

ConicalGearMeshHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ConicalGearMeshHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2290
    from mastapy.system_model.analyses_and_results.system_deflections import _2706


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshHarmonicAnalysis',)


class ConicalGearMeshHarmonicAnalysis(_5727.GearMeshHarmonicAnalysis):
    """ConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_HARMONIC_ANALYSIS

    class _Cast_ConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshHarmonicAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(self):
            return self._parent._cast(_5727.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
            
            return self._parent._cast(_5744.InterMountableComponentConnectionHarmonicAnalysis)

        @property
        def connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
            
            return self._parent._cast(_5688.ConnectionHarmonicAnalysis)

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
        def agma_gleason_conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5657
            
            return self._parent._cast(_5657.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5669
            
            return self._parent._cast(_5669.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
            
            return self._parent._cast(_5742.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5746
            
            return self._parent._cast(_5746.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5749
            
            return self._parent._cast(_5749.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5752
            
            return self._parent._cast(_5752.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
            
            return self._parent._cast(_5783.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5790
            
            return self._parent._cast(_5790.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
            
            return self._parent._cast(_5793.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5812
            
            return self._parent._cast(_5812.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(self) -> 'ConicalGearMeshHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2290.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearMeshHarmonicAnalysis]':
        """List[ConicalGearMeshHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_deflection_results(self) -> '_2706.ConicalGearMeshSystemDeflection':
        """ConicalGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis':
        return self._Cast_ConicalGearMeshHarmonicAnalysis(self)
