﻿"""_2425.py

Bolt
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2427
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2426
    from mastapy.bolts import _1472


__docformat__ = 'restructuredtext en'
__all__ = ('Bolt',)


class Bolt(_2427.Component):
    """Bolt

    This is a mastapy class.
    """

    TYPE = _BOLT

    class _Cast_Bolt:
        """Special nested class for casting Bolt to subclasses."""

        def __init__(self, parent: 'Bolt'):
            self._parent = parent

        @property
        def component(self):
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
        def bolt(self) -> 'Bolt':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Bolt.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bolted_joint(self) -> '_2426.BoltedJoint':
        """BoltedJoint: 'BoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loaded_bolt(self) -> '_1472.LoadedBolt':
        """LoadedBolt: 'LoadedBolt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBolt

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Bolt._Cast_Bolt':
        return self._Cast_Bolt(self)
