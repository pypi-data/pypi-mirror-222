"""_2419.py

AbstractShaftOrHousing
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model import _2427
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousing',)


class AbstractShaftOrHousing(_2427.Component):
    """AbstractShaftOrHousing

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING

    class _Cast_AbstractShaftOrHousing:
        """Special nested class for casting AbstractShaftOrHousing to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousing'):
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
        def abstract_shaft(self):
            from mastapy.system_model.part_model import _2418
            
            return self._parent._cast(_2418.AbstractShaft)

        @property
        def fe_part(self):
            from mastapy.system_model.part_model import _2436
            
            return self._parent._cast(_2436.FEPart)

        @property
        def shaft(self):
            from mastapy.system_model.part_model.shaft_model import _2465
            
            return self._parent._cast(_2465.Shaft)

        @property
        def cycloidal_disc(self):
            from mastapy.system_model.part_model.cycloidal import _2551
            
            return self._parent._cast(_2551.CycloidalDisc)

        @property
        def abstract_shaft_or_housing(self) -> 'AbstractShaftOrHousing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AbstractShaftOrHousing._Cast_AbstractShaftOrHousing':
        return self._Cast_AbstractShaftOrHousing(self)
