"""_1063.py

RelativeMeasurementViewModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_MEASUREMENT_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'RelativeMeasurementViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('RelativeMeasurementViewModel',)


T = TypeVar('T')


class RelativeMeasurementViewModel(_0.APIBase, Generic[T]):
    """RelativeMeasurementViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_MEASUREMENT_VIEW_MODEL

    class _Cast_RelativeMeasurementViewModel:
        """Special nested class for casting RelativeMeasurementViewModel to subclasses."""

        def __init__(self, parent: 'RelativeMeasurementViewModel'):
            self._parent = parent

        @property
        def cylindrical_mesh_angular_backlash(self):
            from mastapy.gears.gear_designs.cylindrical import _1033
            
            return self._parent._cast(_1033.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _1036
            
            return self._parent._cast(_1036.CylindricalMeshLinearBacklashSpecification)

        @property
        def toleranced_value_specification(self):
            from mastapy.gears.gear_designs.cylindrical import _1079
            
            return self._parent._cast(_1079.TolerancedValueSpecification)

        @property
        def nominal_value_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1087
            
            return self._parent._cast(_1087.NominalValueSpecification)

        @property
        def no_value_specification(self):
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1088
            
            return self._parent._cast(_1088.NoValueSpecification)

        @property
        def relative_measurement_view_model(self) -> 'RelativeMeasurementViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RelativeMeasurementViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel':
        return self._Cast_RelativeMeasurementViewModel(self)
