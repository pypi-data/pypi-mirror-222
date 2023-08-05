﻿"""_2579.py

RollingRingAssembly
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssembly',)


class RollingRingAssembly(_2459.SpecialisedAssembly):
    """RollingRingAssembly

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY

    class _Cast_RollingRingAssembly:
        """Special nested class for casting RollingRingAssembly to subclasses."""

        def __init__(self, parent: 'RollingRingAssembly'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def rolling_ring_assembly(self) -> 'RollingRingAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RollingRingAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property."""

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    def angle(self, value: 'float'):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def rolling_rings(self) -> 'List[_2578.RollingRing]':
        """List[RollingRing]: 'RollingRings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RollingRingAssembly._Cast_RollingRingAssembly':
        return self._Cast_RollingRingAssembly(self)
