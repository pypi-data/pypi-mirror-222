"""_2359.py

ElementPropertiesWithSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'ElementPropertiesWithSelection')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _207


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesWithSelection',)


T = TypeVar('T', bound='_207.ElementPropertiesBase')


class ElementPropertiesWithSelection(_0.APIBase, Generic[T]):
    """ElementPropertiesWithSelection

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ELEMENT_PROPERTIES_WITH_SELECTION

    class _Cast_ElementPropertiesWithSelection:
        """Special nested class for casting ElementPropertiesWithSelection to subclasses."""

        def __init__(self, parent: 'ElementPropertiesWithSelection'):
            self._parent = parent

        @property
        def element_properties_with_selection(self) -> 'ElementPropertiesWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_properties(self) -> 'T':
        """T: 'ElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def select_nodes(self):
        """ 'SelectNodes' is the original name of this method."""

        self.wrapped.SelectNodes()

    @property
    def cast_to(self) -> 'ElementPropertiesWithSelection._Cast_ElementPropertiesWithSelection':
        return self._Cast_ElementPropertiesWithSelection(self)
