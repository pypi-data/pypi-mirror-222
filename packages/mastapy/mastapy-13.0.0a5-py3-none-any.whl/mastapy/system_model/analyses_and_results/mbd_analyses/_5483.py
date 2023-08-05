"""_5483.py

TorqueConverterMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'TorqueConverterMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6941


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterMultibodyDynamicsAnalysis',)


class TorqueConverterMultibodyDynamicsAnalysis(_5392.CouplingMultibodyDynamicsAnalysis):
    """TorqueConverterMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_TorqueConverterMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'TorqueConverterMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def coupling_multibody_dynamics_analysis(self):
            return self._parent._cast(_5392.CouplingMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
            
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
        def torque_converter_multibody_dynamics_analysis(self) -> 'TorqueConverterMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2589.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6941.TorqueConverterLoadCase':
        """TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'TorqueConverterMultibodyDynamicsAnalysis._Cast_TorqueConverterMultibodyDynamicsAnalysis':
        return self._Cast_TorqueConverterMultibodyDynamicsAnalysis(self)
