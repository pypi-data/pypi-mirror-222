"""_5503.py

AbstractShaftCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AbstractShaftCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5351


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundMultibodyDynamicsAnalysis',)


class AbstractShaftCompoundMultibodyDynamicsAnalysis(_5504.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis):
    """AbstractShaftCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5504.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis)

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
        def cycloidal_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
            
            return self._parent._cast(_5547.CycloidalDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
            
            return self._parent._cast(_5597.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(self) -> 'AbstractShaftCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5351.AbstractShaftMultibodyDynamicsAnalysis]':
        """List[AbstractShaftMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5351.AbstractShaftMultibodyDynamicsAnalysis]':
        """List[AbstractShaftMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis':
        return self._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis(self)
