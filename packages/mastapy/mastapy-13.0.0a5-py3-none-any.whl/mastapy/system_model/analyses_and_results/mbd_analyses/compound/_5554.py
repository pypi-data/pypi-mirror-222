"""_5554.py

ExternalCADModelCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ExternalCADModelCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2435
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5405


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCompoundMultibodyDynamicsAnalysis',)


class ExternalCADModelCompoundMultibodyDynamicsAnalysis(_5527.ComponentCompoundMultibodyDynamicsAnalysis):
    """ExternalCADModelCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ExternalCADModelCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ExternalCADModelCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ExternalCADModelCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(self):
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
        def external_cad_model_compound_multibody_dynamics_analysis(self) -> 'ExternalCADModelCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ExternalCADModelCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2435.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5405.ExternalCADModelMultibodyDynamicsAnalysis]':
        """List[ExternalCADModelMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5405.ExternalCADModelMultibodyDynamicsAnalysis]':
        """List[ExternalCADModelMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ExternalCADModelCompoundMultibodyDynamicsAnalysis._Cast_ExternalCADModelCompoundMultibodyDynamicsAnalysis':
        return self._Cast_ExternalCADModelCompoundMultibodyDynamicsAnalysis(self)
