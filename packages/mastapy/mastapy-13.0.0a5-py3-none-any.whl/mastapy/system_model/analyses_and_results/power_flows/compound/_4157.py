"""_4157.py

BevelDifferentialGearMeshCompoundPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BevelDifferentialGearMeshCompoundPowerFlow')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2284
    from mastapy.system_model.analyses_and_results.power_flows import _4023


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearMeshCompoundPowerFlow',)


class BevelDifferentialGearMeshCompoundPowerFlow(_4162.BevelGearMeshCompoundPowerFlow):
    """BevelDifferentialGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_POWER_FLOW

    class _Cast_BevelDifferentialGearMeshCompoundPowerFlow:
        """Special nested class for casting BevelDifferentialGearMeshCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearMeshCompoundPowerFlow'):
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
        def bevel_differential_gear_mesh_compound_power_flow(self) -> 'BevelDifferentialGearMeshCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2284.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2284.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4023.BevelDifferentialGearMeshPowerFlow]':
        """List[BevelDifferentialGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4023.BevelDifferentialGearMeshPowerFlow]':
        """List[BevelDifferentialGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearMeshCompoundPowerFlow._Cast_BevelDifferentialGearMeshCompoundPowerFlow':
        return self._Cast_BevelDifferentialGearMeshCompoundPowerFlow(self)
