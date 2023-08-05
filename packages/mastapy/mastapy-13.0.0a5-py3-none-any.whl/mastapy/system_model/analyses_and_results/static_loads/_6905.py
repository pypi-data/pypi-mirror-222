"""_6905.py

PointLoadHarmonicLoadData
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines.harmonic_load_data import _1373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PointLoadHarmonicLoadData')

if TYPE_CHECKING:
    from mastapy.math_utility import _1494, _1503


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadHarmonicLoadData',)


class PointLoadHarmonicLoadData(_1373.SpeedDependentHarmonicLoadData):
    """PointLoadHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_HARMONIC_LOAD_DATA

    class _Cast_PointLoadHarmonicLoadData:
        """Special nested class for casting PointLoadHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'PointLoadHarmonicLoadData'):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(self):
            return self._parent._cast(_1373.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1370
            
            return self._parent._cast(_1370.HarmonicLoadDataBase)

        @property
        def point_load_harmonic_load_data(self) -> 'PointLoadHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom(self) -> '_1494.DegreeOfFreedom':
        """DegreeOfFreedom: 'DegreeOfFreedom' is the original name of this property."""

        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.MathUtility.DegreeOfFreedom')
        return constructor.new_from_mastapy('mastapy.math_utility._1494', 'DegreeOfFreedom')(value) if value is not None else None

    @degree_of_freedom.setter
    def degree_of_freedom(self, value: '_1494.DegreeOfFreedom'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.MathUtility.DegreeOfFreedom')
        self.wrapped.DegreeOfFreedom = value

    @property
    def reference_shaft(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ReferenceShaft' is the original name of this property."""

        temp = self.wrapped.ReferenceShaft

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @reference_shaft.setter
    def reference_shaft(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ReferenceShaft = value

    @property
    def excitations(self) -> 'List[_1503.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData':
        return self._Cast_PointLoadHarmonicLoadData(self)
