"""_5371.py

BoltedJointMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BoltedJointMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2426
    from mastapy.system_model.analyses_and_results.static_loads import _6798


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointMultibodyDynamicsAnalysis',)


class BoltedJointMultibodyDynamicsAnalysis(_5462.SpecialisedAssemblyMultibodyDynamicsAnalysis):
    """BoltedJointMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_BoltedJointMultibodyDynamicsAnalysis:
        """Special nested class for casting BoltedJointMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'BoltedJointMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(self):
            return self._parent._cast(_5462.SpecialisedAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractAssemblyMultibodyDynamicsAnalysis)

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
        def bolted_joint_multibody_dynamics_analysis(self) -> 'BoltedJointMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2426.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6798.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis':
        return self._Cast_BoltedJointMultibodyDynamicsAnalysis(self)
