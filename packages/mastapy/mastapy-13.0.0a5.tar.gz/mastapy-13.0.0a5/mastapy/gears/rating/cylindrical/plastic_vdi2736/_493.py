"""_493.py

PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_VDI2736_GEAR_SINGLE_FLANK_RATING_IN_A_METAL_PLASTIC_OR_A_PLASTIC_METAL_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh',)


class PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh(_488.PlasticGearVDI2736AbstractGearSingleFlankRating):
    """PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh

    This is a mastapy class.
    """

    TYPE = _PLASTIC_VDI2736_GEAR_SINGLE_FLANK_RATING_IN_A_METAL_PLASTIC_OR_A_PLASTIC_METAL_MESH

    class _Cast_PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh:
        """Special nested class for casting PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh to subclasses."""

        def __init__(self, parent: 'PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh'):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(self):
            return self._parent._cast(_488.PlasticGearVDI2736AbstractGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _514
            
            return self._parent._cast(_514.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _463
            
            return self._parent._cast(_463.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _362
            
            return self._parent._cast(_362.GearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(self) -> 'PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh':
        return self._Cast_PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh(self)
