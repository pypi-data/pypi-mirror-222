"""_6283.py

CouplingConnectionDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CouplingConnectionDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2329


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionDynamicAnalysis',)


class CouplingConnectionDynamicAnalysis(_6312.InterMountableComponentConnectionDynamicAnalysis):
    """CouplingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_DYNAMIC_ANALYSIS

    class _Cast_CouplingConnectionDynamicAnalysis:
        """Special nested class for casting CouplingConnectionDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'CouplingConnectionDynamicAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(self):
            return self._parent._cast(_6312.InterMountableComponentConnectionDynamicAnalysis)

        @property
        def connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281
            
            return self._parent._cast(_6281.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7506
            
            return self._parent._cast(_7506.ConnectionFEAnalysis)

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
        def clutch_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6267
            
            return self._parent._cast(_6267.ClutchConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6272
            
            return self._parent._cast(_6272.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327
            
            return self._parent._cast(_6327.PartToPartShearCouplingConnectionDynamicAnalysis)

        @property
        def spring_damper_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349
            
            return self._parent._cast(_6349.SpringDamperConnectionDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
            
            return self._parent._cast(_6364.TorqueConverterConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(self) -> 'CouplingConnectionDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionDynamicAnalysis.TYPE'):
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
    def cast_to(self) -> 'CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis':
        return self._Cast_CouplingConnectionDynamicAnalysis(self)
