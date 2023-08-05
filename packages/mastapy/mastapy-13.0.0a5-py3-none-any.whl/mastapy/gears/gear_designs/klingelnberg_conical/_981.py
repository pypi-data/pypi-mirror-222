﻿"""_981.py

KlingelnbergConicalMeshedGearDesign
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.gear_designs.conical import _1155
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical', 'KlingelnbergConicalMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergConicalMeshedGearDesign',)


class KlingelnbergConicalMeshedGearDesign(_1155.ConicalMeshedGearDesign):
    """KlingelnbergConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_MESHED_GEAR_DESIGN

    class _Cast_KlingelnbergConicalMeshedGearDesign:
        """Special nested class for casting KlingelnbergConicalMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergConicalMeshedGearDesign'):
            self._parent = parent

        @property
        def conical_meshed_gear_design(self):
            return self._parent._cast(_1155.ConicalMeshedGearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _945
            
            return self._parent._cast(_945.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973
            
            return self._parent._cast(_973.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _977
            
            return self._parent._cast(_977.KlingelnbergCycloPalloidHypoidMeshedGearDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(self) -> 'KlingelnbergConicalMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergConicalMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign':
        return self._Cast_KlingelnbergConicalMeshedGearDesign(self)
