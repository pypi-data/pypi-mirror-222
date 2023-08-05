﻿"""_318.py

ConicalGearToothSurface
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_TOOTH_SURFACE = python_net_import('SMT.MastaAPI.Gears', 'ConicalGearToothSurface')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearToothSurface',)


class ConicalGearToothSurface(_0.APIBase):
    """ConicalGearToothSurface

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_TOOTH_SURFACE

    class _Cast_ConicalGearToothSurface:
        """Special nested class for casting ConicalGearToothSurface to subclasses."""

        def __init__(self, parent: 'ConicalGearToothSurface'):
            self._parent = parent

        @property
        def gear_nurbs_surface(self):
            from mastapy.gears import _325
            
            return self._parent._cast(_325.GearNURBSSurface)

        @property
        def conical_meshed_wheel_flank_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _777
            
            return self._parent._cast(_777.ConicalMeshedWheelFlankManufacturingConfig)

        @property
        def pinion_bevel_generating_modified_roll_machine_settings(self):
            from mastapy.gears.manufacturing.bevel import _798
            
            return self._parent._cast(_798.PinionBevelGeneratingModifiedRollMachineSettings)

        @property
        def pinion_bevel_generating_tilt_machine_settings(self):
            from mastapy.gears.manufacturing.bevel import _799
            
            return self._parent._cast(_799.PinionBevelGeneratingTiltMachineSettings)

        @property
        def pinion_conical_machine_settings_specified(self):
            from mastapy.gears.manufacturing.bevel import _801
            
            return self._parent._cast(_801.PinionConicalMachineSettingsSpecified)

        @property
        def pinion_finish_machine_settings(self):
            from mastapy.gears.manufacturing.bevel import _803
            
            return self._parent._cast(_803.PinionFinishMachineSettings)

        @property
        def pinion_hypoid_formate_tilt_machine_settings(self):
            from mastapy.gears.manufacturing.bevel import _804
            
            return self._parent._cast(_804.PinionHypoidFormateTiltMachineSettings)

        @property
        def pinion_hypoid_generating_tilt_machine_settings(self):
            from mastapy.gears.manufacturing.bevel import _805
            
            return self._parent._cast(_805.PinionHypoidGeneratingTiltMachineSettings)

        @property
        def pinion_machine_settings_smt(self):
            from mastapy.gears.manufacturing.bevel import _806
            
            return self._parent._cast(_806.PinionMachineSettingsSMT)

        @property
        def conical_gear_tooth_surface(self) -> 'ConicalGearToothSurface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearToothSurface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearToothSurface._Cast_ConicalGearToothSurface':
        return self._Cast_ConicalGearToothSurface(self)
