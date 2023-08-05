"""_6267.py

ClutchConnectionDynamicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ClutchConnectionDynamicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6800


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionDynamicAnalysis',)


class ClutchConnectionDynamicAnalysis(_6283.CouplingConnectionDynamicAnalysis):
    """ClutchConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_DYNAMIC_ANALYSIS

    class _Cast_ClutchConnectionDynamicAnalysis:
        """Special nested class for casting ClutchConnectionDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ClutchConnectionDynamicAnalysis'):
            self._parent = parent

        @property
        def coupling_connection_dynamic_analysis(self):
            return self._parent._cast(_6283.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312
            
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
        def clutch_connection_dynamic_analysis(self) -> 'ClutchConnectionDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ClutchConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2325.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6800.ClutchConnectionLoadCase':
        """ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ClutchConnectionDynamicAnalysis._Cast_ClutchConnectionDynamicAnalysis':
        return self._Cast_ClutchConnectionDynamicAnalysis(self)
