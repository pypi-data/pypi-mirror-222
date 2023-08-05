"""_2593.py

ActiveFESubstructureSelection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.configurations import _2600
from mastapy.system_model.part_model import _2436
from mastapy.system_model.fe import _2366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveFESubstructureSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveFESubstructureSelection',)


class ActiveFESubstructureSelection(_2600.PartDetailSelection['_2436.FEPart', '_2366.FESubstructure']):
    """ActiveFESubstructureSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION

    class _Cast_ActiveFESubstructureSelection:
        """Special nested class for casting ActiveFESubstructureSelection to subclasses."""

        def __init__(self, parent: 'ActiveFESubstructureSelection'):
            self._parent = parent

        @property
        def part_detail_selection(self):
            return self._parent._cast(_2600.PartDetailSelection)

        @property
        def active_fe_substructure_selection(self) -> 'ActiveFESubstructureSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveFESubstructureSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ActiveFESubstructureSelection._Cast_ActiveFESubstructureSelection':
        return self._Cast_ActiveFESubstructureSelection(self)
