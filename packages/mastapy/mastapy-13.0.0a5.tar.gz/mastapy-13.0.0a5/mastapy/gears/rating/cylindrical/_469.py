﻿"""_469.py

CylindricalRateableMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating import _365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalRateableMesh',)


class CylindricalRateableMesh(_365.RateableMesh):
    """CylindricalRateableMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RATEABLE_MESH

    class _Cast_CylindricalRateableMesh:
        """Special nested class for casting CylindricalRateableMesh to subclasses."""

        def __init__(self, parent: 'CylindricalRateableMesh'):
            self._parent = parent

        @property
        def rateable_mesh(self):
            return self._parent._cast(_365.RateableMesh)

        @property
        def plastic_gear_vdi2736_abstract_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _490
            
            return self._parent._cast(_490.PlasticGearVDI2736AbstractRateableMesh)

        @property
        def vdi2736_metal_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495
            
            return self._parent._cast(_495.VDI2736MetalPlasticRateableMesh)

        @property
        def vdi2736_plastic_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _496
            
            return self._parent._cast(_496.VDI2736PlasticMetalRateableMesh)

        @property
        def vdi2736_plastic_plastic_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497
            
            return self._parent._cast(_497.VDI2736PlasticPlasticRateableMesh)

        @property
        def iso6336_metal_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _519
            
            return self._parent._cast(_519.ISO6336MetalRateableMesh)

        @property
        def iso6336_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _520
            
            return self._parent._cast(_520.ISO6336RateableMesh)

        @property
        def agma2101_rateable_mesh(self):
            from mastapy.gears.rating.cylindrical.agma import _533
            
            return self._parent._cast(_533.AGMA2101RateableMesh)

        @property
        def cylindrical_rateable_mesh(self) -> 'CylindricalRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalRateableMesh._Cast_CylindricalRateableMesh':
        return self._Cast_CylindricalRateableMesh(self)
