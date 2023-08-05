"""_1826.py

DutyCyclePropertySummary
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY = python_net_import('SMT.MastaAPI.Utility.Property', 'DutyCyclePropertySummary')

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1596


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCyclePropertySummary',)


TMeasurement = TypeVar('TMeasurement', bound='_1596.MeasurementBase')
T = TypeVar('T')


class DutyCyclePropertySummary(_0.APIBase, Generic[TMeasurement, T]):
    """DutyCyclePropertySummary

    This is a mastapy class.

    Generic Types:
        TMeasurement
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY

    class _Cast_DutyCyclePropertySummary:
        """Special nested class for casting DutyCyclePropertySummary to subclasses."""

        def __init__(self, parent: 'DutyCyclePropertySummary'):
            self._parent = parent

        @property
        def duty_cycle_property_summary_force(self):
            from mastapy.utility.property import _1827
            
            return self._parent._cast(_1827.DutyCyclePropertySummaryForce)

        @property
        def duty_cycle_property_summary_percentage(self):
            from mastapy.utility.property import _1828
            
            return self._parent._cast(_1828.DutyCyclePropertySummaryPercentage)

        @property
        def duty_cycle_property_summary_small_angle(self):
            from mastapy.utility.property import _1829
            
            return self._parent._cast(_1829.DutyCyclePropertySummarySmallAngle)

        @property
        def duty_cycle_property_summary_stress(self):
            from mastapy.utility.property import _1830
            
            return self._parent._cast(_1830.DutyCyclePropertySummaryStress)

        @property
        def duty_cycle_property_summary(self) -> 'DutyCyclePropertySummary':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCyclePropertySummary.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_value_load_case(self) -> 'T':
        """T: 'MaximumAbsoluteValueLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAbsoluteValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_value_load_case(self) -> 'T':
        """T: 'MaximumValueLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_value_load_case(self) -> 'T':
        """T: 'MinimumValueLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumValueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DutyCyclePropertySummary._Cast_DutyCyclePropertySummary':
        return self._Cast_DutyCyclePropertySummary(self)
