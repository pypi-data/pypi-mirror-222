"""_4870.py

CouplingConnectionModalAnalysisAtAStiffness
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4899
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CouplingConnectionModalAnalysisAtAStiffness')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2329


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionModalAnalysisAtAStiffness',)


class CouplingConnectionModalAnalysisAtAStiffness(_4899.InterMountableComponentConnectionModalAnalysisAtAStiffness):
    """CouplingConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CouplingConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CouplingConnectionModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4899.InterMountableComponentConnectionModalAnalysisAtAStiffness)

        @property
        def connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4868
            
            return self._parent._cast(_4868.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4854
            
            return self._parent._cast(_4854.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4859
            
            return self._parent._cast(_4859.ConceptCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4914
            
            return self._parent._cast(_4914.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness)

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4936
            
            return self._parent._cast(_4936.SpringDamperConnectionModalAnalysisAtAStiffness)

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4951
            
            return self._parent._cast(_4951.TorqueConverterConnectionModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(self) -> 'CouplingConnectionModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2329.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionModalAnalysisAtAStiffness._Cast_CouplingConnectionModalAnalysisAtAStiffness':
        return self._Cast_CouplingConnectionModalAnalysisAtAStiffness(self)
