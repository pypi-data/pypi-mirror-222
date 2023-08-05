"""_5361.py

BeltConnectionMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BeltConnectionMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _74
    from mastapy.system_model.connections_and_sockets import _2251
    from mastapy.system_model.analyses_and_results.static_loads import _6788


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionMultibodyDynamicsAnalysis',)


class BeltConnectionMultibodyDynamicsAnalysis(_5423.InterMountableComponentConnectionMultibodyDynamicsAnalysis):
    """BeltConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_BeltConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting BeltConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'BeltConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5423.InterMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388
            
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
        def cvt_belt_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393
            
            return self._parent._cast(_5393.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def belt_connection_multibody_dynamics_analysis(self) -> 'BeltConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extension(self) -> 'float':
        """float: 'Extension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Extension

        if temp is None:
            return 0.0

        return temp

    @property
    def loading_status(self) -> '_74.LoadingStatus':
        """LoadingStatus: 'LoadingStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadingStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.LoadingStatus')
        return constructor.new_from_mastapy('mastapy.nodal_analysis._74', 'LoadingStatus')(value) if value is not None else None

    @property
    def tension(self) -> 'float':
        """float: 'Tension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tension

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2251.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6788.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltConnectionMultibodyDynamicsAnalysis._Cast_BeltConnectionMultibodyDynamicsAnalysis':
        return self._Cast_BeltConnectionMultibodyDynamicsAnalysis(self)
