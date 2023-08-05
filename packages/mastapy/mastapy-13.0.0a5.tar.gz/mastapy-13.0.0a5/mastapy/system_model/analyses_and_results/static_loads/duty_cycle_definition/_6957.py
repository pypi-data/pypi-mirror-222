﻿"""_6957.py

BoostPressureLoadCaseInputOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility_gui import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'BoostPressureLoadCaseInputOptions')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2508


__docformat__ = 'restructuredtext en'
__all__ = ('BoostPressureLoadCaseInputOptions',)


class BoostPressureLoadCaseInputOptions(_1835.ColumnInputOptions):
    """BoostPressureLoadCaseInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS

    class _Cast_BoostPressureLoadCaseInputOptions:
        """Special nested class for casting BoostPressureLoadCaseInputOptions to subclasses."""

        def __init__(self, parent: 'BoostPressureLoadCaseInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1835.ColumnInputOptions)

        @property
        def boost_pressure_load_case_input_options(self) -> 'BoostPressureLoadCaseInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoostPressureLoadCaseInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_set(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGearSet: 'RotorSet' is the original name of this property."""

        temp = self.wrapped.RotorSet

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_CylindricalGearSet')(temp) if temp is not None else None

    @rotor_set.setter
    def rotor_set(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.RotorSet = value

    @property
    def cast_to(self) -> 'BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions':
        return self._Cast_BoostPressureLoadCaseInputOptions(self)
