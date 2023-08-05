"""_5504.py

AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5352


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis',)


class AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(_5527.ComponentCompoundMultibodyDynamicsAnalysis):
    """AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis'):
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
        def abstract_shaft_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5503
            
            return self._parent._cast(_5503.AbstractShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5547
            
            return self._parent._cast(_5547.CycloidalDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def fe_part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5558
            
            return self._parent._cast(_5558.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
            
            return self._parent._cast(_5597.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(self) -> 'AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_5352.AbstractShaftOrHousingMultibodyDynamicsAnalysis]':
        """List[AbstractShaftOrHousingMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5352.AbstractShaftOrHousingMultibodyDynamicsAnalysis]':
        """List[AbstractShaftOrHousingMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis':
        return self._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(self)
