﻿"""_6966.py

PowerLoadInputOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility_gui import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'PowerLoadInputOptions')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadInputOptions',)


class PowerLoadInputOptions(_1835.ColumnInputOptions):
    """PowerLoadInputOptions

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_INPUT_OPTIONS

    class _Cast_PowerLoadInputOptions:
        """Special nested class for casting PowerLoadInputOptions to subclasses."""

        def __init__(self, parent: 'PowerLoadInputOptions'):
            self._parent = parent

        @property
        def column_input_options(self):
            return self._parent._cast(_1835.ColumnInputOptions)

        @property
        def speed_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6968
            
            return self._parent._cast(_6968.SpeedInputOptions)

        @property
        def torque_input_options(self):
            from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6971
            
            return self._parent._cast(_6971.TorqueInputOptions)

        @property
        def power_load_input_options(self) -> 'PowerLoadInputOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerLoadInputOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'PowerLoad' is the original name of this property."""

        temp = self.wrapped.PowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_PowerLoad')(temp) if temp is not None else None

    @power_load.setter
    def power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.PowerLoad = value

    @property
    def cast_to(self) -> 'PowerLoadInputOptions._Cast_PowerLoadInputOptions':
        return self._Cast_PowerLoadInputOptions(self)
