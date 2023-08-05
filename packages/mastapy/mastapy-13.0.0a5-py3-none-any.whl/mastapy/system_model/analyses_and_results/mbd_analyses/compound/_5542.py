"""_5542.py

CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CVTBeltConnectionCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5393


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundMultibodyDynamicsAnalysis',)


class CVTBeltConnectionCompoundMultibodyDynamicsAnalysis(_5511.BeltConnectionCompoundMultibodyDynamicsAnalysis):
    """CVTBeltConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def belt_connection_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5511.BeltConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
            
            return self._parent._cast(_5567.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5537
            
            return self._parent._cast(_5537.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(self) -> 'CVTBeltConnectionCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5393.CVTBeltConnectionMultibodyDynamicsAnalysis]':
        """List[CVTBeltConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5393.CVTBeltConnectionMultibodyDynamicsAnalysis]':
        """List[CVTBeltConnectionMultibodyDynamicsAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundMultibodyDynamicsAnalysis._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis':
        return self._Cast_CVTBeltConnectionCompoundMultibodyDynamicsAnalysis(self)
