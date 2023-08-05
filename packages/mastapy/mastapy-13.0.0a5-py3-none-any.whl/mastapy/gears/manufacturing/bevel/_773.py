"""_773.py

ConicalGearManufacturingConfig
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.bevel import _775
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalGearManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearManufacturingConfig',)


class ConicalGearManufacturingConfig(_775.ConicalGearMicroGeometryConfigBase):
    """ConicalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_CONFIG

    class _Cast_ConicalGearManufacturingConfig:
        """Special nested class for casting ConicalGearManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalGearManufacturingConfig'):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config_base(self):
            return self._parent._cast(_775.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1217
            
            return self._parent._cast(_1217.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalPinionManufacturingConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _791
            
            return self._parent._cast(_791.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(self) -> 'ConicalGearManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig':
        return self._Cast_ConicalGearManufacturingConfig(self)
