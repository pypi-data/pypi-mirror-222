﻿"""_1301.py

UShapedLayerSpecification
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_U_SHAPED_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'UShapedLayerSpecification')

if TYPE_CHECKING:
    from mastapy.electric_machines import _1272, _1274


__docformat__ = 'restructuredtext en'
__all__ = ('UShapedLayerSpecification',)


class UShapedLayerSpecification(_1286.RotorInternalLayerSpecification):
    """UShapedLayerSpecification

    This is a mastapy class.
    """

    TYPE = _U_SHAPED_LAYER_SPECIFICATION

    class _Cast_UShapedLayerSpecification:
        """Special nested class for casting UShapedLayerSpecification to subclasses."""

        def __init__(self, parent: 'UShapedLayerSpecification'):
            self._parent = parent

        @property
        def rotor_internal_layer_specification(self):
            return self._parent._cast(_1286.RotorInternalLayerSpecification)

        @property
        def u_shaped_layer_specification(self) -> 'UShapedLayerSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UShapedLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_inner_and_outer_sections(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AngleBetweenInnerAndOuterSections' is the original name of this property."""

        temp = self.wrapped.AngleBetweenInnerAndOuterSections

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @angle_between_inner_and_outer_sections.setter
    def angle_between_inner_and_outer_sections(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleBetweenInnerAndOuterSections = value

    @property
    def bridge_offset_at_layer_bend(self) -> 'float':
        """float: 'BridgeOffsetAtLayerBend' is the original name of this property."""

        temp = self.wrapped.BridgeOffsetAtLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_offset_at_layer_bend.setter
    def bridge_offset_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeOffsetAtLayerBend = float(value) if value is not None else 0.0

    @property
    def bridge_thickness_at_layer_bend(self) -> 'float':
        """float: 'BridgeThicknessAtLayerBend' is the original name of this property."""

        temp = self.wrapped.BridgeThicknessAtLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_thickness_at_layer_bend.setter
    def bridge_thickness_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeThicknessAtLayerBend = float(value) if value is not None else 0.0

    @property
    def distance_to_layer(self) -> 'float':
        """float: 'DistanceToLayer' is the original name of this property."""

        temp = self.wrapped.DistanceToLayer

        if temp is None:
            return 0.0

        return temp

    @distance_to_layer.setter
    def distance_to_layer(self, value: 'float'):
        self.wrapped.DistanceToLayer = float(value) if value is not None else 0.0

    @property
    def magnet_configuration(self) -> '_1272.MagnetConfiguration':
        """MagnetConfiguration: 'MagnetConfiguration' is the original name of this property."""

        temp = self.wrapped.MagnetConfiguration

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.ElectricMachines.MagnetConfiguration')
        return constructor.new_from_mastapy('mastapy.electric_machines._1272', 'MagnetConfiguration')(value) if value is not None else None

    @magnet_configuration.setter
    def magnet_configuration(self, value: '_1272.MagnetConfiguration'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.ElectricMachines.MagnetConfiguration')
        self.wrapped.MagnetConfiguration = value

    @property
    def thickness_of_inner_flux_barriers(self) -> 'float':
        """float: 'ThicknessOfInnerFluxBarriers' is the original name of this property."""

        temp = self.wrapped.ThicknessOfInnerFluxBarriers

        if temp is None:
            return 0.0

        return temp

    @thickness_of_inner_flux_barriers.setter
    def thickness_of_inner_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfInnerFluxBarriers = float(value) if value is not None else 0.0

    @property
    def thickness_of_outer_flux_barriers(self) -> 'float':
        """float: 'ThicknessOfOuterFluxBarriers' is the original name of this property."""

        temp = self.wrapped.ThicknessOfOuterFluxBarriers

        if temp is None:
            return 0.0

        return temp

    @thickness_of_outer_flux_barriers.setter
    def thickness_of_outer_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfOuterFluxBarriers = float(value) if value is not None else 0.0

    @property
    def web_thickness(self) -> 'float':
        """float: 'WebThickness' is the original name of this property."""

        temp = self.wrapped.WebThickness

        if temp is None:
            return 0.0

        return temp

    @web_thickness.setter
    def web_thickness(self, value: 'float'):
        self.wrapped.WebThickness = float(value) if value is not None else 0.0

    @property
    def outer_magnets(self) -> '_1274.MagnetForLayer':
        """MagnetForLayer: 'OuterMagnets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMagnets

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'UShapedLayerSpecification._Cast_UShapedLayerSpecification':
        return self._Cast_UShapedLayerSpecification(self)
