﻿"""_463.py

CylindricalGearSingleFlankRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating import _362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSingleFlankRating')

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _459
    from mastapy.gears.rating import _355
    from mastapy.materials import _273


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSingleFlankRating',)


class CylindricalGearSingleFlankRating(_362.GearSingleFlankRating):
    """CylindricalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SINGLE_FLANK_RATING

    class _Cast_CylindricalGearSingleFlankRating:
        """Special nested class for casting CylindricalGearSingleFlankRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearSingleFlankRating'):
            self._parent = parent

        @property
        def gear_single_flank_rating(self):
            return self._parent._cast(_362.GearSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _488
            
            return self._parent._cast(_488.PlasticGearVDI2736AbstractGearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493
            
            return self._parent._cast(_493.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(self):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494
            
            return self._parent._cast(_494.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh)

        @property
        def iso63361996_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _508
            
            return self._parent._cast(_508.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _510
            
            return self._parent._cast(_510.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _512
            
            return self._parent._cast(_512.ISO63362019GearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _514
            
            return self._parent._cast(_514.ISO6336AbstractGearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _516
            
            return self._parent._cast(_516.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _529
            
            return self._parent._cast(_529.DIN3990GearSingleFlankRating)

        @property
        def agma2101_gear_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.agma import _531
            
            return self._parent._cast(_531.AGMA2101GearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(self) -> 'CylindricalGearSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSingleFlankRating.TYPE'):
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
    def angular_velocity(self) -> 'float':
        """float: 'AngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocity

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
    def axial_pitch(self) -> 'float':
        """float: 'AxialPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_helix_angle(self) -> 'float':
        """float: 'BaseHelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def base_transverse_pitch(self) -> 'float':
        """float: 'BaseTransversePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseTransversePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_moment_arm(self) -> 'float':
        """float: 'BendingMomentArm' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingMomentArm

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_fatigue(self) -> 'float':
        """float: 'BendingSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_contact_stress(self) -> 'float':
        """float: 'CalculatedContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_tip_relief(self) -> 'float':
        """float: 'CombinedTipRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedTipRelief

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'ContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_source(self) -> 'str':
        """str: 'ContactStressSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressSource

        if temp is None:
            return ''

        return temp

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_wear(self) -> 'float':
        """float: 'DamageWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageWear

        if temp is None:
            return 0.0

        return temp

    @property
    def fillet_roughness_rz(self) -> 'float':
        """float: 'FilletRoughnessRz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletRoughnessRz

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_roughness_rz(self) -> 'float':
        """float: 'FlankRoughnessRz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankRoughnessRz

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_rotation_speed(self) -> 'float':
        """float: 'GearRotationSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_data_source_for_rating(self) -> '_459.CylindricalGearRatingGeometryDataSource':
        """CylindricalGearRatingGeometryDataSource: 'GeometryDataSourceForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryDataSourceForRating

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Cylindrical.CylindricalGearRatingGeometryDataSource')
        return constructor.new_from_mastapy('mastapy.gears.rating.cylindrical._459', 'CylindricalGearRatingGeometryDataSource')(value) if value is not None else None

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def is_gear_driving_or_driven(self) -> '_355.FlankLoadingState':
        """FlankLoadingState: 'IsGearDrivingOrDriven' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsGearDrivingOrDriven

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.FlankLoadingState')
        return constructor.new_from_mastapy('mastapy.gears.rating._355', 'FlankLoadingState')(value) if value is not None else None

    @property
    def life_factor_for_contact_stress(self) -> 'float':
        """float: 'LifeFactorForContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def metal_plastic(self) -> '_273.MetalPlasticType':
        """MetalPlasticType: 'MetalPlastic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MetalPlastic

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.MetalPlasticType')
        return constructor.new_from_mastapy('mastapy.materials._273', 'MetalPlasticType')(value) if value is not None else None

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
    def nominal_stress_number_bending(self) -> 'float':
        """float: 'NominalStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngle

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
    def permissible_contact_stress_for_reference_stress(self) -> 'float':
        """float: 'PermissibleContactStressForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStressForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_for_static_stress(self) -> 'float':
        """float: 'PermissibleContactStressForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStressForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_linear_wear(self) -> 'float':
        """float: 'PermissibleLinearWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleLinearWear

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
    def permissible_tooth_root_bending_stress_for_reference_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStressForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStressForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress_for_static_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStressForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStressForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter

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
    def pitting_stress_limit_for_reference_stress(self) -> 'float':
        """float: 'PittingStressLimitForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimitForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit_for_static_stress(self) -> 'float':
        """float: 'PittingStressLimitForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimitForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_bending(self) -> 'float':
        """float: 'ReliabilityBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_contact(self) -> 'float':
        """float: 'ReliabilityContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def reversed_bending_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ReversedBendingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def rim_thickness(self) -> 'float':
        """float: 'RimThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_factor(self) -> 'float':
        """float: 'RimThicknessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_over_normal_module(self) -> 'float':
        """float: 'RimThicknessOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessOverNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def root_fillet_radius(self) -> 'float':
        """float: 'RootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_wear(self) -> 'float':
        """float: 'SafetyFactorWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorWear

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor_contact(self) -> 'float':
        """float: 'SizeFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor_bending(self) -> 'float':
        """float: 'StaticSafetyFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def static_safety_factor_contact(self) -> 'float':
        """float: 'StaticSafetyFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_cycle_factor_bending(self) -> 'float':
        """float: 'StressCycleFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCycleFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_contact_coefficient_for_report(self) -> 'float':
        """float: 'ThermalContactCoefficientForReport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermalContactCoefficientForReport

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed(self) -> 'float':
        """float: 'ToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_chord_at_critical_section(self) -> 'float':
        """float: 'ToothRootChordAtCriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootChordAtCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress(self) -> 'float':
        """float: 'ToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStress

        if temp is None:
            return 0.0

        return temp

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
    def tooth_root_stress_limit_for_reference_stress(self) -> 'float':
        """float: 'ToothRootStressLimitForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimitForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_limit_for_static_stress(self) -> 'float':
        """float: 'ToothRootStressLimitForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimitForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_source(self) -> 'str':
        """str: 'ToothRootStressSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressSource

        if temp is None:
            return ''

        return temp

    @property
    def transverse_module(self) -> 'float':
        """float: 'TransverseModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseModule

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pitch(self) -> 'float':
        """float: 'TransversePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self) -> 'float':
        """float: 'TransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def welding_structural_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WeldingStructuralFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WeldingStructuralFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @property
    def cast_to(self) -> 'CylindricalGearSingleFlankRating._Cast_CylindricalGearSingleFlankRating':
        return self._Cast_CylindricalGearSingleFlankRating(self)
