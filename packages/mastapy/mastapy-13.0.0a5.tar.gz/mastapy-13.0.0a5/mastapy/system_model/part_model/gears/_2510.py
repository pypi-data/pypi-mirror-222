﻿"""_2510.py

FaceGear
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.part_model.gears import _2512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.gears.gear_designs.face import _986


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGear',)


class FaceGear(_2512.Gear):
    """FaceGear

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR

    class _Cast_FaceGear:
        """Special nested class for casting FaceGear to subclasses."""

        def __init__(self, parent: 'FaceGear'):
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
        def face_gear(self) -> 'FaceGear':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> '_2513.GearOrientations':
        """GearOrientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations')
        return constructor.new_from_mastapy('mastapy.system_model.part_model.gears._2513', 'GearOrientations')(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_2513.GearOrientations'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations')
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self) -> '_986.FaceGearDesign':
        """FaceGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear_design(self) -> '_986.FaceGearDesign':
        """FaceGearDesign: 'FaceGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FaceGear._Cast_FaceGear':
        return self._Cast_FaceGear(self)
