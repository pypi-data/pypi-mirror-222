"""_4071.py

GearMeshPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'GearMeshPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296
    from mastapy.gears.rating import _358
    from mastapy.system_model.analyses_and_results.power_flows import _4132


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshPowerFlow',)


class GearMeshPowerFlow(_4078.InterMountableComponentConnectionPowerFlow):
    """GearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_POWER_FLOW

    class _Cast_GearMeshPowerFlow:
        """Special nested class for casting GearMeshPowerFlow to subclasses."""

        def __init__(self, parent: 'GearMeshPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(self):
            return self._parent._cast(_4078.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.ConnectionPowerFlow)

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
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
            return self._parent._cast(_4016.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4023
            
            return self._parent._cast(_4023.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4028
            
            return self._parent._cast(_4028.BevelGearMeshPowerFlow)

        @property
        def concept_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4041
            
            return self._parent._cast(_4041.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConicalGearMeshPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4060
            
            return self._parent._cast(_4060.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4066
            
            return self._parent._cast(_4066.FaceGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4075
            
            return self._parent._cast(_4075.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4079
            
            return self._parent._cast(_4079.KlingelnbergCycloPalloidConicalGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4082
            
            return self._parent._cast(_4082.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow)

        @property
        def spiral_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4114
            
            return self._parent._cast(_4114.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4120
            
            return self._parent._cast(_4120.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4123
            
            return self._parent._cast(_4123.StraightBevelGearMeshPowerFlow)

        @property
        def worm_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4139
            
            return self._parent._cast(_4139.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4142
            
            return self._parent._cast(_4142.ZerolBevelGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self) -> 'GearMeshPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_tooth_passing_speed(self) -> 'float':
        """float: 'GearAToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_tooth_passing_speed(self) -> 'float':
        """float: 'GearBToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self) -> 'float':
        """float: 'ToothPassingFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

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
    def rating(self) -> '_358.GearMeshRating':
        """GearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_passing_harmonics(self) -> 'List[_4132.ToothPassingHarmonic]':
        """List[ToothPassingHarmonic]: 'ToothPassingHarmonics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshPowerFlow._Cast_GearMeshPowerFlow':
        return self._Cast_GearMeshPowerFlow(self)
