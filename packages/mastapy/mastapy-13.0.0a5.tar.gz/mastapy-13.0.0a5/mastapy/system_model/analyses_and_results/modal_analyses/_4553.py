﻿"""_4553.py

AbstractShaftToMountableComponentConnectionModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'AbstractShaftToMountableComponentConnectionModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2248
    from mastapy.system_model.analyses_and_results.system_deflections import _2670


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionModalAnalysis',)


class AbstractShaftToMountableComponentConnectionModalAnalysis(_4585.ConnectionModalAnalysis):
    """AbstractShaftToMountableComponentConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS

    class _Cast_AbstractShaftToMountableComponentConnectionModalAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionModalAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionModalAnalysis'):
            self._parent = parent

        @property
        def connection_modal_analysis(self):
            return self._parent._cast(_4585.ConnectionModalAnalysis)

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
        def coaxial_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574
            
            return self._parent._cast(_4574.CoaxialConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595
            
            return self._parent._cast(_4595.CycloidalDiscCentralBearingConnectionModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597
            
            return self._parent._cast(_4597.CycloidalDiscPlanetaryBearingConnectionModalAnalysis)

        @property
        def planetary_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642
            
            return self._parent._cast(_4642.PlanetaryConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657
            
            return self._parent._cast(_4657.ShaftToMountableComponentConnectionModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(self) -> 'AbstractShaftToMountableComponentConnectionModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2248.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2670.AbstractShaftToMountableComponentConnectionSystemDeflection':
        """AbstractShaftToMountableComponentConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis':
        return self._Cast_AbstractShaftToMountableComponentConnectionModalAnalysis(self)
