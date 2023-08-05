﻿"""_2480.py

CylindricalGearFromCAD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.import_from_cad import _2486
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'CylindricalGearFromCAD')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2508, _2507
    from mastapy.geometry.two_d import _310


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFromCAD',)


class CylindricalGearFromCAD(_2486.MountableComponentFromCAD):
    """CylindricalGearFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FROM_CAD

    class _Cast_CylindricalGearFromCAD:
        """Special nested class for casting CylindricalGearFromCAD to subclasses."""

        def __init__(self, parent: 'CylindricalGearFromCAD'):
            self._parent = parent

        @property
        def mountable_component_from_cad(self):
            return self._parent._cast(_2486.MountableComponentFromCAD)

        @property
        def component_from_cad(self):
            from mastapy.system_model.part_model.import_from_cad import _2477
            
            return self._parent._cast(_2477.ComponentFromCAD)

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
        def cylindrical_gear_from_cad(self) -> 'CylindricalGearFromCAD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_drawing_diameter(self) -> 'float':
        """float: 'CADDrawingDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CADDrawingDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_distance(self) -> 'float':
        """float: 'CentreDistance' is the original name of this property."""

        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    def centre_distance(self, value: 'float'):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def existing_gear_set(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGearSet: 'ExistingGearSet' is the original name of this property."""

        temp = self.wrapped.ExistingGearSet

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_CylindricalGearSet')(temp) if temp is not None else None

    @existing_gear_set.setter
    def existing_gear_set(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ExistingGearSet = value

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def gear_set_name(self) -> 'str':
        """str: 'GearSetName' is the original name of this property."""

        temp = self.wrapped.GearSetName

        if temp is None:
            return ''

        return temp

    @gear_set_name.setter
    def gear_set_name(self, value: 'str'):
        self.wrapped.GearSetName = str(value) if value is not None else ''

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def internal_external(self) -> '_310.InternalExternalType':
        """InternalExternalType: 'InternalExternal' is the original name of this property."""

        temp = self.wrapped.InternalExternal

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Geometry.TwoD.InternalExternalType')
        return constructor.new_from_mastapy('mastapy.geometry.two_d._310', 'InternalExternalType')(value) if value is not None else None

    @internal_external.setter
    def internal_external(self, value: '_310.InternalExternalType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Geometry.TwoD.InternalExternalType')
        self.wrapped.InternalExternal = value

    @property
    def meshing_gear(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGear':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGear: 'MeshingGear' is the original name of this property."""

        temp = self.wrapped.MeshingGear

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_CylindricalGear')(temp) if temp is not None else None

    @meshing_gear.setter
    def meshing_gear(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGear.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGear.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGear.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.MeshingGear = value

    @property
    def normal_module(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NormalModule' is the original name of this property."""

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @normal_module.setter
    def normal_module(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NormalModule = value

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    def normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def number_of_teeth(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_int')(temp) if temp is not None else 0

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfTeeth = value

    @property
    def root_diameter(self) -> 'float':
        """float: 'RootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self) -> 'float':
        """float: 'TipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'CylindricalGearFromCAD._Cast_CylindricalGearFromCAD':
        return self._Cast_CylindricalGearFromCAD(self)
