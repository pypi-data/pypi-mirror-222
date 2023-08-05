"""_943.py

DesignConstraintsCollection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_CONSTRAINTS_COLLECTION = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'DesignConstraintsCollection')

if TYPE_CHECKING:
    from mastapy.utility.property import _1825
    from mastapy.gears.gear_designs import _941


__docformat__ = 'restructuredtext en'
__all__ = ('DesignConstraintsCollection',)


class DesignConstraintsCollection(_1818.NamedDatabaseItem):
    """DesignConstraintsCollection

    This is a mastapy class.
    """

    TYPE = _DESIGN_CONSTRAINTS_COLLECTION

    class _Cast_DesignConstraintsCollection:
        """Special nested class for casting DesignConstraintsCollection to subclasses."""

        def __init__(self, parent: 'DesignConstraintsCollection'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def design_constraints_collection(self) -> 'DesignConstraintsCollection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DesignConstraintsCollection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_constraints(self) -> 'List[_1825.DeletableCollectionMember[_941.DesignConstraint]]':
        """List[DeletableCollectionMember[DesignConstraint]]: 'DesignConstraints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DesignConstraintsCollection._Cast_DesignConstraintsCollection':
        return self._Cast_DesignConstraintsCollection(self)
