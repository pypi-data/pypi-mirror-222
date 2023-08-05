"""_782.py

ConicalMeshManufacturingConfig
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingConfig')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _785, _791


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingConfig',)


class ConicalMeshManufacturingConfig(_784.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG

    class _Cast_ConicalMeshManufacturingConfig:
        """Special nested class for casting ConicalMeshManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalMeshManufacturingConfig'):
            self._parent = parent

        @property
        def conical_mesh_micro_geometry_config_base(self):
            return self._parent._cast(_784.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1221
            
            return self._parent._cast(_1221.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_config(self) -> 'ConicalMeshManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_config(self) -> '_785.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'PinionConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_791.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshManufacturingConfig._Cast_ConicalMeshManufacturingConfig':
        return self._Cast_ConicalMeshManufacturingConfig(self)
