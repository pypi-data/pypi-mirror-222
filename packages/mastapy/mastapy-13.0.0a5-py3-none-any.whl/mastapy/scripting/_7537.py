﻿"""_7537.py

ApiVersioning
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_API_VERSIONING = python_net_import('SMT.MastaAPIUtility.Scripting', 'ApiVersioning')

if TYPE_CHECKING:
    from mastapy.scripting import _7529


__docformat__ = 'restructuredtext en'
__all__ = ('ApiVersioning',)


class ApiVersioning:
    """ApiVersioning

    This is a mastapy class.
    """

    TYPE = _API_VERSIONING

    class _Cast_ApiVersioning:
        """Special nested class for casting ApiVersioning to subclasses."""

        def __init__(self, parent: 'ApiVersioning'):
            self._parent = parent

        @property
        def api_versioning(self) -> 'ApiVersioning':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ApiVersioning.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    def get_available_api_versions(folder: 'str') -> 'Iterable[_7529.ApiVersion]':
        """ 'GetAvailableApiVersions' is the original name of this method.

        Args:
            folder (str)

        Returns:
            Iterable[mastapy.scripting.ApiVersion]
        """

        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(ApiVersioning.TYPE.GetAvailableApiVersions(folder if folder else ''))

    @staticmethod
    def get_available_api_utility_versions(folder: 'str') -> 'Iterable[_7529.ApiVersion]':
        """ 'GetAvailableApiUtilityVersions' is the original name of this method.

        Args:
            folder (str)

        Returns:
            Iterable[mastapy.scripting.ApiVersion]
        """

        folder = str(folder)
        return conversion.pn_to_mp_objects_in_iterable(ApiVersioning.TYPE.GetAvailableApiUtilityVersions(folder if folder else ''))

    @staticmethod
    def get_api_version_for_assembly(api_library_search_folder: 'str', assembly_path: 'str') -> '_7529.ApiVersion':
        """ 'GetApiVersionForAssembly' is the original name of this method.

        Args:
            api_library_search_folder (str)
            assembly_path (str)

        Returns:
            mastapy.scripting.ApiVersion
        """

        api_library_search_folder = str(api_library_search_folder)
        assembly_path = str(assembly_path)
        method_result = ApiVersioning.TYPE.GetApiVersionForAssembly(api_library_search_folder if api_library_search_folder else '', assembly_path if assembly_path else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'ApiVersioning._Cast_ApiVersioning':
        return self._Cast_ApiVersioning(self)
