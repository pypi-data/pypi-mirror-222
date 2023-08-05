﻿"""_1574.py

FileHistoryItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FILE_HISTORY_ITEM = python_net_import('SMT.MastaAPI.Utility', 'FileHistoryItem')


__docformat__ = 'restructuredtext en'
__all__ = ('FileHistoryItem',)


class FileHistoryItem(_0.APIBase):
    """FileHistoryItem

    This is a mastapy class.
    """

    TYPE = _FILE_HISTORY_ITEM

    class _Cast_FileHistoryItem:
        """Special nested class for casting FileHistoryItem to subclasses."""

        def __init__(self, parent: 'FileHistoryItem'):
            self._parent = parent

        @property
        def file_history_item(self) -> 'FileHistoryItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FileHistoryItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @property
    def hash_code(self) -> 'str':
        """str: 'HashCode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HashCode

        if temp is None:
            return ''

        return temp

    @property
    def licence_id(self) -> 'str':
        """str: 'LicenceID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LicenceID

        if temp is None:
            return ''

        return temp

    @property
    def save_date(self) -> 'str':
        """str: 'SaveDate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SaveDate

        if temp is None:
            return ''

        return temp

    @property
    def save_date_and_age(self) -> 'str':
        """str: 'SaveDateAndAge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SaveDateAndAge

        if temp is None:
            return ''

        return temp

    @property
    def user_name(self) -> 'str':
        """str: 'UserName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserName

        if temp is None:
            return ''

        return temp

    @property
    def version(self) -> 'str':
        """str: 'Version' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Version

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'FileHistoryItem._Cast_FileHistoryItem':
        return self._Cast_FileHistoryItem(self)
