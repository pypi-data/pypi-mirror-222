"""_3754.py

BeltConnectionStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'BeltConnectionStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2251
    from mastapy.system_model.analyses_and_results.static_loads import _6788


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionStabilityAnalysis',)


class BeltConnectionStabilityAnalysis(_3811.InterMountableComponentConnectionStabilityAnalysis):
    """BeltConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_STABILITY_ANALYSIS

    class _Cast_BeltConnectionStabilityAnalysis:
        """Special nested class for casting BeltConnectionStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'BeltConnectionStabilityAnalysis'):
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
        def cvt_belt_connection_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3786
            
            return self._parent._cast(_3786.CVTBeltConnectionStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(self) -> 'BeltConnectionStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2251.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6788.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltConnectionStabilityAnalysis._Cast_BeltConnectionStabilityAnalysis':
        return self._Cast_BeltConnectionStabilityAnalysis(self)
