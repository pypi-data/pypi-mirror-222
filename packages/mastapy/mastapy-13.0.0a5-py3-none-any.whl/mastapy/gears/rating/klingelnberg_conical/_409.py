"""_409.py

KlingelnbergCycloPalloidConicalGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating.conical import _536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical', 'KlingelnbergCycloPalloidConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshRating',)


class KlingelnbergCycloPalloidConicalGearMeshRating(_536.ConicalGearMeshRating):
    """KlingelnbergCycloPalloidConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshRating'):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(self):
            return self._parent._cast(_536.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _358
            
            return self._parent._cast(_358.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
            
            return self._parent._cast(_403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _406
            
            return self._parent._cast(_406.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self) -> 'KlingelnbergCycloPalloidConicalGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshRating(self)
