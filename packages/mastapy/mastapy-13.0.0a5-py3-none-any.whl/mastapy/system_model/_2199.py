"""_2199.py

MASTASettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel', 'MASTASettings')

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1962
    from mastapy.bearings import (
        _1866, _1867, _1880, _1886
    )
    from mastapy.bolts import _1459, _1461, _1466
    from mastapy.cycloidal import _1447, _1454
    from mastapy.electric_machines import _1276, _1294, _1306
    from mastapy.gears import _314, _315, _341
    from mastapy.gears.gear_designs import (
        _937, _939, _942, _948
    )
    from mastapy.gears.gear_designs.cylindrical import (
        _1008, _1012, _1013, _1018,
        _1029
    )
    from mastapy.gears.gear_set_pareto_optimiser import (
        _917, _918, _921, _922,
        _924, _925, _927, _928,
        _930, _931, _932, _933
    )
    from mastapy.gears.ltca.cylindrical import _852
    from mastapy.gears.manufacturing.bevel import _797
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _702, _708, _713, _714
    )
    from mastapy.gears.manufacturing.cylindrical import _612, _623
    from mastapy.gears.materials import (
        _583, _585, _586, _587,
        _590, _593, _596, _597,
        _604
    )
    from mastapy.gears.rating.cylindrical import (
        _450, _451, _466, _467
    )
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6551
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5733
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5434
    from mastapy.system_model.analyses_and_results.modal_analyses import _4632
    from mastapy.system_model.analyses_and_results.power_flows import _4101
    from mastapy.system_model.analyses_and_results.stability_analyses import _3851
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3072
    from mastapy.system_model.analyses_and_results.system_deflections import _2808
    from mastapy.system_model.drawing import _2235
    from mastapy.system_model.optimization import _2215, _2224
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2546
    from mastapy.system_model.part_model import _2453
    from mastapy.materials import (
        _244, _247, _266, _269,
        _270
    )
    from mastapy.nodal_analysis import _48, _49, _68
    from mastapy.nodal_analysis.geometry_modeller_link import _160
    from mastapy.shafts import _25, _38, _39
    from mastapy.utility.cad_export import _1821
    from mastapy.utility.databases import _1816
    from mastapy.utility import _1587, _1588
    from mastapy.utility.scripting import _1730
    from mastapy.utility.units_and_measurements import _1597


__docformat__ = 'restructuredtext en'
__all__ = ('MASTASettings',)


class MASTASettings(_0.APIBase):
    """MASTASettings

    This is a mastapy class.
    """

    TYPE = _MASTA_SETTINGS

    class _Cast_MASTASettings:
        """Special nested class for casting MASTASettings to subclasses."""

        def __init__(self, parent: 'MASTASettings'):
            self._parent = parent

        @property
        def masta_settings(self) -> 'MASTASettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MASTASettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self) -> '_1962.ISO14179SettingsDatabase':
        """ISO14179SettingsDatabase: 'ISO14179SettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179SettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings(self) -> '_1866.BearingSettings':
        """BearingSettings: 'BearingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings_database(self) -> '_1867.BearingSettingsDatabase':
        """BearingSettingsDatabase: 'BearingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rolling_bearing_database(self) -> '_1880.RollingBearingDatabase':
        """RollingBearingDatabase: 'RollingBearingDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def skf_settings(self) -> '_1886.SKFSettings':
        """SKFSettings: 'SKFSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_geometry_database(self) -> '_1459.BoltGeometryDatabase':
        """BoltGeometryDatabase: 'BoltGeometryDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltGeometryDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_material_database(self) -> '_1461.BoltMaterialDatabase':
        """BoltMaterialDatabase: 'BoltMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clamped_section_material_database(self) -> '_1466.ClampedSectionMaterialDatabase':
        """ClampedSectionMaterialDatabase: 'ClampedSectionMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClampedSectionMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cycloidal_disc_material_database(self) -> '_1447.CycloidalDiscMaterialDatabase':
        """CycloidalDiscMaterialDatabase: 'CycloidalDiscMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_material_database(self) -> '_1454.RingPinsMaterialDatabase':
        """RingPinsMaterialDatabase: 'RingPinsMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnet_material_database(self) -> '_1276.MagnetMaterialDatabase':
        """MagnetMaterialDatabase: 'MagnetMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_rotor_material_database(self) -> '_1294.StatorRotorMaterialDatabase':
        """StatorRotorMaterialDatabase: 'StatorRotorMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorRotorMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_material_database(self) -> '_1306.WindingMaterialDatabase':
        """WindingMaterialDatabase: 'WindingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings(self) -> '_314.BevelHypoidGearDesignSettings':
        """BevelHypoidGearDesignSettings: 'BevelHypoidGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings(self) -> '_315.BevelHypoidGearRatingSettings':
        """BevelHypoidGearRatingSettings: 'BevelHypoidGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings_database(self) -> '_937.BevelHypoidGearDesignSettingsDatabase':
        """BevelHypoidGearDesignSettingsDatabase: 'BevelHypoidGearDesignSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings_database(self) -> '_939.BevelHypoidGearRatingSettingsDatabase':
        """BevelHypoidGearRatingSettingsDatabase: 'BevelHypoidGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_defaults(self) -> '_1008.CylindricalGearDefaults':
        """CylindricalGearDefaults: 'CylindricalGearDefaults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDefaults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraints_database(self) -> '_1012.CylindricalGearDesignConstraintsDatabase':
        """CylindricalGearDesignConstraintsDatabase: 'CylindricalGearDesignConstraintsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraint_settings(self) -> '_1013.CylindricalGearDesignConstraintSettings':
        """CylindricalGearDesignConstraintSettings: 'CylindricalGearDesignConstraintSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_settings_database(self) -> '_1018.CylindricalGearMicroGeometrySettingsDatabase':
        """CylindricalGearMicroGeometrySettingsDatabase: 'CylindricalGearMicroGeometrySettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_micro_geometry_settings(self) -> '_1029.CylindricalGearSetMicroGeometrySettings':
        """CylindricalGearSetMicroGeometrySettings: 'CylindricalGearSetMicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometrySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_constraint_collection_database(self) -> '_942.DesignConstraintCollectionDatabase':
        """DesignConstraintCollectionDatabase: 'DesignConstraintCollectionDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraintCollectionDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_design_constraints_collection(self) -> '_948.SelectedDesignConstraintsCollection':
        """SelectedDesignConstraintsCollection: 'SelectedDesignConstraintsCollection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedDesignConstraintsCollection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(self) -> '_917.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> '_918.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_921.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> '_922.ParetoCylindricalGearSetOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetOptimisationStrategyDatabase: 'ParetoCylindricalGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_924.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_face_gear_set_optimisation_strategy_database(self) -> '_925.ParetoFaceGearSetOptimisationStrategyDatabase':
        """ParetoFaceGearSetOptimisationStrategyDatabase: 'ParetoFaceGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_927.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(self) -> '_928.ParetoHypoidGearSetOptimisationStrategyDatabase':
        """ParetoHypoidGearSetOptimisationStrategyDatabase: 'ParetoHypoidGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_930.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self) -> '_931.ParetoSpiralBevelGearSetOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_932.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> '_933.ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_fe_settings(self) -> '_852.CylindricalGearFESettings':
        """CylindricalGearFESettings: 'CylindricalGearFESettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearFESettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_machine_database(self) -> '_797.ManufacturingMachineDatabase':
        """ManufacturingMachineDatabase: 'ManufacturingMachineDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingMachineDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_formed_wheel_grinder_database(self) -> '_702.CylindricalFormedWheelGrinderDatabase':
        """CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plunge_shaver_database(self) -> '_708.CylindricalGearPlungeShaverDatabase':
        """CylindricalGearPlungeShaverDatabase: 'CylindricalGearPlungeShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlungeShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_shaver_database(self) -> '_713.CylindricalGearShaverDatabase':
        """CylindricalGearShaverDatabase: 'CylindricalGearShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearShaverDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_worm_grinder_database(self) -> '_714.CylindricalWormGrinderDatabase':
        """CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalWormGrinderDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_hob_database(self) -> '_612.CylindricalHobDatabase':
        """CylindricalHobDatabase: 'CylindricalHobDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalHobDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_shaper_database(self) -> '_623.CylindricalShaperDatabase':
        """CylindricalShaperDatabase: 'CylindricalShaperDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalShaperDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_iso_material_database(self) -> '_583.BevelGearISOMaterialDatabase':
        """BevelGearISOMaterialDatabase: 'BevelGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_database(self) -> '_585.BevelGearMaterialDatabase':
        """BevelGearMaterialDatabase: 'BevelGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_agma_material_database(self) -> '_586.CylindricalGearAGMAMaterialDatabase':
        """CylindricalGearAGMAMaterialDatabase: 'CylindricalGearAGMAMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_iso_material_database(self) -> '_587.CylindricalGearISOMaterialDatabase':
        """CylindricalGearISOMaterialDatabase: 'CylindricalGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearISOMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plastic_material_database(self) -> '_590.CylindricalGearPlasticMaterialDatabase':
        """CylindricalGearPlasticMaterialDatabase: 'CylindricalGearPlasticMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_material_expert_system_factor_settings(self) -> '_593.GearMaterialExpertSystemFactorSettings':
        """GearMaterialExpertSystemFactorSettings: 'GearMaterialExpertSystemFactorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMaterialExpertSystemFactorSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(self) -> '_596.ISOTR1417912001CoefficientOfFrictionConstantsDatabase':
        """ISOTR1417912001CoefficientOfFrictionConstantsDatabase: 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTR1417912001CoefficientOfFrictionConstantsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_material_database(self) -> '_597.KlingelnbergConicalGearMaterialDatabase':
        """KlingelnbergConicalGearMaterialDatabase: 'KlingelnbergConicalGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def raw_material_database(self) -> '_604.RawMaterialDatabase':
        """RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RawMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pocketing_power_loss_coefficients_database(self) -> '_341.PocketingPowerLossCoefficientsDatabase':
        """PocketingPowerLossCoefficientsDatabase: 'PocketingPowerLossCoefficientsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PocketingPowerLossCoefficientsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings(self) -> '_450.CylindricalGearDesignAndRatingSettings':
        """CylindricalGearDesignAndRatingSettings: 'CylindricalGearDesignAndRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings_database(self) -> '_451.CylindricalGearDesignAndRatingSettingsDatabase':
        """CylindricalGearDesignAndRatingSettingsDatabase: 'CylindricalGearDesignAndRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings(self) -> '_466.CylindricalPlasticGearRatingSettings':
        """CylindricalPlasticGearRatingSettings: 'CylindricalPlasticGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings_database(self) -> '_467.CylindricalPlasticGearRatingSettingsDatabase':
        """CylindricalPlasticGearRatingSettingsDatabase: 'CylindricalPlasticGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speed_analysis_draw_style(self) -> '_6551.CriticalSpeedAnalysisDrawStyle':
        """CriticalSpeedAnalysisDrawStyle: 'CriticalSpeedAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_draw_style(self) -> '_5733.HarmonicAnalysisDrawStyle':
        """HarmonicAnalysisDrawStyle: 'HarmonicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mbd_analysis_draw_style(self) -> '_5434.MBDAnalysisDrawStyle':
        """MBDAnalysisDrawStyle: 'MBDAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MBDAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis_draw_style(self) -> '_4632.ModalAnalysisDrawStyle':
        """ModalAnalysisDrawStyle: 'ModalAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_draw_style(self) -> '_4101.PowerFlowDrawStyle':
        """PowerFlowDrawStyle: 'PowerFlowDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis_draw_style(self) -> '_3851.StabilityAnalysisDrawStyle':
        """StabilityAnalysisDrawStyle: 'StabilityAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response_draw_style(self) -> '_3072.SteadyStateSynchronousResponseDrawStyle':
        """SteadyStateSynchronousResponseDrawStyle: 'SteadyStateSynchronousResponseDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_draw_style(self) -> '_2808.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'SystemDeflectionDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def model_view_options_draw_style(self) -> '_2235.ModelViewOptionsDrawStyle':
        """ModelViewOptionsDrawStyle: 'ModelViewOptionsDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelViewOptionsDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_optimization_strategy_database(self) -> '_2215.ConicalGearOptimizationStrategyDatabase':
        """ConicalGearOptimizationStrategyDatabase: 'ConicalGearOptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimization_strategy_database(self) -> '_2224.OptimizationStrategyDatabase':
        """OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimizationStrategyDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_set_database(self) -> '_2546.SuperchargerRotorSetDatabase':
        """SuperchargerRotorSetDatabase: 'SuperchargerRotorSetDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSetDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_carrier_settings(self) -> '_2453.PlanetCarrierSettings':
        """PlanetCarrierSettings: 'PlanetCarrierSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarrierSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_material_database(self) -> '_244.BearingMaterialDatabase':
        """BearingMaterialDatabase: 'BearingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_material_database(self) -> '_247.ComponentMaterialDatabase':
        """ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lubrication_detail_database(self) -> '_266.LubricationDetailDatabase':
        """LubricationDetailDatabase: 'LubricationDetailDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetailDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings(self) -> '_269.MaterialsSettings':
        """MaterialsSettings: 'MaterialsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings_database(self) -> '_270.MaterialsSettingsDatabase':
        """MaterialsSettingsDatabase: 'MaterialsSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings(self) -> '_48.AnalysisSettings':
        """AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings_database(self) -> '_49.AnalysisSettingsDatabase':
        """AnalysisSettingsDatabase: 'AnalysisSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fe_user_settings(self) -> '_68.FEUserSettings':
        """FEUserSettings: 'FEUserSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEUserSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def geometry_modeller_settings(self) -> '_160.GeometryModellerSettings':
        """GeometryModellerSettings: 'GeometryModellerSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryModellerSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_material_database(self) -> '_25.ShaftMaterialDatabase':
        """ShaftMaterialDatabase: 'ShaftMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMaterialDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        """ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings_database(self) -> '_39.ShaftSettingsDatabase':
        """ShaftSettingsDatabase: 'ShaftSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettingsDatabase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cad_export_settings(self) -> '_1821.CADExportSettings':
        """CADExportSettings: 'CADExportSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CADExportSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def database_settings(self) -> '_1816.DatabaseSettings':
        """DatabaseSettings: 'DatabaseSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DatabaseSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def program_settings(self) -> '_1587.ProgramSettings':
        """ProgramSettings: 'ProgramSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProgramSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pushbullet_settings(self) -> '_1588.PushbulletSettings':
        """PushbulletSettings: 'PushbulletSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PushbulletSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def scripting_setup(self) -> '_1730.ScriptingSetup':
        """ScriptingSetup: 'ScriptingSetup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScriptingSetup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def measurement_settings(self) -> '_1597.MeasurementSettings':
        """MeasurementSettings: 'MeasurementSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MASTASettings._Cast_MASTASettings':
        return self._Cast_MASTASettings(self)
