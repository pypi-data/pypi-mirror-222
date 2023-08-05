﻿"""_1489.py

CoordinateSystem3D
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy._math.matrix_4x4 import Matrix4x4
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_3D = python_net_import('SMT.MastaAPI.MathUtility', 'CoordinateSystem3D')

if TYPE_CHECKING:
    from mastapy.math_utility import _1494


__docformat__ = 'restructuredtext en'
__all__ = ('CoordinateSystem3D',)


class CoordinateSystem3D(_0.APIBase):
    """CoordinateSystem3D

    This is a mastapy class.
    """

    TYPE = _COORDINATE_SYSTEM_3D

    class _Cast_CoordinateSystem3D:
        """Special nested class for casting CoordinateSystem3D to subclasses."""

        def __init__(self, parent: 'CoordinateSystem3D'):
            self._parent = parent

        @property
        def coordinate_system_3d(self) -> 'CoordinateSystem3D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoordinateSystem3D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def origin(self) -> 'Vector3D':
        """Vector3D: 'Origin' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Origin

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def x_axis(self) -> 'Vector3D':
        """Vector3D: 'XAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def y_axis(self) -> 'Vector3D':
        """Vector3D: 'YAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def z_axis(self) -> 'Vector3D':
        """Vector3D: 'ZAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxis

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    def axis(self, degree_of_freedom: '_1494.DegreeOfFreedom') -> 'Vector3D':
        """ 'Axis' is the original name of this method.

        Args:
            degree_of_freedom (mastapy.math_utility.DegreeOfFreedom)

        Returns:
            Vector3D
        """

        degree_of_freedom = conversion.mp_to_pn_enum(degree_of_freedom, 'SMT.MastaAPI.MathUtility.DegreeOfFreedom')
        return conversion.pn_to_mp_vector3d(self.wrapped.Axis(degree_of_freedom))

    def rotated_about_axis(self, axis: 'Vector3D', angle: 'float') -> 'CoordinateSystem3D':
        """ 'RotatedAboutAxis' is the original name of this method.

        Args:
            axis (Vector3D)
            angle (float)

        Returns:
            mastapy.math_utility.CoordinateSystem3D
        """

        axis = conversion.mp_to_pn_vector3d(axis)
        angle = float(angle)
        method_result = self.wrapped.RotatedAboutAxis(axis, angle if angle else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def transform_from_world_to_this(self) -> 'Matrix4x4':
        """ 'TransformFromWorldToThis' is the original name of this method.

        Returns:
            Matrix4x4
        """

        return conversion.pn_to_mp_matrix4x4(self.wrapped.TransformFromWorldToThis())

    def transform_to_world_from_this(self) -> 'Matrix4x4':
        """ 'TransformToWorldFromThis' is the original name of this method.

        Returns:
            Matrix4x4
        """

        return conversion.pn_to_mp_matrix4x4(self.wrapped.TransformToWorldFromThis())

    def transformed_by(self, transform: 'Matrix4x4') -> 'CoordinateSystem3D':
        """ 'TransformedBy' is the original name of this method.

        Args:
            transform (Matrix4x4)

        Returns:
            mastapy.math_utility.CoordinateSystem3D
        """

        transform = conversion.mp_to_pn_matrix4x4(transform)
        method_result = self.wrapped.TransformedBy(transform)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def without_translation(self) -> 'CoordinateSystem3D':
        """ 'WithoutTranslation' is the original name of this method.

        Returns:
            mastapy.math_utility.CoordinateSystem3D
        """

        method_result = self.wrapped.WithoutTranslation()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'CoordinateSystem3D._Cast_CoordinateSystem3D':
        return self._Cast_CoordinateSystem3D(self)
