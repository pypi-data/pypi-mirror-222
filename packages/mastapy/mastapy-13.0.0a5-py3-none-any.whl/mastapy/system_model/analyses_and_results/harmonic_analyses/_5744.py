﻿"""_5744.py

InterMountableComponentConnectionHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'InterMountableComponentConnectionHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2264
    from mastapy.system_model.analyses_and_results.system_deflections import _2749


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionHarmonicAnalysis',)


class InterMountableComponentConnectionHarmonicAnalysis(_5688.ConnectionHarmonicAnalysis):
    """InterMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS

    class _Cast_InterMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionHarmonicAnalysis'):
            self._parent = parent

        @property
        def connection_harmonic_analysis(self):
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
        def belt_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5661
            
            return self._parent._cast(_5661.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5664
            
            return self._parent._cast(_5664.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5669
            
            return self._parent._cast(_5669.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5673
            
            return self._parent._cast(_5673.ClutchConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5679
            
            return self._parent._cast(_5679.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5683
            
            return self._parent._cast(_5683.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5686
            
            return self._parent._cast(_5686.ConicalGearMeshHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5690
            
            return self._parent._cast(_5690.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
            
            return self._parent._cast(_5693.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5701
            
            return self._parent._cast(_5701.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5720
            
            return self._parent._cast(_5720.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
            
            return self._parent._cast(_5727.GearMeshHarmonicAnalysis)

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
        def part_to_part_shear_coupling_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
            
            return self._parent._cast(_5759.PartToPartShearCouplingConnectionHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
            
            return self._parent._cast(_5771.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
            
            return self._parent._cast(_5773.RollingRingConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
            
            return self._parent._cast(_5783.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5785
            
            return self._parent._cast(_5785.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5790
            
            return self._parent._cast(_5790.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5793
            
            return self._parent._cast(_5793.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5801
            
            return self._parent._cast(_5801.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5809
            
            return self._parent._cast(_5809.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5812
            
            return self._parent._cast(_5812.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(self) -> 'InterMountableComponentConnectionHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2264.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2749.InterMountableComponentConnectionSystemDeflection':
        """InterMountableComponentConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis':
        return self._Cast_InterMountableComponentConnectionHarmonicAnalysis(self)
