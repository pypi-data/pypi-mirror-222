"""_1103.py

CylindricalGearSetMicroGeometry
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearSetMicroGeometry')

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1025, _1037, _1009
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097, _1094


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometry',)


class CylindricalGearSetMicroGeometry(_1227.GearSetImplementationDetail):
    """CylindricalGearSetMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY

    class _Cast_CylindricalGearSetMicroGeometry:
        """Special nested class for casting CylindricalGearSetMicroGeometry to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetMicroGeometry'):
            self._parent = parent

        @property
        def gear_set_implementation_detail(self):
            return self._parent._cast(_1227.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry(self) -> 'CylindricalGearSetMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set_design(self) -> '_1025.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometries(self) -> 'List[_1097.CylindricalGearMicroGeometryBase]':
        """List[CylindricalGearMicroGeometryBase]: 'CylindricalGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_micro_geometries(self) -> 'List[_1094.CylindricalGearMeshMicroGeometry]':
        """List[CylindricalGearMeshMicroGeometry]: 'CylindricalMeshMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'CylindricalGearSetMicroGeometry':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_and_add_to(self, gear_set_design: '_1025.CylindricalGearSetDesign') -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateAndAddTo' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign)

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.DuplicateAndAddTo(gear_set_design.wrapped if gear_set_design else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_planet(self) -> '_1227.GearSetImplementationDetail':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachPlanet' is the original name of this method.

        Returns:
            mastapy.gears.analysis.GearSetImplementationDetail
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanet()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_planet_and_add_to(self, gear_set_design: '_1037.CylindricalPlanetaryGearSetDesign') -> '_1227.GearSetImplementationDetail':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachPlanetAndAddTo' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalPlanetaryGearSetDesign)

        Returns:
            mastapy.gears.analysis.GearSetImplementationDetail
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanetAndAddTo(gear_set_design.wrapped if gear_set_design else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_tooth(self) -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachTooth' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachTooth()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_tooth_for(self, gears: 'List[_1009.CylindricalGearDesign]') -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachToothFor' is the original name of this method.

        Args:
            gears (List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign])

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        gears = conversion.mp_to_pn_objects_in_list(gears)
        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachToothFor(gears)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry':
        return self._Cast_CylindricalGearSetMicroGeometry(self)
