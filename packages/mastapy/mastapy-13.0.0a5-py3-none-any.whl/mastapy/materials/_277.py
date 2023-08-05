"""_277.py

SafetyFactorGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_GROUP = python_net_import('SMT.MastaAPI.Materials', 'SafetyFactorGroup')

if TYPE_CHECKING:
    from mastapy.materials import _278


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorGroup',)


class SafetyFactorGroup(_0.APIBase):
    """SafetyFactorGroup

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_GROUP

    class _Cast_SafetyFactorGroup:
        """Special nested class for casting SafetyFactorGroup to subclasses."""

        def __init__(self, parent: 'SafetyFactorGroup'):
            self._parent = parent

        @property
        def safety_factor_group(self) -> 'SafetyFactorGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SafetyFactorGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self) -> 'List[_278.SafetyFactorItem]':
        """List[SafetyFactorItem]: 'Items' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Items

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SafetyFactorGroup._Cast_SafetyFactorGroup':
        return self._Cast_SafetyFactorGroup(self)
