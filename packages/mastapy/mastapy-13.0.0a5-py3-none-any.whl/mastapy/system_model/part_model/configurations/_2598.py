"""_2598.py

BearingDetailSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.part_model.configurations import _2600
from mastapy.system_model.part_model import _2422
from mastapy.bearings.bearing_designs import _2117
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailSelection')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1947
    from mastapy.system_model.part_model import _2424


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailSelection',)


class BearingDetailSelection(_2600.PartDetailSelection['_2422.Bearing', '_2117.BearingDesign']):
    """BearingDetailSelection

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_SELECTION

    class _Cast_BearingDetailSelection:
        """Special nested class for casting BearingDetailSelection to subclasses."""

        def __init__(self, parent: 'BearingDetailSelection'):
            self._parent = parent

        @property
        def part_detail_selection(self):
            return self._parent._cast(_2600.PartDetailSelection)

        @property
        def bearing_detail_selection(self) -> 'BearingDetailSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDetailSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_offset(self) -> 'Optional[float]':
        """Optional[float]: 'InnerOffset' is the original name of this property."""

        temp = self.wrapped.InnerOffset

        if temp is None:
            return None

        return temp

    @inner_offset.setter
    def inner_offset(self, value: 'Optional[float]'):
        self.wrapped.InnerOffset = value

    @property
    def orientation(self) -> '_1947.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.BearingResults.Orientations')
        return constructor.new_from_mastapy('mastapy.bearings.bearing_results._1947', 'Orientations')(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1947.Orientations'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.BearingResults.Orientations')
        self.wrapped.Orientation = value

    @property
    def outer_offset(self) -> 'Optional[float]':
        """Optional[float]: 'OuterOffset' is the original name of this property."""

        temp = self.wrapped.OuterOffset

        if temp is None:
            return None

        return temp

    @outer_offset.setter
    def outer_offset(self, value: 'Optional[float]'):
        self.wrapped.OuterOffset = value

    @property
    def mounting(self) -> 'List[_2424.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BearingDetailSelection._Cast_BearingDetailSelection':
        return self._Cast_BearingDetailSelection(self)
