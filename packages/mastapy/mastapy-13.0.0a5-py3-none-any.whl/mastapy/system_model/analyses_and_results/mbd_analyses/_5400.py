﻿"""_5400.py

CylindricalGearMeshMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'CylindricalGearMeshMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2292
    from mastapy.system_model.analyses_and_results.static_loads import _6831


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshMultibodyDynamicsAnalysis',)


class CylindricalGearMeshMultibodyDynamicsAnalysis(_5411.GearMeshMultibodyDynamicsAnalysis):
    """CylindricalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CylindricalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(self):
            return self._parent._cast(_5411.GearMeshMultibodyDynamicsAnalysis)

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
        def cylindrical_gear_mesh_multibody_dynamics_analysis(self) -> 'CylindricalGearMeshMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stress_gear_a_left_flank(self) -> 'float':
        """float: 'ContactStressGearALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_a_right_flank(self) -> 'float':
        """float: 'ContactStressGearARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_b_left_flank(self) -> 'float':
        """float: 'ContactStressGearBLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_gear_b_right_flank(self) -> 'float':
        """float: 'ContactStressGearBRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance_left_flank(self) -> 'float':
        """float: 'RollDistanceLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollDistanceLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def roll_distance_right_flank(self) -> 'float':
        """float: 'RollDistanceRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollDistanceRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_a_left_flank(self) -> 'float':
        """float: 'ToothRootStressGearALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_a_right_flank(self) -> 'float':
        """float: 'ToothRootStressGearARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_b_left_flank(self) -> 'float':
        """float: 'ToothRootStressGearBLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_gear_b_right_flank(self) -> 'float':
        """float: 'ToothRootStressGearBRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2292.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6831.CylindricalGearMeshLoadCase':
        """CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshMultibodyDynamicsAnalysis]':
        """List[CylindricalGearMeshMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMeshMultibodyDynamicsAnalysis._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis':
        return self._Cast_CylindricalGearMeshMultibodyDynamicsAnalysis(self)
