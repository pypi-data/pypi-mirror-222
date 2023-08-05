﻿"""_764.py

ShavingDynamicsCalculationForDesignedGears
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _763
from mastapy._internal.cast_exception import CastException

_REPORTING_OVERRIDABLE = python_net_import('SMT.MastaAPI.Utility.Property', 'ReportingOverridable')
_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsCalculationForDesignedGears')

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1854
    from mastapy.gears.gear_designs.cylindrical import _1022
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761, _758, _762


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsCalculationForDesignedGears',)


T = TypeVar('T', bound='_762.ShavingDynamics')


class ShavingDynamicsCalculationForDesignedGears(_763.ShavingDynamicsCalculation[T]):
    """ShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS

    class _Cast_ShavingDynamicsCalculationForDesignedGears:
        """Special nested class for casting ShavingDynamicsCalculationForDesignedGears to subclasses."""

        def __init__(self, parent: 'ShavingDynamicsCalculationForDesignedGears'):
            self._parent = parent

        @property
        def shaving_dynamics_calculation(self):
            return self._parent._cast(_763.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_designed_gears(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _749
            
            return self._parent._cast(_749.ConventionalShavingDynamicsCalculationForDesignedGears)

        @property
        def plunge_shaving_dynamics_calculation_for_designed_gears(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _755
            
            return self._parent._cast(_755.PlungeShavingDynamicsCalculationForDesignedGears)

        @property
        def shaving_dynamics_calculation_for_designed_gears(self) -> 'ShavingDynamicsCalculationForDesignedGears':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsCalculationForDesignedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def redressing_chart(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_redressing(self) -> 'list_with_selected_item.ListWithSelectedItem_T':
        """list_with_selected_item.ListWithSelectedItem_T: 'SelectedRedressing' is the original name of this property."""

        temp = self.wrapped.SelectedRedressing

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_T')(temp) if temp is not None else None

    @selected_redressing.setter
    def selected_redressing(self, value: 'list_with_selected_item.ListWithSelectedItem_T.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def end_of_shaving_profile(self) -> '_1022.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing(self) -> '_761.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'Redressing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Redressing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def start_of_shaving_profile(self) -> '_1022.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'StartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_settings(self) -> 'List[_758.RedressingSettings[T]]':
        """List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingSettings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears':
        return self._Cast_ShavingDynamicsCalculationForDesignedGears(self)
