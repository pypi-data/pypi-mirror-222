"""_5825.py

DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_POINT_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_AT_A_FREQUENCY_TO_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic',)


class DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic(_0.APIBase):
    """DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic

    This is a mastapy class.
    """

    TYPE = _DATA_POINT_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_AT_A_FREQUENCY_TO_A_HARMONIC

    class _Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic:
        """Special nested class for casting DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic to subclasses."""

        def __init__(self, parent: 'DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic'):
            self._parent = parent

        @property
        def data_point_for_response_of_a_component_or_surface_at_a_frequency_to_a_harmonic(self) -> 'DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def response(self) -> 'complex':
        """complex: 'Response' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Response

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def cast_to(self) -> 'DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic':
        return self._Cast_DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic(self)
