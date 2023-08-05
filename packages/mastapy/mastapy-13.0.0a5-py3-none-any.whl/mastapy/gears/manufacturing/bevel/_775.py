"""_775.py

ConicalGearMicroGeometryConfigBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalGearMicroGeometryConfigBase')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _793


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMicroGeometryConfigBase',)


class ConicalGearMicroGeometryConfigBase(_1217.GearImplementationDetail):
    """ConicalGearMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MICRO_GEOMETRY_CONFIG_BASE

    class _Cast_ConicalGearMicroGeometryConfigBase:
        """Special nested class for casting ConicalGearMicroGeometryConfigBase to subclasses."""

        def __init__(self, parent: 'ConicalGearMicroGeometryConfigBase'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
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
        def conical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _774
            
            return self._parent._cast(_774.ConicalGearMicroGeometryConfig)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _786
            
            return self._parent._cast(_786.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _791
            
            return self._parent._cast(_791.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(self) -> 'ConicalGearMicroGeometryConfigBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_measurement_border(self) -> '_793.FlankMeasurementBorder':
        """FlankMeasurementBorder: 'FlankMeasurementBorder' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalGearMicroGeometryConfigBase._Cast_ConicalGearMicroGeometryConfigBase':
        return self._Cast_ConicalGearMicroGeometryConfigBase(self)
