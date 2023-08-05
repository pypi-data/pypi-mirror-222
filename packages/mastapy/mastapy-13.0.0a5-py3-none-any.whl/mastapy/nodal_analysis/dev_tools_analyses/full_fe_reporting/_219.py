﻿"""_219.py

RigidElementNodeDegreesOfFreedom
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_ELEMENT_NODE_DEGREES_OF_FREEDOM = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'RigidElementNodeDegreesOfFreedom')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _204


__docformat__ = 'restructuredtext en'
__all__ = ('RigidElementNodeDegreesOfFreedom',)


class RigidElementNodeDegreesOfFreedom(_0.APIBase):
    """RigidElementNodeDegreesOfFreedom

    This is a mastapy class.
    """

    TYPE = _RIGID_ELEMENT_NODE_DEGREES_OF_FREEDOM

    class _Cast_RigidElementNodeDegreesOfFreedom:
        """Special nested class for casting RigidElementNodeDegreesOfFreedom to subclasses."""

        def __init__(self, parent: 'RigidElementNodeDegreesOfFreedom'):
            self._parent = parent

        @property
        def rigid_element_node_degrees_of_freedom(self) -> 'RigidElementNodeDegreesOfFreedom':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidElementNodeDegreesOfFreedom.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def index(self) -> 'int':
        """int: 'Index' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Index

        if temp is None:
            return 0

        return temp

    @property
    def type_(self) -> '_204.DegreeOfFreedomType':
        """DegreeOfFreedomType: 'Type' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Type

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting.DegreeOfFreedomType')
        return constructor.new_from_mastapy('mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting._204', 'DegreeOfFreedomType')(value) if value is not None else None

    @property
    def x(self) -> 'bool':
        """bool: 'X' is the original name of this property."""

        temp = self.wrapped.X

        if temp is None:
            return False

        return temp

    @x.setter
    def x(self, value: 'bool'):
        self.wrapped.X = bool(value) if value is not None else False

    @property
    def y(self) -> 'bool':
        """bool: 'Y' is the original name of this property."""

        temp = self.wrapped.Y

        if temp is None:
            return False

        return temp

    @y.setter
    def y(self, value: 'bool'):
        self.wrapped.Y = bool(value) if value is not None else False

    @property
    def z(self) -> 'bool':
        """bool: 'Z' is the original name of this property."""

        temp = self.wrapped.Z

        if temp is None:
            return False

        return temp

    @z.setter
    def z(self, value: 'bool'):
        self.wrapped.Z = bool(value) if value is not None else False

    @property
    def theta_x(self) -> 'bool':
        """bool: 'ThetaX' is the original name of this property."""

        temp = self.wrapped.ThetaX

        if temp is None:
            return False

        return temp

    @theta_x.setter
    def theta_x(self, value: 'bool'):
        self.wrapped.ThetaX = bool(value) if value is not None else False

    @property
    def theta_y(self) -> 'bool':
        """bool: 'ThetaY' is the original name of this property."""

        temp = self.wrapped.ThetaY

        if temp is None:
            return False

        return temp

    @theta_y.setter
    def theta_y(self, value: 'bool'):
        self.wrapped.ThetaY = bool(value) if value is not None else False

    @property
    def theta_z(self) -> 'bool':
        """bool: 'ThetaZ' is the original name of this property."""

        temp = self.wrapped.ThetaZ

        if temp is None:
            return False

        return temp

    @theta_z.setter
    def theta_z(self, value: 'bool'):
        self.wrapped.ThetaZ = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'RigidElementNodeDegreesOfFreedom._Cast_RigidElementNodeDegreesOfFreedom':
        return self._Cast_RigidElementNodeDegreesOfFreedom(self)
