"""_2587.py

SynchroniserPart
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.couplings import _2566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPart',)


class SynchroniserPart(_2566.CouplingHalf):
    """SynchroniserPart

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART

    class _Cast_SynchroniserPart:
        """Special nested class for casting SynchroniserPart to subclasses."""

        def __init__(self, parent: 'SynchroniserPart'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2566.CouplingHalf)

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
        def synchroniser_half(self):
            from mastapy.system_model.part_model.couplings import _2586
            
            return self._parent._cast(_2586.SynchroniserHalf)

        @property
        def synchroniser_sleeve(self):
            from mastapy.system_model.part_model.couplings import _2588
            
            return self._parent._cast(_2588.SynchroniserSleeve)

        @property
        def synchroniser_part(self) -> 'SynchroniserPart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SynchroniserPart._Cast_SynchroniserPart':
        return self._Cast_SynchroniserPart(self)
