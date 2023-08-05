"""_5669.py

BevelGearMeshHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BevelGearMeshHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2286
    from mastapy.system_model.analyses_and_results.system_deflections import _2688


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMeshHarmonicAnalysis',)


class BevelGearMeshHarmonicAnalysis(_5657.AGMAGleasonConicalGearMeshHarmonicAnalysis):
    """BevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_HARMONIC_ANALYSIS

    class _Cast_BevelGearMeshHarmonicAnalysis:
        """Special nested class for casting BevelGearMeshHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'BevelGearMeshHarmonicAnalysis'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(self):
            return self._parent._cast(_5657.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
            
            return self._parent._cast(_5686.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
            
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
        def bevel_differential_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialGearMeshHarmonicAnalysis)

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
        def bevel_gear_mesh_harmonic_analysis(self) -> 'BevelGearMeshHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearMeshHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2286.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2688.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearMeshHarmonicAnalysis._Cast_BevelGearMeshHarmonicAnalysis':
        return self._Cast_BevelGearMeshHarmonicAnalysis(self)
