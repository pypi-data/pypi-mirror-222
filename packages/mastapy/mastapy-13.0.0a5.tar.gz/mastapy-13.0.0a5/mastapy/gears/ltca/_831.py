﻿"""_831.py

GearBendingStiffnessNode
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.ltca import _845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_BENDING_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearBendingStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('GearBendingStiffnessNode',)


class GearBendingStiffnessNode(_845.GearStiffnessNode):
    """GearBendingStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_BENDING_STIFFNESS_NODE

    class _Cast_GearBendingStiffnessNode:
        """Special nested class for casting GearBendingStiffnessNode to subclasses."""

        def __init__(self, parent: 'GearBendingStiffnessNode'):
            self._parent = parent

        @property
        def gear_stiffness_node(self):
            return self._parent._cast(_845.GearStiffnessNode)

        @property
        def fe_stiffness_node(self):
            from mastapy.nodal_analysis import _67
            
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _849
            
            return self._parent._cast(_849.CylindricalGearBendingStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.conical import _861
            
            return self._parent._cast(_861.ConicalGearBendingStiffnessNode)

        @property
        def gear_bending_stiffness_node(self) -> 'GearBendingStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearBendingStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearBendingStiffnessNode._Cast_GearBendingStiffnessNode':
        return self._Cast_GearBendingStiffnessNode(self)
