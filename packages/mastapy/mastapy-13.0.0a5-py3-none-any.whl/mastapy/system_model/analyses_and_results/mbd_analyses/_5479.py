"""_5479.py

SynchroniserPartMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5391
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'SynchroniserPartMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartMultibodyDynamicsAnalysis',)


class SynchroniserPartMultibodyDynamicsAnalysis(_5391.CouplingHalfMultibodyDynamicsAnalysis):
    """SynchroniserPartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_SynchroniserPartMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserPartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'SynchroniserPartMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(self):
            return self._parent._cast(_5391.CouplingHalfMultibodyDynamicsAnalysis)

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
        def synchroniser_half_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477
            
            return self._parent._cast(_5477.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480
            
            return self._parent._cast(_5480.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(self) -> 'SynchroniserPartMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2587.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis':
        return self._Cast_SynchroniserPartMultibodyDynamicsAnalysis(self)
