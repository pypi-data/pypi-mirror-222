﻿"""_2681.py

BeltConnectionSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BeltConnectionSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2251
    from mastapy.system_model.analyses_and_results.static_loads import _6788
    from mastapy.system_model.analyses_and_results.power_flows import _4021


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionSystemDeflection',)


class BeltConnectionSystemDeflection(_2749.InterMountableComponentConnectionSystemDeflection):
    """BeltConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_SYSTEM_DEFLECTION

    class _Cast_BeltConnectionSystemDeflection:
        """Special nested class for casting BeltConnectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'BeltConnectionSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(self):
            return self._parent._cast(_2749.InterMountableComponentConnectionSystemDeflection)

        @property
        def connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2709
            
            return self._parent._cast(_2709.ConnectionSystemDeflection)

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
        def cvt_belt_connection_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2714
            
            return self._parent._cast(_2714.CVTBeltConnectionSystemDeflection)

        @property
        def belt_connection_system_deflection(self) -> 'BeltConnectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extension(self) -> 'float':
        """float: 'Extension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Extension

        if temp is None:
            return 0.0

        return temp

    @property
    def extension_including_pre_tension(self) -> 'float':
        """float: 'ExtensionIncludingPreTension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExtensionIncludingPreTension

        if temp is None:
            return 0.0

        return temp

    @property
    def force_in_loa(self) -> 'float':
        """float: 'ForceInLOA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceInLOA

        if temp is None:
            return 0.0

        return temp

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
    def power_flow_results(self) -> '_4021.BeltConnectionPowerFlow':
        """BeltConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltConnectionSystemDeflection._Cast_BeltConnectionSystemDeflection':
        return self._Cast_BeltConnectionSystemDeflection(self)
