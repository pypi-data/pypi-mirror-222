﻿"""_5423.py

InterMountableComponentConnectionMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'InterMountableComponentConnectionMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2264


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionMultibodyDynamicsAnalysis',)


class InterMountableComponentConnectionMultibodyDynamicsAnalysis(_5388.ConnectionMultibodyDynamicsAnalysis):
    """InterMountableComponentConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_InterMountableComponentConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting InterMountableComponentConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5388.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.ConnectionTimeSeriesLoadAnalysisCase)

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
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5354
            
            return self._parent._cast(_5354.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5361
            
            return self._parent._cast(_5361.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5363
            
            return self._parent._cast(_5363.BevelDifferentialGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5368
            
            return self._parent._cast(_5368.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5373
            
            return self._parent._cast(_5373.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379
            
            return self._parent._cast(_5379.ConceptCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382
            
            return self._parent._cast(_5382.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
            
            return self._parent._cast(_5385.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
            
            return self._parent._cast(_5390.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393
            
            return self._parent._cast(_5393.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
            
            return self._parent._cast(_5400.CylindricalGearMeshMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406
            
            return self._parent._cast(_5406.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
            
            return self._parent._cast(_5411.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416
            
            return self._parent._cast(_5416.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
            
            return self._parent._cast(_5424.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427
            
            return self._parent._cast(_5427.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
            
            return self._parent._cast(_5430.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
            
            return self._parent._cast(_5441.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451
            
            return self._parent._cast(_5451.RingPinsToDiscConnectionMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453
            
            return self._parent._cast(_5453.RollingRingConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
            
            return self._parent._cast(_5463.SpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def spring_damper_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
            
            return self._parent._cast(_5466.SpringDamperConnectionMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469
            
            return self._parent._cast(_5469.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472
            
            return self._parent._cast(_5472.StraightBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def torque_converter_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481
            
            return self._parent._cast(_5481.TorqueConverterConnectionMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490
            
            return self._parent._cast(_5490.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493
            
            return self._parent._cast(_5493.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self) -> 'InterMountableComponentConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionMultibodyDynamicsAnalysis.TYPE'):
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
    def cast_to(self) -> 'InterMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionMultibodyDynamicsAnalysis':
        return self._Cast_InterMountableComponentConnectionMultibodyDynamicsAnalysis(self)
