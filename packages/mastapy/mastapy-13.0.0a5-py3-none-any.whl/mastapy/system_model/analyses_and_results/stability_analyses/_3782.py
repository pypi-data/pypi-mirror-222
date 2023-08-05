"""_3782.py

CouplingConnectionStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CouplingConnectionStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2329


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionStabilityAnalysis',)


class CouplingConnectionStabilityAnalysis(_3811.InterMountableComponentConnectionStabilityAnalysis):
    """CouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STABILITY_ANALYSIS

    class _Cast_CouplingConnectionStabilityAnalysis:
        """Special nested class for casting CouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionStabilityAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(self):
            return self._parent._cast(_3811.InterMountableComponentConnectionStabilityAnalysis)

        @property
        def connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3780
            
            return self._parent._cast(_3780.ConnectionStabilityAnalysis)

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
        def clutch_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3766
            
            return self._parent._cast(_3766.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3771
            
            return self._parent._cast(_3771.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3826
            
            return self._parent._cast(_3826.PartToPartShearCouplingConnectionStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3848
            
            return self._parent._cast(_3848.SpringDamperConnectionStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3865
            
            return self._parent._cast(_3865.TorqueConverterConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(self) -> 'CouplingConnectionStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionStabilityAnalysis.TYPE'):
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
    def cast_to(self) -> 'CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis':
        return self._Cast_CouplingConnectionStabilityAnalysis(self)
