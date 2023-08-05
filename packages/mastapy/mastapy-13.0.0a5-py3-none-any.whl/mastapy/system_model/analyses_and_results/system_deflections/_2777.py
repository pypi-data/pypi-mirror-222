﻿"""_2777.py

RingPinsToDiscConnectionSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RingPinsToDiscConnectionSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2324
    from mastapy.system_model.analyses_and_results.static_loads import _6912
    from mastapy.system_model.analyses_and_results.power_flows import _4105
    from mastapy.system_model.analyses_and_results.system_deflections import _2778


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionSystemDeflection',)


class RingPinsToDiscConnectionSystemDeflection(_2749.InterMountableComponentConnectionSystemDeflection):
    """RingPinsToDiscConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_SYSTEM_DEFLECTION

    class _Cast_RingPinsToDiscConnectionSystemDeflection:
        """Special nested class for casting RingPinsToDiscConnectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnectionSystemDeflection'):
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
        def ring_pins_to_disc_connection_system_deflection(self) -> 'RingPinsToDiscConnectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_contact_stress_across_all_pins(self) -> 'float':
        """float: 'MaximumContactStressAcrossAllPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStressAcrossAllPins

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_deflections(self) -> 'List[float]':
        """List[float]: 'NormalDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def number_of_pins_in_contact(self) -> 'int':
        """int: 'NumberOfPinsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPinsInContact

        if temp is None:
            return 0

        return temp

    @property
    def pin_with_maximum_contact_stress(self) -> 'int':
        """int: 'PinWithMaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinWithMaximumContactStress

        if temp is None:
            return 0

        return temp

    @property
    def strain_energy(self) -> 'float':
        """float: 'StrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2324.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6912.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4105.RingPinsToDiscConnectionPowerFlow':
        """RingPinsToDiscConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pin_to_disc_contacts(self) -> 'List[_2778.RingPinToDiscContactReporting]':
        """List[RingPinToDiscContactReporting]: 'RingPinToDiscContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinToDiscContacts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingPinsToDiscConnectionSystemDeflection._Cast_RingPinsToDiscConnectionSystemDeflection':
        return self._Cast_RingPinsToDiscConnectionSystemDeflection(self)
