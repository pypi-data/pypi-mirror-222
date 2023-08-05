﻿"""_96.py

MomentInputComponent
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.varying_input_components import _93
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_INPUT_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.VaryingInputComponents', 'MomentInputComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentInputComponent',)


class MomentInputComponent(_93.AbstractVaryingInputComponent):
    """MomentInputComponent

    This is a mastapy class.
    """

    TYPE = _MOMENT_INPUT_COMPONENT

    class _Cast_MomentInputComponent:
        """Special nested class for casting MomentInputComponent to subclasses."""

        def __init__(self, parent: 'MomentInputComponent'):
            self._parent = parent

        @property
        def abstract_varying_input_component(self):
            return self._parent._cast(_93.AbstractVaryingInputComponent)

        @property
        def moment_input_component(self) -> 'MomentInputComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MomentInputComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def moment(self) -> 'float':
        """float: 'Moment' is the original name of this property."""

        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @moment.setter
    def moment(self, value: 'float'):
        self.wrapped.Moment = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'MomentInputComponent._Cast_MomentInputComponent':
        return self._Cast_MomentInputComponent(self)
