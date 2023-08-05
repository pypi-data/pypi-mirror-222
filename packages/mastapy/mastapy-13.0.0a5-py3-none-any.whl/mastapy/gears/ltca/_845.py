"""_845.py

GearStiffnessNode
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis import _67
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('GearStiffnessNode',)


class GearStiffnessNode(_67.FEStiffnessNode):
    """GearStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS_NODE

    class _Cast_GearStiffnessNode:
        """Special nested class for casting GearStiffnessNode to subclasses."""

        def __init__(self, parent: 'GearStiffnessNode'):
            self._parent = parent

        @property
        def fe_stiffness_node(self):
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def gear_bending_stiffness_node(self):
            from mastapy.gears.ltca import _831
            
            return self._parent._cast(_831.GearBendingStiffnessNode)

        @property
        def gear_contact_stiffness_node(self):
            from mastapy.gears.ltca import _833
            
            return self._parent._cast(_833.GearContactStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _849
            
            return self._parent._cast(_849.CylindricalGearBendingStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.cylindrical import _851
            
            return self._parent._cast(_851.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(self):
            from mastapy.gears.ltca.conical import _861
            
            return self._parent._cast(_861.ConicalGearBendingStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(self):
            from mastapy.gears.ltca.conical import _863
            
            return self._parent._cast(_863.ConicalGearContactStiffnessNode)

        @property
        def gear_stiffness_node(self) -> 'GearStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearStiffnessNode._Cast_GearStiffnessNode':
        return self._Cast_GearStiffnessNode(self)
