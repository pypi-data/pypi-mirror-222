"""_4120.py

StraightBevelDiffGearMeshPowerFlow
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4028
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'StraightBevelDiffGearMeshPowerFlow')

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel_diff import _396
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.static_loads import _6928


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshPowerFlow',)


class StraightBevelDiffGearMeshPowerFlow(_4028.BevelGearMeshPowerFlow):
    """StraightBevelDiffGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_POWER_FLOW

    class _Cast_StraightBevelDiffGearMeshPowerFlow:
        """Special nested class for casting StraightBevelDiffGearMeshPowerFlow to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMeshPowerFlow'):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(self):
            return self._parent._cast(_4028.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4016
            
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
        def straight_bevel_diff_gear_mesh_power_flow(self) -> 'StraightBevelDiffGearMeshPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_396.StraightBevelDiffGearMeshRating':
        """StraightBevelDiffGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_396.StraightBevelDiffGearMeshRating':
        """StraightBevelDiffGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

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
    def connection_load_case(self) -> '_6928.StraightBevelDiffGearMeshLoadCase':
        """StraightBevelDiffGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMeshPowerFlow._Cast_StraightBevelDiffGearMeshPowerFlow':
        return self._Cast_StraightBevelDiffGearMeshPowerFlow(self)
