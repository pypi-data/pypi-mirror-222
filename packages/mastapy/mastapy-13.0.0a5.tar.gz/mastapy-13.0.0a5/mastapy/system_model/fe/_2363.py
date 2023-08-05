﻿"""_2363.py

FEPartWithBatchOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_WITH_BATCH_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FEPartWithBatchOptions')

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2372


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartWithBatchOptions',)


class FEPartWithBatchOptions(_0.APIBase):
    """FEPartWithBatchOptions

    This is a mastapy class.
    """

    TYPE = _FE_PART_WITH_BATCH_OPTIONS

    class _Cast_FEPartWithBatchOptions:
        """Special nested class for casting FEPartWithBatchOptions to subclasses."""

        def __init__(self, parent: 'FEPartWithBatchOptions'):
            self._parent = parent

        @property
        def fe_part_with_batch_options(self) -> 'FEPartWithBatchOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FEPartWithBatchOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_selected(self) -> 'Optional[bool]':
        """Optional[bool]: 'AllSelected' is the original name of this property."""

        temp = self.wrapped.AllSelected

        if temp is None:
            return None

        return temp

    @all_selected.setter
    def all_selected(self, value: 'Optional[bool]'):
        self.wrapped.AllSelected = value

    @property
    def fe_part(self) -> 'str':
        """str: 'FEPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEPart

        if temp is None:
            return ''

        return temp

    @property
    def f_es(self) -> 'List[_2372.FESubstructureWithBatchOptions]':
        """List[FESubstructureWithBatchOptions]: 'FEs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def f_es_with_external_files(self) -> 'List[_2372.FESubstructureWithBatchOptions]':
        """List[FESubstructureWithBatchOptions]: 'FEsWithExternalFiles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEsWithExternalFiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FEPartWithBatchOptions._Cast_FEPartWithBatchOptions':
        return self._Cast_FEPartWithBatchOptions(self)
