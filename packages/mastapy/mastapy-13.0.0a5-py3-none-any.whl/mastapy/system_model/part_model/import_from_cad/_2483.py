"""_2483.py

CylindricalRingGearFromCAD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.part_model.import_from_cad import _2481
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RING_GEAR_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'CylindricalRingGearFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalRingGearFromCAD',)


class CylindricalRingGearFromCAD(_2481.CylindricalGearInPlanetarySetFromCAD):
    """CylindricalRingGearFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RING_GEAR_FROM_CAD

    class _Cast_CylindricalRingGearFromCAD:
        """Special nested class for casting CylindricalRingGearFromCAD to subclasses."""

        def __init__(self, parent: 'CylindricalRingGearFromCAD'):
            self._parent = parent

        @property
        def cylindrical_gear_in_planetary_set_from_cad(self):
            return self._parent._cast(_2481.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2480
            
            return self._parent._cast(_2480.CylindricalGearFromCAD)

        @property
        def mountable_component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2486
            
            return self._parent._cast(_2486.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2477
            
            return self._parent._cast(_2477.ComponentFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(self) -> 'CylindricalRingGearFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalRingGearFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD':
        return self._Cast_CylindricalRingGearFromCAD(self)
