"""_4012.py

AbstractAssemblyPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4092
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AbstractAssemblyPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2417


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyPowerFlow',)


class AbstractAssemblyPowerFlow(_4092.PartPowerFlow):
    """AbstractAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_POWER_FLOW

    class _Cast_AbstractAssemblyPowerFlow:
        """Special nested class for casting AbstractAssemblyPowerFlow to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyPowerFlow'):
            self._parent = parent

        @property
        def part_power_flow(self):
            return self._parent._cast(_4092.PartPowerFlow)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4018
            
            return self._parent._cast(_4018.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4019
            
            return self._parent._cast(_4019.AssemblyPowerFlow)

        @property
        def belt_drive_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4025
            
            return self._parent._cast(_4025.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4030
            
            return self._parent._cast(_4030.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4031
            
            return self._parent._cast(_4031.BoltedJointPowerFlow)

        @property
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4035
            
            return self._parent._cast(_4035.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4040
            
            return self._parent._cast(_4040.ConceptCouplingPowerFlow)

        @property
        def concept_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConceptGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4046
            
            return self._parent._cast(_4046.ConicalGearSetPowerFlow)

        @property
        def coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4051
            
            return self._parent._cast(_4051.CouplingPowerFlow)

        @property
        def cvt_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4053
            
            return self._parent._cast(_4053.CVTPowerFlow)

        @property
        def cycloidal_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4055
            
            return self._parent._cast(_4055.CycloidalAssemblyPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4062
            
            return self._parent._cast(_4062.CylindricalGearSetPowerFlow)

        @property
        def face_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4068
            
            return self._parent._cast(_4068.FaceGearSetPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4073
            
            return self._parent._cast(_4073.GearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4077
            
            return self._parent._cast(_4077.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4081
            
            return self._parent._cast(_4081.KlingelnbergCycloPalloidConicalGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4084
            
            return self._parent._cast(_4084.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4095
            
            return self._parent._cast(_4095.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4097
            
            return self._parent._cast(_4097.PlanetaryGearSetPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4106
            
            return self._parent._cast(_4106.RollingRingAssemblyPowerFlow)

        @property
        def root_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4109
            
            return self._parent._cast(_4109.RootAssemblyPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4125
            
            return self._parent._cast(_4125.StraightBevelGearSetPowerFlow)

        @property
        def synchroniser_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4130
            
            return self._parent._cast(_4130.SynchroniserPowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4134
            
            return self._parent._cast(_4134.TorqueConverterPowerFlow)

        @property
        def worm_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4144
            
            return self._parent._cast(_4144.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_power_flow(self) -> 'AbstractAssemblyPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2417.AbstractAssembly':
        """AbstractAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2417.AbstractAssembly':
        """AbstractAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractAssemblyPowerFlow._Cast_AbstractAssemblyPowerFlow':
        return self._Cast_AbstractAssemblyPowerFlow(self)
