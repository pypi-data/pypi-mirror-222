﻿"""_2486.py

MountableComponentFromCAD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2477
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'MountableComponentFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentFromCAD',)


class MountableComponentFromCAD(_2477.ComponentFromCAD):
    """MountableComponentFromCAD

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_FROM_CAD

    class _Cast_MountableComponentFromCAD:
        """Special nested class for casting MountableComponentFromCAD to subclasses."""

        def __init__(self, parent: 'MountableComponentFromCAD'):
            self._parent = parent

        @property
        def component_from_cad(self):
            return self._parent._cast(_2477.ComponentFromCAD)

        @property
        def clutch_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2476
            
            return self._parent._cast(_2476.ClutchFromCAD)

        @property
        def concept_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2478
            
            return self._parent._cast(_2478.ConceptBearingFromCAD)

        @property
        def connector_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2479
            
            return self._parent._cast(_2479.ConnectorFromCAD)

        @property
        def cylindrical_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2480
            
            return self._parent._cast(_2480.CylindricalGearFromCAD)

        @property
        def cylindrical_gear_in_planetary_set_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2481
            
            return self._parent._cast(_2481.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_planet_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2482
            
            return self._parent._cast(_2482.CylindricalPlanetGearFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2483
            
            return self._parent._cast(_2483.CylindricalRingGearFromCAD)

        @property
        def cylindrical_sun_gear_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2484
            
            return self._parent._cast(_2484.CylindricalSunGearFromCAD)

        @property
        def pulley_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2488
            
            return self._parent._cast(_2488.PulleyFromCAD)

        @property
        def rigid_connector_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2489
            
            return self._parent._cast(_2489.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2490
            
            return self._parent._cast(_2490.RollingBearingFromCAD)

        @property
        def mountable_component_from_cad(self) -> 'MountableComponentFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MountableComponentFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'MountableComponentFromCAD._Cast_MountableComponentFromCAD':
        return self._Cast_MountableComponentFromCAD(self)
