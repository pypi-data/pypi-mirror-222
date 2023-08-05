﻿"""_1813.py

Database
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE = python_net_import('SMT.MastaAPI.Utility.Databases', 'Database')

if TYPE_CHECKING:
    from mastapy.utility.databases import _1815


__docformat__ = 'restructuredtext en'
__all__ = ('Database',)


TKey = TypeVar('TKey', bound='_1815.DatabaseKey')
TValue = TypeVar('TValue', bound='_0.APIBase')


class Database(_0.APIBase, Generic[TKey, TValue]):
    """Database

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _DATABASE

    class _Cast_Database:
        """Special nested class for casting Database to subclasses."""

        def __init__(self, parent: 'Database'):
            self._parent = parent

        @property
        def shaft_material_database(self):
            from mastapy.shafts import _25
            
            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(self):
            from mastapy.shafts import _39
            
            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(self):
            from mastapy.nodal_analysis import _49
            
            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(self):
            from mastapy.materials import _244
            
            return self._parent._cast(_244.BearingMaterialDatabase)

        @property
        def component_material_database(self):
            from mastapy.materials import _247
            
            return self._parent._cast(_247.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(self):
            from mastapy.materials import _266
            
            return self._parent._cast(_266.LubricationDetailDatabase)

        @property
        def material_database(self):
            from mastapy.materials import _268
            
            return self._parent._cast(_268.MaterialDatabase)

        @property
        def materials_settings_database(self):
            from mastapy.materials import _270
            
            return self._parent._cast(_270.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(self):
            from mastapy.gears import _341
            
            return self._parent._cast(_341.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(self):
            from mastapy.gears.rating.cylindrical import _451
            
            return self._parent._cast(_451.CylindricalGearDesignAndRatingSettingsDatabase)

        @property
        def cylindrical_plastic_gear_rating_settings_database(self):
            from mastapy.gears.rating.cylindrical import _467
            
            return self._parent._cast(_467.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(self):
            from mastapy.gears.materials import _581
            
            return self._parent._cast(_581.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(self):
            from mastapy.gears.materials import _583
            
            return self._parent._cast(_583.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(self):
            from mastapy.gears.materials import _585
            
            return self._parent._cast(_585.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(self):
            from mastapy.gears.materials import _586
            
            return self._parent._cast(_586.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(self):
            from mastapy.gears.materials import _587
            
            return self._parent._cast(_587.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(self):
            from mastapy.gears.materials import _589
            
            return self._parent._cast(_589.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(self):
            from mastapy.gears.materials import _590
            
            return self._parent._cast(_590.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(self):
            from mastapy.gears.materials import _592
            
            return self._parent._cast(_592.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(self):
            from mastapy.gears.materials import _596
            
            return self._parent._cast(_596.ISOTR1417912001CoefficientOfFrictionConstantsDatabase)

        @property
        def klingelnberg_conical_gear_material_database(self):
            from mastapy.gears.materials import _597
            
            return self._parent._cast(_597.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(self):
            from mastapy.gears.materials import _604
            
            return self._parent._cast(_604.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(self):
            from mastapy.gears.manufacturing.cylindrical import _607
            
            return self._parent._cast(_607.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(self):
            from mastapy.gears.manufacturing.cylindrical import _612
            
            return self._parent._cast(_612.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(self):
            from mastapy.gears.manufacturing.cylindrical import _623
            
            return self._parent._cast(_623.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _702
            
            return self._parent._cast(_702.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _708
            
            return self._parent._cast(_708.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _714
            
            return self._parent._cast(_714.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(self):
            from mastapy.gears.manufacturing.bevel import _797
            
            return self._parent._cast(_797.ManufacturingMachineDatabase)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _917
            
            return self._parent._cast(_917.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _918
            
            return self._parent._cast(_918.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase)

        @property
        def pareto_conical_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _920
            
            return self._parent._cast(_920.ParetoConicalRatingOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _921
            
            return self._parent._cast(_921.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _922
            
            return self._parent._cast(_922.ParetoCylindricalGearSetOptimisationStrategyDatabase)

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _923
            
            return self._parent._cast(_923.ParetoCylindricalRatingOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _924
            
            return self._parent._cast(_924.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_face_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _925
            
            return self._parent._cast(_925.ParetoFaceGearSetOptimisationStrategyDatabase)

        @property
        def pareto_face_rating_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _926
            
            return self._parent._cast(_926.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _927
            
            return self._parent._cast(_927.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _928
            
            return self._parent._cast(_928.ParetoHypoidGearSetOptimisationStrategyDatabase)

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _930
            
            return self._parent._cast(_930.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _931
            
            return self._parent._cast(_931.ParetoSpiralBevelGearSetOptimisationStrategyDatabase)

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _932
            
            return self._parent._cast(_932.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase)

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(self):
            from mastapy.gears.gear_set_pareto_optimiser import _933
            
            return self._parent._cast(_933.ParetoStraightBevelGearSetOptimisationStrategyDatabase)

        @property
        def bevel_hypoid_gear_design_settings_database(self):
            from mastapy.gears.gear_designs import _937
            
            return self._parent._cast(_937.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(self):
            from mastapy.gears.gear_designs import _939
            
            return self._parent._cast(_939.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(self):
            from mastapy.gears.gear_designs.cylindrical import _1012
            
            return self._parent._cast(_1012.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(self):
            from mastapy.gears.gear_designs.cylindrical import _1018
            
            return self._parent._cast(_1018.CylindricalGearMicroGeometrySettingsDatabase)

        @property
        def magnet_material_database(self):
            from mastapy.electric_machines import _1276
            
            return self._parent._cast(_1276.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(self):
            from mastapy.electric_machines import _1294
            
            return self._parent._cast(_1294.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(self):
            from mastapy.electric_machines import _1306
            
            return self._parent._cast(_1306.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(self):
            from mastapy.cycloidal import _1447
            
            return self._parent._cast(_1447.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(self):
            from mastapy.cycloidal import _1454
            
            return self._parent._cast(_1454.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(self):
            from mastapy.bolts import _1457
            
            return self._parent._cast(_1457.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(self):
            from mastapy.bolts import _1459
            
            return self._parent._cast(_1459.BoltGeometryDatabase)

        @property
        def bolt_material_database(self):
            from mastapy.bolts import _1461
            
            return self._parent._cast(_1461.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(self):
            from mastapy.bolts import _1466
            
            return self._parent._cast(_1466.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1530
            
            return self._parent._cast(_1530.DesignSpaceSearchStrategyDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(self):
            from mastapy.math_utility.optimisation import _1532
            
            return self._parent._cast(_1532.MicroGeometryDesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(self):
            from mastapy.math_utility.optimisation import _1543
            
            return self._parent._cast(_1543.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(self):
            from mastapy.utility.databases import _1817
            
            return self._parent._cast(_1817.NamedDatabase)

        @property
        def sql_database(self):
            from mastapy.utility.databases import _1820
            
            return self._parent._cast(_1820.SQLDatabase)

        @property
        def bearing_settings_database(self):
            from mastapy.bearings import _1867
            
            return self._parent._cast(_1867.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(self):
            from mastapy.bearings import _1880
            
            return self._parent._cast(_1880.RollingBearingDatabase)

        @property
        def iso14179_settings_database(self):
            from mastapy.bearings.bearing_results.rolling import _1962
            
            return self._parent._cast(_1962.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(self):
            from mastapy.system_model.optimization import _2215
            
            return self._parent._cast(_2215.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(self):
            from mastapy.system_model.optimization import _2224
            
            return self._parent._cast(_2224.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2546
            
            return self._parent._cast(_2546.SuperchargerRotorSetDatabase)

        @property
        def database(self) -> 'Database':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Database.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def count(self) -> 'int':
        """int: 'Count' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    def can_be_removed(self, item: 'TValue') -> 'bool':
        """ 'CanBeRemoved' is the original name of this method.

        Args:
            item (TValue)

        Returns:
            bool
        """

        method_result = self.wrapped.CanBeRemoved(item)
        return method_result

    def get_all_items(self) -> 'List[TValue]':
        """ 'GetAllItems' is the original name of this method.

        Returns:
            List[TValue]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetAllItems())

    @property
    def cast_to(self) -> 'Database._Cast_Database':
        return self._Cast_Database(self)
