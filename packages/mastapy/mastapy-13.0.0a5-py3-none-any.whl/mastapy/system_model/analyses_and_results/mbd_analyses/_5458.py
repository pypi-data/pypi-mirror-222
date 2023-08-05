"""_5458.py

ShaftHubConnectionMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ShaftHubConnectionMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5498, _5500


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionMultibodyDynamicsAnalysis',)


class ShaftHubConnectionMultibodyDynamicsAnalysis(_5389.ConnectorMultibodyDynamicsAnalysis):
    """ShaftHubConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ShaftHubConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftHubConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ShaftHubConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def connector_multibody_dynamics_analysis(self):
            return self._parent._cast(_5389.ConnectorMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
            
            return self._parent._cast(_5438.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378
            
            return self._parent._cast(_5378.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
            
            return self._parent._cast(_5440.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7515
            
            return self._parent._cast(_7515.PartTimeSeriesLoadAnalysisCase)

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
        def shaft_hub_connection_multibody_dynamics_analysis(self) -> 'ShaftHubConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force(self) -> 'Vector3D':
        """Vector3D: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def force_angular(self) -> 'Vector3D':
        """Vector3D: 'ForceAngular' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def relative_angular_displacement(self) -> 'Vector3D':
        """Vector3D: 'RelativeAngularDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAngularDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def relative_linear_displacement(self) -> 'Vector3D':
        """Vector3D: 'RelativeLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def component_design(self) -> '_2580.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6917.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_dynamic_force(self) -> '_5498.DynamicForceVector3DResult':
        """DynamicForceVector3DResult: 'PeakDynamicForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakDynamicForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_dynamic_force_angular(self) -> '_5500.DynamicTorqueVector3DResult':
        """DynamicTorqueVector3DResult: 'PeakDynamicForceAngular' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakDynamicForceAngular

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionMultibodyDynamicsAnalysis]':
        """List[ShaftHubConnectionMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis':
        return self._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis(self)
