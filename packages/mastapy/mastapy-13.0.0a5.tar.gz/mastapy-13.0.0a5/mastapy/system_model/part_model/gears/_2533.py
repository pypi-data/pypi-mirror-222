﻿"""_2533.py

WormGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _954


__docformat__ = 'restructuredtext en'
__all__ = ('WormGear',)


class WormGear(_2512.Gear):
    """WormGear

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR

    class _Cast_WormGear:
        """Special nested class for casting WormGear to subclasses."""

        def __init__(self, parent: 'WormGear'):
            self._parent = parent

        @property
        def gear(self):
            return self._parent._cast(_2512.Gear)

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
        def worm_gear(self) -> 'WormGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_design(self) -> '_954.WormGearDesign':
        """WormGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_design(self) -> '_954.WormGearDesign':
        """WormGearDesign: 'WormGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGear._Cast_WormGear':
        return self._Cast_WormGear(self)
