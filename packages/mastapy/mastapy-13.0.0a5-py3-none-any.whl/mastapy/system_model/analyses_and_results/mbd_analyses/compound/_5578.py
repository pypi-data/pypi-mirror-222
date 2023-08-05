"""_5578.py

MeasurementComponentCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'MeasurementComponentCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5437


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundMultibodyDynamicsAnalysis',)


class MeasurementComponentCompoundMultibodyDynamicsAnalysis(_5624.VirtualComponentCompoundMultibodyDynamicsAnalysis):
    """MeasurementComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_MeasurementComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting MeasurementComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'MeasurementComponentCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def virtual_component_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5624.VirtualComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5579
            
            return self._parent._cast(_5579.MountableComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
            
            return self._parent._cast(_5527.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
            
            return self._parent._cast(_5581.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(self) -> 'MeasurementComponentCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2446.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5437.MeasurementComponentMultibodyDynamicsAnalysis]':
        """List[MeasurementComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5437.MeasurementComponentMultibodyDynamicsAnalysis]':
        """List[MeasurementComponentMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MeasurementComponentCompoundMultibodyDynamicsAnalysis._Cast_MeasurementComponentCompoundMultibodyDynamicsAnalysis':
        return self._Cast_MeasurementComponentCompoundMultibodyDynamicsAnalysis(self)
