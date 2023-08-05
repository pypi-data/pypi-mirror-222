"""_4251.py

StraightBevelDiffGearMeshCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'StraightBevelDiffGearMeshCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.power_flows import _4120


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshCompoundPowerFlow',)


class StraightBevelDiffGearMeshCompoundPowerFlow(_4162.BevelGearMeshCompoundPowerFlow):
    """StraightBevelDiffGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_POWER_FLOW

    class _Cast_StraightBevelDiffGearMeshCompoundPowerFlow:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMeshCompoundPowerFlow'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_power_flow(self):
            return self._parent._cast(_4162.BevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4150
            
            return self._parent._cast(_4150.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4178
            
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
        def straight_bevel_diff_gear_mesh_compound_power_flow(self) -> 'StraightBevelDiffGearMeshCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2308.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2308.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4120.StraightBevelDiffGearMeshPowerFlow]':
        """List[StraightBevelDiffGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4120.StraightBevelDiffGearMeshPowerFlow]':
        """List[StraightBevelDiffGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMeshCompoundPowerFlow._Cast_StraightBevelDiffGearMeshCompoundPowerFlow':
        return self._Cast_StraightBevelDiffGearMeshCompoundPowerFlow(self)
