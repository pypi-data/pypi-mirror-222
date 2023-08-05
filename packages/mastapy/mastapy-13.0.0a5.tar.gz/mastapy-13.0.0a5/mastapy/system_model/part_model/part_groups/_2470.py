﻿"""_2470.py

ConcentricPartGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy.system_model.part_model.part_groups import _2469
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_PART_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.PartGroups', 'ConcentricPartGroup')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2471


__docformat__ = 'restructuredtext en'
__all__ = ('ConcentricPartGroup',)


class ConcentricPartGroup(_2469.ConcentricOrParallelPartGroup):
    """ConcentricPartGroup

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_PART_GROUP

    class _Cast_ConcentricPartGroup:
        """Special nested class for casting ConcentricPartGroup to subclasses."""

        def __init__(self, parent: 'ConcentricPartGroup'):
            self._parent = parent

        @property
        def concentric_or_parallel_part_group(self):
            return self._parent._cast(_2469.ConcentricOrParallelPartGroup)

        @property
        def part_group(self):
            from mastapy.system_model.part_model.part_groups import _2474
            
            return self._parent._cast(_2474.PartGroup)

        @property
        def concentric_part_group(self) -> 'ConcentricPartGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConcentricPartGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_of_cylindrical_gear_face_widths(self) -> 'float':
        """float: 'TotalOfCylindricalGearFaceWidths' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalOfCylindricalGearFaceWidths

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_position(self) -> 'Vector2D':
        """Vector2D: 'RadialPosition' is the original name of this property."""

        temp = self.wrapped.RadialPosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @radial_position.setter
    def radial_position(self, value: 'Vector2D'):
        value = conversion.mp_to_pn_vector2d(value)
        self.wrapped.RadialPosition = value

    @property
    def parallel_groups(self) -> 'List[_2471.ConcentricPartGroupParallelToThis]':
        """List[ConcentricPartGroupParallelToThis]: 'ParallelGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParallelGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConcentricPartGroup._Cast_ConcentricPartGroup':
        return self._Cast_ConcentricPartGroup(self)
