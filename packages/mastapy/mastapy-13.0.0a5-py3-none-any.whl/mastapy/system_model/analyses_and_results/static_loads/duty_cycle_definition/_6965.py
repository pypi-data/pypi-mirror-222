﻿"""_6965.py

PointLoadInputOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility_gui import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'PointLoadInputOptions')

if TYPE_CHECKING:
    from mastapy.math_utility import _1482
    from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6956
    from mastapy.system_model.part_model import _2454


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadInputOptions',)


class PointLoadInputOptions(_1835.ColumnInputOptions):
    """PointLoadInputOptions

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_INPUT_OPTIONS

    class _Cast_PointLoadInputOptions:
        """Special nested class for casting PointLoadInputOptions to subclasses."""

        def __init__(self, parent: 'PointLoadInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1835.ColumnInputOptions)

        @property
        def force_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6960
            
            return self._parent._cast(_6960.ForceInputOptions)

        @property
        def moment_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6963
            
            return self._parent._cast(_6963.MomentInputOptions)

        @property
        def point_load_input_options(self) -> 'PointLoadInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoadInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self) -> '_1482.Axis':
        """Axis: 'Axis' is the original name of this property."""

        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.MathUtility.Axis')
        return constructor.new_from_mastapy('mastapy.math_utility._1482', 'Axis')(value) if value is not None else None

    @axis.setter
    def axis(self, value: '_1482.Axis'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.MathUtility.Axis')
        self.wrapped.Axis = value

    @property
    def conversion_to_load_case(self) -> '_6956.AdditionalForcesObtainedFrom':
        """AdditionalForcesObtainedFrom: 'ConversionToLoadCase' is the original name of this property."""

        temp = self.wrapped.ConversionToLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.AdditionalForcesObtainedFrom')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition._6956', 'AdditionalForcesObtainedFrom')(value) if value is not None else None

    @conversion_to_load_case.setter
    def conversion_to_load_case(self, value: '_6956.AdditionalForcesObtainedFrom'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition.AdditionalForcesObtainedFrom')
        self.wrapped.ConversionToLoadCase = value

    @property
    def point_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PointLoad':
        """list_with_selected_item.ListWithSelectedItem_PointLoad: 'PointLoad' is the original name of this property."""

        temp = self.wrapped.PointLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_PointLoad')(temp) if temp is not None else None

    @point_load.setter
    def point_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PointLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PointLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PointLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.PointLoad = value

    @property
    def cast_to(self) -> 'PointLoadInputOptions._Cast_PointLoadInputOptions':
        return self._Cast_PointLoadInputOptions(self)
