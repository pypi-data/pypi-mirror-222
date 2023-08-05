"""_1896.py

InterferenceTolerance
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.tolerances import _1888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InterferenceTolerance')

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1891
    from mastapy.bearings import _1875


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceTolerance',)


class InterferenceTolerance(_1888.BearingConnectionComponent):
    """InterferenceTolerance

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_TOLERANCE

    class _Cast_InterferenceTolerance:
        """Special nested class for casting InterferenceTolerance to subclasses."""

        def __init__(self, parent: 'InterferenceTolerance'):
            self._parent = parent

        @property
        def bearing_connection_component(self):
            return self._parent._cast(_1888.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1893
            
            return self._parent._cast(_1893.InnerRingTolerance)

        @property
        def inner_support_tolerance(self):
            from mastapy.bearings.tolerances import _1894
            
            return self._parent._cast(_1894.InnerSupportTolerance)

        @property
        def outer_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1899
            
            return self._parent._cast(_1899.OuterRingTolerance)

        @property
        def outer_support_tolerance(self):
            from mastapy.bearings.tolerances import _1900
            
            return self._parent._cast(_1900.OuterSupportTolerance)

        @property
        def ring_tolerance(self):
            from mastapy.bearings.tolerances import _1904
            
            return self._parent._cast(_1904.RingTolerance)

        @property
        def support_tolerance(self):
            from mastapy.bearings.tolerances import _1909
            
            return self._parent._cast(_1909.SupportTolerance)

        @property
        def interference_tolerance(self) -> 'InterferenceTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def definition_option(self) -> '_1891.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'DefinitionOption' is the original name of this property."""

        temp = self.wrapped.DefinitionOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions')
        return constructor.new_from_mastapy('mastapy.bearings.tolerances._1891', 'BearingToleranceDefinitionOptions')(value) if value is not None else None

    @definition_option.setter
    def definition_option(self, value: '_1891.BearingToleranceDefinitionOptions'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.Tolerances.BearingToleranceDefinitionOptions')
        self.wrapped.DefinitionOption = value

    @property
    def mounting_point_surface_finish(self) -> '_1875.MountingPointSurfaceFinishes':
        """MountingPointSurfaceFinishes: 'MountingPointSurfaceFinish' is the original name of this property."""

        temp = self.wrapped.MountingPointSurfaceFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Bearings.MountingPointSurfaceFinishes')
        return constructor.new_from_mastapy('mastapy.bearings._1875', 'MountingPointSurfaceFinishes')(value) if value is not None else None

    @mounting_point_surface_finish.setter
    def mounting_point_surface_finish(self, value: '_1875.MountingPointSurfaceFinishes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Bearings.MountingPointSurfaceFinishes')
        self.wrapped.MountingPointSurfaceFinish = value

    @property
    def non_contacting_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NonContactingDiameter' is the original name of this property."""

        temp = self.wrapped.NonContactingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @non_contacting_diameter.setter
    def non_contacting_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NonContactingDiameter = value

    @property
    def surface_fitting_reduction(self) -> 'float':
        """float: 'SurfaceFittingReduction' is the original name of this property."""

        temp = self.wrapped.SurfaceFittingReduction

        if temp is None:
            return 0.0

        return temp

    @surface_fitting_reduction.setter
    def surface_fitting_reduction(self, value: 'float'):
        self.wrapped.SurfaceFittingReduction = float(value) if value is not None else 0.0

    @property
    def tolerance_lower_limit(self) -> 'float':
        """float: 'ToleranceLowerLimit' is the original name of this property."""

        temp = self.wrapped.ToleranceLowerLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_lower_limit.setter
    def tolerance_lower_limit(self, value: 'float'):
        self.wrapped.ToleranceLowerLimit = float(value) if value is not None else 0.0

    @property
    def tolerance_upper_limit(self) -> 'float':
        """float: 'ToleranceUpperLimit' is the original name of this property."""

        temp = self.wrapped.ToleranceUpperLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_upper_limit.setter
    def tolerance_upper_limit(self, value: 'float'):
        self.wrapped.ToleranceUpperLimit = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'InterferenceTolerance._Cast_InterferenceTolerance':
        return self._Cast_InterferenceTolerance(self)
