"""_4150.py

AGMAGleasonConicalGearMeshCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'AGMAGleasonConicalGearMeshCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4016


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundPowerFlow',)


class AGMAGleasonConicalGearMeshCompoundPowerFlow(_4178.ConicalGearMeshCompoundPowerFlow):
    """AGMAGleasonConicalGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW

    class _Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundPowerFlow'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_power_flow(self):
            return self._parent._cast(_4178.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4204
            
            return self._parent._cast(_4204.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
            
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
        def bevel_differential_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4157
            
            return self._parent._cast(_4157.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
            
            return self._parent._cast(_4162.BevelGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4208
            
            return self._parent._cast(_4208.HypoidGearMeshCompoundPowerFlow)

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
        def zerol_bevel_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4272
            
            return self._parent._cast(_4272.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(self) -> 'AGMAGleasonConicalGearMeshCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4016.AGMAGleasonConicalGearMeshPowerFlow]':
        """List[AGMAGleasonConicalGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4016.AGMAGleasonConicalGearMeshPowerFlow]':
        """List[AGMAGleasonConicalGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundPowerFlow._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundPowerFlow(self)
