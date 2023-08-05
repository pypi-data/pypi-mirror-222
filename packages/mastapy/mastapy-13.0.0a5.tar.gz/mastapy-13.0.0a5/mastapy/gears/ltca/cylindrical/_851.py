"""_851.py

CylindricalGearContactStiffnessNode
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.ltca import _833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CONTACT_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearContactStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearContactStiffnessNode',)


class CylindricalGearContactStiffnessNode(_833.GearContactStiffnessNode):
    """CylindricalGearContactStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CONTACT_STIFFNESS_NODE

    class _Cast_CylindricalGearContactStiffnessNode:
        """Special nested class for casting CylindricalGearContactStiffnessNode to subclasses."""

        def __init__(self, parent: 'CylindricalGearContactStiffnessNode'):
            self._parent = parent

        @property
        def gear_contact_stiffness_node(self):
            return self._parent._cast(_833.GearContactStiffnessNode)

        @property
        def gear_stiffness_node(self):
            from mastapy.gears.ltca import _845
            
            return self._parent._cast(_845.GearStiffnessNode)

        @property
        def fe_stiffness_node(self):
            from mastapy.nodal_analysis import _67
            
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(self) -> 'CylindricalGearContactStiffnessNode':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearContactStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode':
        return self._Cast_CylindricalGearContactStiffnessNode(self)
