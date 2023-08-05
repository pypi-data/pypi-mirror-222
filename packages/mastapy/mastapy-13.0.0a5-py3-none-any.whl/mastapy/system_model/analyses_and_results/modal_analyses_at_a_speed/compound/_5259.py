"""_5259.py

CouplingConnectionCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'CouplingConnectionCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5129


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundModalAnalysisAtASpeed',)


class CouplingConnectionCompoundModalAnalysisAtASpeed(_5286.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed):
    """CouplingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_CouplingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5286.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5256
            
            return self._parent._cast(_5256.ConnectionCompoundModalAnalysisAtASpeed)

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
        def clutch_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5243
            
            return self._parent._cast(_5243.ClutchConnectionCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5248
            
            return self._parent._cast(_5248.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5302
            
            return self._parent._cast(_5302.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5324
            
            return self._parent._cast(_5324.SpringDamperConnectionCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5339
            
            return self._parent._cast(_5339.TorqueConverterConnectionCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(self) -> 'CouplingConnectionCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5129.CouplingConnectionModalAnalysisAtASpeed]':
        """List[CouplingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5129.CouplingConnectionModalAnalysisAtASpeed]':
        """List[CouplingConnectionModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed':
        return self._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed(self)
