﻿"""_488.py

PlasticGearVDI2736AbstractGearSingleFlankRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.cylindrical.iso6336 import _514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticGearVDI2736AbstractGearSingleFlankRating')

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _492
    from mastapy.materials import _283, _284


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticGearVDI2736AbstractGearSingleFlankRating',)


class PlasticGearVDI2736AbstractGearSingleFlankRating(_514.ISO6336AbstractGearSingleFlankRating):
    """PlasticGearVDI2736AbstractGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING

    class _Cast_PlasticGearVDI2736AbstractGearSingleFlankRating:
        """Special nested class for casting PlasticGearVDI2736AbstractGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'PlasticGearVDI2736AbstractGearSingleFlankRating'):
            self._parent = parent

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            return self._parent._cast(_514.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _463
            
            return self._parent._cast(_463.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(self):
            from mastapy.gears.rating import _362
            
            return self._parent._cast(_362.GearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493
            
            return self._parent._cast(_493.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494
            
            return self._parent._cast(_494.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(self) -> 'PlasticGearVDI2736AbstractGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticGearVDI2736AbstractGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self) -> 'float':
        """float: 'AllowableStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_number_contact(self) -> 'float':
        """float: 'AllowableStressNumberContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @property
    def averaged_linear_wear(self) -> 'float':
        """float: 'AveragedLinearWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragedLinearWear

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankHeatTransferCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankHeatTransferCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def flank_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankTemperature' is the original name of this property."""

        temp = self.wrapped.FlankTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @flank_temperature.setter
    def flank_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FlankTemperature = value

    @property
    def important_note_on_contact_durability_of_pom(self) -> 'str':
        """str: 'ImportantNoteOnContactDurabilityOfPOM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportantNoteOnContactDurabilityOfPOM

        if temp is None:
            return ''

        return temp

    @property
    def minimum_factor_of_safety_bending_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyBendingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyBendingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_factor_of_safety_pitting_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyPittingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyPittingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_factor_of_safety_wear(self) -> 'float':
        """float: 'MinimumFactorOfSafetyWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyWear

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tooth_root_stress(self) -> 'float':
        """float: 'NominalToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress(self) -> 'float':
        """float: 'PermissibleContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit(self) -> 'float':
        """float: 'PittingStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_line_length_of_the_active_tooth_flank(self) -> 'float':
        """float: 'ProfileLineLengthOfTheActiveToothFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileLineLengthOfTheActiveToothFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def root_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootHeatTransferCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootHeatTransferCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def root_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootTemperature' is the original name of this property."""

        temp = self.wrapped.RootTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @root_temperature.setter
    def root_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootTemperature = value

    @property
    def tooth_root_stress_limit(self) -> 'float':
        """float: 'ToothRootStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def standard_plastic_sn_curve_for_the_specified_operating_conditions(self) -> '_492.PlasticSNCurveForTheSpecifiedOperatingConditions':
        """PlasticSNCurveForTheSpecifiedOperatingConditions: 'StandardPlasticSNCurveForTheSpecifiedOperatingConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StandardPlasticSNCurveForTheSpecifiedOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bending_stress_cycle_data_for_damage_tables(self) -> 'List[_283.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]':
        """List[StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]: 'BendingStressCycleDataForDamageTables' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_stress_cycle_data_for_damage_tables(self) -> 'List[_284.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]':
        """List[StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]: 'ContactStressCycleDataForDamageTables' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating':
        return self._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating(self)
