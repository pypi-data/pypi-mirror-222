"""_1904.py

RingTolerance
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.bearings.tolerances import _1896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'RingTolerance')

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1905


__docformat__ = 'restructuredtext en'
__all__ = ('RingTolerance',)


class RingTolerance(_1896.InterferenceTolerance):
    """RingTolerance

    This is a mastapy class.
    """

    TYPE = _RING_TOLERANCE

    class _Cast_RingTolerance:
        """Special nested class for casting RingTolerance to subclasses."""

        def __init__(self, parent: 'RingTolerance'):
            self._parent = parent

        @property
        def interference_tolerance(self):
            return self._parent._cast(_1896.InterferenceTolerance)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1888
            
            return self._parent._cast(_1888.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1893
            
            return self._parent._cast(_1893.InnerRingTolerance)

        @property
        def outer_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1899
            
            return self._parent._cast(_1899.OuterRingTolerance)

        @property
        def ring_tolerance(self) -> 'RingTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def roundness_specification(self) -> '_1905.RoundnessSpecification':
        """RoundnessSpecification: 'RoundnessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoundnessSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RingTolerance._Cast_RingTolerance':
        return self._Cast_RingTolerance(self)
