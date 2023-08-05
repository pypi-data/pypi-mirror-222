"""_4075.py

HypoidGearMeshPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4016
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'HypoidGearMeshPowerFlow')

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _436
    from mastapy.system_model.connections_and_sockets.gears import _2298
    from mastapy.system_model.analyses_and_results.static_loads import _6874


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshPowerFlow',)


class HypoidGearMeshPowerFlow(_4016.AGMAGleasonConicalGearMeshPowerFlow):
    """HypoidGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_POWER_FLOW

    class _Cast_HypoidGearMeshPowerFlow:
        """Special nested class for casting HypoidGearMeshPowerFlow to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshPowerFlow'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_power_flow(self):
            return self._parent._cast(_4016.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4044
            
            return self._parent._cast(_4044.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4071
            
            return self._parent._cast(_4071.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4078
            
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
        def hypoid_gear_mesh_power_flow(self) -> 'HypoidGearMeshPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_436.HypoidGearMeshRating':
        """HypoidGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_436.HypoidGearMeshRating':
        """HypoidGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2298.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6874.HypoidGearMeshLoadCase':
        """HypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HypoidGearMeshPowerFlow._Cast_HypoidGearMeshPowerFlow':
        return self._Cast_HypoidGearMeshPowerFlow(self)
