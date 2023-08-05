﻿"""_5379.py

ConceptCouplingConnectionMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ConceptCouplingConnectionMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6806


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionMultibodyDynamicsAnalysis',)


class ConceptCouplingConnectionMultibodyDynamicsAnalysis(_5390.CouplingConnectionMultibodyDynamicsAnalysis):
    """ConceptCouplingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ConceptCouplingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptCouplingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnectionMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5390.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
            
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
        def concept_coupling_connection_multibody_dynamics_analysis(self) -> 'ConceptCouplingConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def specified_speed_ratio(self) -> 'float':
        """float: 'SpecifiedSpeedRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedSpeedRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_torque_ratio(self) -> 'float':
        """float: 'SpecifiedTorqueRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedTorqueRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2327.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6806.ConceptCouplingConnectionLoadCase':
        """ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptCouplingConnectionMultibodyDynamicsAnalysis._Cast_ConceptCouplingConnectionMultibodyDynamicsAnalysis':
        return self._Cast_ConceptCouplingConnectionMultibodyDynamicsAnalysis(self)
