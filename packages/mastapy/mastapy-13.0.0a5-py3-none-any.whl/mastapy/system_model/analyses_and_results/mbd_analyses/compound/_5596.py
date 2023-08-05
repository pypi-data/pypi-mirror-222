"""_5596.py

RootAssemblyCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5509
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'RootAssemblyCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5455


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundMultibodyDynamicsAnalysis',)


class RootAssemblyCompoundMultibodyDynamicsAnalysis(_5509.AssemblyCompoundMultibodyDynamicsAnalysis):
    """RootAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting RootAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'RootAssemblyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def assembly_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5509.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5502
            
            return self._parent._cast(_5502.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

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
        def root_assembly_compound_multibody_dynamics_analysis(self) -> 'RootAssemblyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5455.RootAssemblyMultibodyDynamicsAnalysis]':
        """List[RootAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5455.RootAssemblyMultibodyDynamicsAnalysis]':
        """List[RootAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis(self)
