﻿"""_952.py

ZerolBevelMeshedGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.bevel import _1179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelMeshedGearDesign',)


class ZerolBevelMeshedGearDesign(_1179.BevelMeshedGearDesign):
    """ZerolBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_MESHED_GEAR_DESIGN

    class _Cast_ZerolBevelMeshedGearDesign:
        """Special nested class for casting ZerolBevelMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'ZerolBevelMeshedGearDesign'):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(self):
            return self._parent._cast(_1179.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1192
            
            return self._parent._cast(_1192.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1155
            
            return self._parent._cast(_1155.ConicalMeshedGearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(self) -> 'ZerolBevelMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign':
        return self._Cast_ZerolBevelMeshedGearDesign(self)
