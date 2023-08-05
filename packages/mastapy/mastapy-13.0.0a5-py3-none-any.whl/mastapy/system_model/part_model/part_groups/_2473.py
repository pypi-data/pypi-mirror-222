﻿"""_2473.py

ParallelPartGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.part_groups import _2469
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARALLEL_PART_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.PartGroups', 'ParallelPartGroup')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2470, _2472


__docformat__ = 'restructuredtext en'
__all__ = ('ParallelPartGroup',)


class ParallelPartGroup(_2469.ConcentricOrParallelPartGroup):
    """ParallelPartGroup

    This is a mastapy class.
    """

    TYPE = _PARALLEL_PART_GROUP

    class _Cast_ParallelPartGroup:
        """Special nested class for casting ParallelPartGroup to subclasses."""

        def __init__(self, parent: 'ParallelPartGroup'):
            self._parent = parent

        @property
        def concentric_or_parallel_part_group(self):
            return self._parent._cast(_2469.ConcentricOrParallelPartGroup)

        @property
        def part_group(self):
            from mastapy.system_model.part_model.part_groups import _2474
            
            return self._parent._cast(_2474.PartGroup)

        @property
        def parallel_part_group(self) -> 'ParallelPartGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParallelPartGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_dx_axis_direction(self) -> 'Vector3D':
        """Vector3D: 'TwoDXAxisDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDXAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def two_dy_axis_direction(self) -> 'Vector3D':
        """Vector3D: 'TwoDYAxisDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDYAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def two_dz_axis_direction(self) -> 'Vector3D':
        """Vector3D: 'TwoDZAxisDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDZAxisDirection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def concentric_part_groups(self) -> 'List[_2470.ConcentricPartGroup]':
        """List[ConcentricPartGroup]: 'ConcentricPartGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConcentricPartGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def design_measurements(self) -> 'List[_2472.DesignMeasurements]':
        """List[DesignMeasurements]: 'DesignMeasurements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignMeasurements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ParallelPartGroup._Cast_ParallelPartGroup':
        return self._Cast_ParallelPartGroup(self)
