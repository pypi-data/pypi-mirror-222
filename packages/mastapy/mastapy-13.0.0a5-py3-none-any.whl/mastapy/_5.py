﻿"""_5.py

Versioning
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy._internal.class_property import classproperty
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VERSIONING = python_net_import('SMT.MastaAPI', 'Versioning')


__docformat__ = 'restructuredtext en'
__all__ = ('Versioning',)


class Versioning:
    """Versioning

    This is a mastapy class.
    """

    TYPE = _VERSIONING

    class _Cast_Versioning:
        """Special nested class for casting Versioning to subclasses."""

        def __init__(self, parent: 'Versioning'):
            self._parent = parent

        @property
        def versioning(self) -> 'Versioning':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Versioning.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def api_release_version_string(cls) -> 'str':
        """str: 'APIReleaseVersionString' is the original name of this property."""

        temp = Versioning.TYPE.APIReleaseVersionString

        if temp is None:
            return ''

        return temp

    @classproperty
    def masta_version_string(cls) -> 'str':
        """str: 'MastaVersionString' is the original name of this property."""

        temp = Versioning.TYPE.MastaVersionString

        if temp is None:
            return ''

        return temp

    @classproperty
    def is_backwards_compatible_case(cls) -> 'bool':
        """bool: 'IsBackwardsCompatibleCase' is the original name of this property."""

        temp = Versioning.TYPE.IsBackwardsCompatibleCase

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'Versioning._Cast_Versioning':
        return self._Cast_Versioning(self)
