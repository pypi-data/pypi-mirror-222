﻿"""_309.py

CADFaceGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_FACE_GROUP = python_net_import('SMT.MastaAPI.Geometry.TwoD', 'CADFaceGroup')

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _308


__docformat__ = 'restructuredtext en'
__all__ = ('CADFaceGroup',)


class CADFaceGroup(_0.APIBase):
    """CADFaceGroup

    This is a mastapy class.
    """

    TYPE = _CAD_FACE_GROUP

    class _Cast_CADFaceGroup:
        """Special nested class for casting CADFaceGroup to subclasses."""

        def __init__(self, parent: 'CADFaceGroup'):
            self._parent = parent

        @property
        def cad_face_group(self) -> 'CADFaceGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADFaceGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def add_face(self, moniker: 'str') -> '_308.CADFace':
        """ 'AddFace' is the original name of this method.

        Args:
            moniker (str)

        Returns:
            mastapy.geometry.two_d.CADFace
        """

        moniker = str(moniker)
        method_result = self.wrapped.AddFace(moniker if moniker else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'CADFaceGroup._Cast_CADFaceGroup':
        return self._Cast_CADFaceGroup(self)
