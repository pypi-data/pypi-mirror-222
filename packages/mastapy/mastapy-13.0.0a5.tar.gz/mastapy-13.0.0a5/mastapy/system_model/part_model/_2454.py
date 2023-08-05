"""_2454.py

PointLoad
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._math.vector_2d import Vector2D
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2462
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoad',)


class PointLoad(_2462.VirtualComponent):
    """PointLoad

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD

    class _Cast_PointLoad:
        """Special nested class for casting PointLoad to subclasses."""

        def __init__(self, parent: 'PointLoad'):
            self._parent = parent

        @property
        def virtual_component(self):
            return self._parent._cast(_2462.VirtualComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2447
            
            return self._parent._cast(_2447.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2427
            
            return self._parent._cast(_2427.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def point_load(self) -> 'PointLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PointLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self) -> 'Vector2D':
        """Vector2D: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)
        return value

    def set_offset(self, radius: 'float', angle: 'float'):
        """ 'SetOffset' is the original name of this method.

        Args:
            radius (float)
            angle (float)
        """

        radius = float(radius)
        angle = float(angle)
        self.wrapped.SetOffset(radius if radius else 0.0, angle if angle else 0.0)

    @property
    def cast_to(self) -> 'PointLoad._Cast_PointLoad':
        return self._Cast_PointLoad(self)
