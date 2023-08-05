﻿"""_2763.py

MeshSeparationsAtFaceWidth
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_SEPARATIONS_AT_FACE_WIDTH = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'MeshSeparationsAtFaceWidth')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshSeparationsAtFaceWidth',)


class MeshSeparationsAtFaceWidth(_0.APIBase):
    """MeshSeparationsAtFaceWidth

    This is a mastapy class.
    """

    TYPE = _MESH_SEPARATIONS_AT_FACE_WIDTH

    class _Cast_MeshSeparationsAtFaceWidth:
        """Special nested class for casting MeshSeparationsAtFaceWidth to subclasses."""

        def __init__(self, parent: 'MeshSeparationsAtFaceWidth'):
            self._parent = parent

        @property
        def mesh_separations_at_face_width(self) -> 'MeshSeparationsAtFaceWidth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshSeparationsAtFaceWidth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_location(self) -> 'float':
        """float: 'FaceWidthLocation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthLocation

        if temp is None:
            return 0.0

        return temp

    @property
    def left_flank_separation(self) -> 'float':
        """float: 'LeftFlankSeparation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankSeparation

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def right_flank_separation(self) -> 'float':
        """float: 'RightFlankSeparation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankSeparation

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'MeshSeparationsAtFaceWidth._Cast_MeshSeparationsAtFaceWidth':
        return self._Cast_MeshSeparationsAtFaceWidth(self)
