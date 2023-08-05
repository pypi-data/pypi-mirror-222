"""_786.py

ConicalPinionMicroGeometryConfig
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_PINION_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionMicroGeometryConfig')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _780


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionMicroGeometryConfig',)


class ConicalPinionMicroGeometryConfig(_774.ConicalGearMicroGeometryConfig):
    """ConicalPinionMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MICRO_GEOMETRY_CONFIG

    class _Cast_ConicalPinionMicroGeometryConfig:
        """Special nested class for casting ConicalPinionMicroGeometryConfig to subclasses."""

        def __init__(self, parent: 'ConicalPinionMicroGeometryConfig'):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config(self):
            return self._parent._cast(_774.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _775
            
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
        def conical_pinion_micro_geometry_config(self) -> 'ConicalPinionMicroGeometryConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalPinionMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(self) -> '_780.ConicalMeshFlankNURBSMicroGeometryConfig':
        """ConicalMeshFlankNURBSMicroGeometryConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_convex_ib_configuration(self) -> '_780.ConicalMeshFlankNURBSMicroGeometryConfig':
        """ConicalMeshFlankNURBSMicroGeometryConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalPinionMicroGeometryConfig._Cast_ConicalPinionMicroGeometryConfig':
        return self._Cast_ConicalPinionMicroGeometryConfig(self)
