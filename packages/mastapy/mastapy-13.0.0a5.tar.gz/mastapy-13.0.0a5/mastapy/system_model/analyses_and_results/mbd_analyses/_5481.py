﻿"""_5481.py

TorqueConverterConnectionMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'TorqueConverterConnectionMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
    from mastapy.system_model.connections_and_sockets.couplings import _2335
    from mastapy.system_model.analyses_and_results.static_loads import _6940


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionMultibodyDynamicsAnalysis',)


class TorqueConverterConnectionMultibodyDynamicsAnalysis(_5390.CouplingConnectionMultibodyDynamicsAnalysis):
    """TorqueConverterConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterConnectionMultibodyDynamicsAnalysis'):
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
        def torque_converter_connection_multibody_dynamics_analysis(self) -> 'TorqueConverterConnectionMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def capacity_factor_k(self) -> 'float':
        """float: 'CapacityFactorK' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CapacityFactorK

        if temp is None:
            return 0.0

        return temp

    @property
    def inverse_capacity_factor_1k(self) -> 'float':
        """float: 'InverseCapacityFactor1K' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InverseCapacityFactor1K

        if temp is None:
            return 0.0

        return temp

    @property
    def is_locked(self) -> 'bool':
        """bool: 'IsLocked' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLocked

        if temp is None:
            return False

        return temp

    @property
    def lock_up_clutch_temperature(self) -> 'float':
        """float: 'LockUpClutchTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LockUpClutchTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def lock_up_viscous_torque(self) -> 'float':
        """float: 'LockUpViscousTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LockUpViscousTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locked_torque(self) -> 'float':
        """float: 'LockedTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LockedTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def locking_status(self) -> '_5485.TorqueConverterStatus':
        """TorqueConverterStatus: 'LockingStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LockingStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.TorqueConverterStatus')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.mbd_analyses._5485', 'TorqueConverterStatus')(value) if value is not None else None

    @property
    def percentage_applied_pressure(self) -> 'float':
        """float: 'PercentageAppliedPressure' is the original name of this property."""

        temp = self.wrapped.PercentageAppliedPressure

        if temp is None:
            return 0.0

        return temp

    @percentage_applied_pressure.setter
    def percentage_applied_pressure(self, value: 'float'):
        self.wrapped.PercentageAppliedPressure = float(value) if value is not None else 0.0

    @property
    def power_loss(self) -> 'float':
        """float: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def pump_torque(self) -> 'float':
        """float: 'PumpTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PumpTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_ratio(self) -> 'float':
        """float: 'SpeedRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio(self) -> 'float':
        """float: 'TorqueRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def turbine_torque(self) -> 'float':
        """float: 'TurbineTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TurbineTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2335.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6940.TorqueConverterConnectionLoadCase':
        """TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterConnectionMultibodyDynamicsAnalysis._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis':
        return self._Cast_TorqueConverterConnectionMultibodyDynamicsAnalysis(self)
