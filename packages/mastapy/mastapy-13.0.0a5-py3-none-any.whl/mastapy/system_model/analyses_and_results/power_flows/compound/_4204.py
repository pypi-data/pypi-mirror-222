"""_4204.py

GearMeshCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearMeshCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.gears.rating import _363
    from mastapy.system_model.analyses_and_results.power_flows import _4071


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundPowerFlow',)


class GearMeshCompoundPowerFlow(_4210.InterMountableComponentConnectionCompoundPowerFlow):
    """GearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_POWER_FLOW

    class _Cast_GearMeshCompoundPowerFlow:
        """Special nested class for casting GearMeshCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundPowerFlow'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(self):
            return self._parent._cast(_4210.InterMountableComponentConnectionCompoundPowerFlow)

        @property
        def connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
            
            return self._parent._cast(_4180.ConnectionCompoundPowerFlow)

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
        def agma_gleason_conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4150
            
            return self._parent._cast(_4150.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4157
            
            return self._parent._cast(_4157.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
            
            return self._parent._cast(_4162.BevelGearMeshCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4175
            
            return self._parent._cast(_4175.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4178
            
            return self._parent._cast(_4178.ConicalGearMeshCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4193
            
            return self._parent._cast(_4193.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4199
            
            return self._parent._cast(_4199.FaceGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4208
            
            return self._parent._cast(_4208.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4212
            
            return self._parent._cast(_4212.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4215
            
            return self._parent._cast(_4215.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4218
            
            return self._parent._cast(_4218.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4245
            
            return self._parent._cast(_4245.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4251
            
            return self._parent._cast(_4251.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4254
            
            return self._parent._cast(_4254.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4269
            
            return self._parent._cast(_4269.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4272
            
            return self._parent._cast(_4272.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(self) -> 'GearMeshCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_rating(self) -> '_363.MeshDutyCycleRating':
        """MeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases(self) -> 'List[_4071.GearMeshPowerFlow]':
        """List[GearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4071.GearMeshPowerFlow]':
        """List[GearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundPowerFlow._Cast_GearMeshCompoundPowerFlow':
        return self._Cast_GearMeshCompoundPowerFlow(self)
