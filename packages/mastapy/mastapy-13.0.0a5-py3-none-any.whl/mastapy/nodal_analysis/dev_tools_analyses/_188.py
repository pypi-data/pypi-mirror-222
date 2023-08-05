﻿"""_188.py

FEModelPart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_PART = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelPart')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelPart',)


class FEModelPart(_0.APIBase):
    """FEModelPart

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_PART

    class _Cast_FEModelPart:
        """Special nested class for casting FEModelPart to subclasses."""

        def __init__(self, parent: 'FEModelPart'):
            self._parent = parent

        @property
        def fe_model_part(self) -> 'FEModelPart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEModelPart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self) -> 'int':
        """int: 'ID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'FEModelPart._Cast_FEModelPart':
        return self._Cast_FEModelPart(self)
