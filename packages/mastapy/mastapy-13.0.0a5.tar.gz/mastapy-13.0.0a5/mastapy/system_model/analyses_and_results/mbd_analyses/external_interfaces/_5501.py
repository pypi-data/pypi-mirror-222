﻿"""_5501.py

DynamicExternalInterfaceOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_EXTERNAL_INTERFACE_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ExternalInterfaces', 'DynamicExternalInterfaceOptions')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5421


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicExternalInterfaceOptions',)


class DynamicExternalInterfaceOptions(_0.APIBase):
    """DynamicExternalInterfaceOptions

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_EXTERNAL_INTERFACE_OPTIONS

    class _Cast_DynamicExternalInterfaceOptions:
        """Special nested class for casting DynamicExternalInterfaceOptions to subclasses."""

        def __init__(self, parent: 'DynamicExternalInterfaceOptions'):
            self._parent = parent

        @property
        def dynamic_external_interface_options(self) -> 'DynamicExternalInterfaceOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicExternalInterfaceOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def generate_load_case(self) -> 'bool':
        """bool: 'GenerateLoadCase' is the original name of this property."""

        temp = self.wrapped.GenerateLoadCase

        if temp is None:
            return False

        return temp

    @generate_load_case.setter
    def generate_load_case(self, value: 'bool'):
        self.wrapped.GenerateLoadCase = bool(value) if value is not None else False

    @property
    def input_signal_filter_level(self) -> '_5421.InputSignalFilterLevel':
        """InputSignalFilterLevel: 'InputSignalFilterLevel' is the original name of this property."""

        temp = self.wrapped.InputSignalFilterLevel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputSignalFilterLevel')
        return constructor.new_from_mastapy('mastapy.system_model.analyses_and_results.mbd_analyses._5421', 'InputSignalFilterLevel')(value) if value is not None else None

    @input_signal_filter_level.setter
    def input_signal_filter_level(self, value: '_5421.InputSignalFilterLevel'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputSignalFilterLevel')
        self.wrapped.InputSignalFilterLevel = value

    @property
    def path_of_saved_file(self) -> 'str':
        """str: 'PathOfSavedFile' is the original name of this property."""

        temp = self.wrapped.PathOfSavedFile

        if temp is None:
            return ''

        return temp

    @path_of_saved_file.setter
    def path_of_saved_file(self, value: 'str'):
        self.wrapped.PathOfSavedFile = str(value) if value is not None else ''

    @property
    def sample_time(self) -> 'float':
        """float: 'SampleTime' is the original name of this property."""

        temp = self.wrapped.SampleTime

        if temp is None:
            return 0.0

        return temp

    @sample_time.setter
    def sample_time(self, value: 'float'):
        self.wrapped.SampleTime = float(value) if value is not None else 0.0

    @property
    def save_results(self) -> 'bool':
        """bool: 'SaveResults' is the original name of this property."""

        temp = self.wrapped.SaveResults

        if temp is None:
            return False

        return temp

    @save_results.setter
    def save_results(self, value: 'bool'):
        self.wrapped.SaveResults = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'DynamicExternalInterfaceOptions._Cast_DynamicExternalInterfaceOptions':
        return self._Cast_DynamicExternalInterfaceOptions(self)
