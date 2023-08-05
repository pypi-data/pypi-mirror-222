"""_1095.py

CylindricalGearMeshMicroGeometryDutyCycle
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMeshMicroGeometryDutyCycle')

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _461
    from mastapy.gears.ltca.cylindrical import _854


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshMicroGeometryDutyCycle',)


class CylindricalGearMeshMicroGeometryDutyCycle(_1218.GearMeshDesignAnalysis):
    """CylindricalGearMeshMicroGeometryDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY_DUTY_CYCLE

    class _Cast_CylindricalGearMeshMicroGeometryDutyCycle:
        """Special nested class for casting CylindricalGearMeshMicroGeometryDutyCycle to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshMicroGeometryDutyCycle'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(self) -> 'CylindricalGearMeshMicroGeometryDutyCycle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshMicroGeometryDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set_duty_cycle_rating(self) -> '_461.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'CylindricalGearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshes_analysis(self) -> 'List[_854.CylindricalGearMeshLoadDistributionAnalysis]':
        """List[CylindricalGearMeshLoadDistributionAnalysis]: 'MeshesAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMeshMicroGeometryDutyCycle._Cast_CylindricalGearMeshMicroGeometryDutyCycle':
        return self._Cast_CylindricalGearMeshMicroGeometryDutyCycle(self)
