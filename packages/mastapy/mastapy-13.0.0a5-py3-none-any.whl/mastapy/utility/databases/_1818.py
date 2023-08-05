"""_1818.py

NamedDatabaseItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import('SMT.MastaAPI.Utility.Databases', 'NamedDatabaseItem')

if TYPE_CHECKING:
    from mastapy.utility import _1573
    from mastapy.utility.databases import _1819


__docformat__ = 'restructuredtext en'
__all__ = ('NamedDatabaseItem',)


class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE = _NAMED_DATABASE_ITEM

    class _Cast_NamedDatabaseItem:
        """Special nested class for casting NamedDatabaseItem to subclasses."""

        def __init__(self, parent: 'NamedDatabaseItem'):
            self._parent = parent

        @property
        def shaft_material(self):
            from mastapy.shafts import _24
            
            return self._parent._cast(_24.ShaftMaterial)

        @property
        def shaft_settings_item(self):
            from mastapy.shafts import _40
            
            return self._parent._cast(_40.ShaftSettingsItem)

        @property
        def simple_shaft_definition(self):
            from mastapy.shafts import _43
            
            return self._parent._cast(_43.SimpleShaftDefinition)

        @property
        def analysis_settings_item(self):
            from mastapy.nodal_analysis import _50
            
            return self._parent._cast(_50.AnalysisSettingsItem)

        @property
        def bearing_material(self):
            from mastapy.materials import _243
            
            return self._parent._cast(_243.BearingMaterial)

        @property
        def lubrication_detail(self):
            from mastapy.materials import _265
            
            return self._parent._cast(_265.LubricationDetail)

        @property
        def material(self):
            from mastapy.materials import _267
            
            return self._parent._cast(_267.Material)

        @property
        def materials_settings_item(self):
            from mastapy.materials import _271
            
            return self._parent._cast(_271.MaterialsSettingsItem)

        @property
        def pocketing_power_loss_coefficients(self):
            from mastapy.gears import _340
            
            return self._parent._cast(_340.PocketingPowerLossCoefficients)

        @property
        def cylindrical_gear_design_and_rating_settings_item(self):
            from mastapy.gears.rating.cylindrical import _452
            
            return self._parent._cast(_452.CylindricalGearDesignAndRatingSettingsItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(self):
            from mastapy.gears.rating.cylindrical import _468
            
            return self._parent._cast(_468.CylindricalPlasticGearRatingSettingsItem)

        @property
        def agma_cylindrical_gear_material(self):
            from mastapy.gears.materials import _580
            
            return self._parent._cast(_580.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(self):
            from mastapy.gears.materials import _582
            
            return self._parent._cast(_582.BevelGearISOMaterial)

        @property
        def bevel_gear_material(self):
            from mastapy.gears.materials import _584
            
            return self._parent._cast(_584.BevelGearMaterial)

        @property
        def cylindrical_gear_material(self):
            from mastapy.gears.materials import _588
            
            return self._parent._cast(_588.CylindricalGearMaterial)

        @property
        def gear_material(self):
            from mastapy.gears.materials import _591
            
            return self._parent._cast(_591.GearMaterial)

        @property
        def iso_cylindrical_gear_material(self):
            from mastapy.gears.materials import _594
            
            return self._parent._cast(_594.ISOCylindricalGearMaterial)

        @property
        def isotr1417912001_coefficient_of_friction_constants(self):
            from mastapy.gears.materials import _595
            
            return self._parent._cast(_595.ISOTR1417912001CoefficientOfFrictionConstants)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(self):
            from mastapy.gears.materials import _598
            
            return self._parent._cast(_598.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(self):
            from mastapy.gears.materials import _600
            
            return self._parent._cast(_600.PlasticCylindricalGearMaterial)

        @property
        def raw_material(self):
            from mastapy.gears.materials import _603
            
            return self._parent._cast(_603.RawMaterial)

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearAbstractCutterDesign)

        @property
        def cylindrical_gear_form_grinding_wheel(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704
            
            return self._parent._cast(_704.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705
            
            return self._parent._cast(_705.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _706
            
            return self._parent._cast(_706.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _707
            
            return self._parent._cast(_707.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709
            
            return self._parent._cast(_709.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _711
            
            return self._parent._cast(_711.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _712
            
            return self._parent._cast(_712.CylindricalGearShaver)

        @property
        def involute_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _715
            
            return self._parent._cast(_715.InvoluteCutterDesign)

        @property
        def manufacturing_machine(self):
            from mastapy.gears.manufacturing.bevel import _796
            
            return self._parent._cast(_796.ManufacturingMachine)

        @property
        def bevel_hypoid_gear_design_settings_item(self):
            from mastapy.gears.gear_designs import _938
            
            return self._parent._cast(_938.BevelHypoidGearDesignSettingsItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(self):
            from mastapy.gears.gear_designs import _940
            
            return self._parent._cast(_940.BevelHypoidGearRatingSettingsItem)

        @property
        def design_constraints_collection(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.DesignConstraintsCollection)

        @property
        def cylindrical_gear_design_constraints(self):
            from mastapy.gears.gear_designs.cylindrical import _1011
            
            return self._parent._cast(_1011.CylindricalGearDesignConstraints)

        @property
        def cylindrical_gear_micro_geometry_settings_item(self):
            from mastapy.gears.gear_designs.cylindrical import _1019
            
            return self._parent._cast(_1019.CylindricalGearMicroGeometrySettingsItem)

        @property
        def magnet_material(self):
            from mastapy.electric_machines import _1275
            
            return self._parent._cast(_1275.MagnetMaterial)

        @property
        def stator_rotor_material(self):
            from mastapy.electric_machines import _1293
            
            return self._parent._cast(_1293.StatorRotorMaterial)

        @property
        def winding_material(self):
            from mastapy.electric_machines import _1305
            
            return self._parent._cast(_1305.WindingMaterial)

        @property
        def spline_material(self):
            from mastapy.detailed_rigid_connectors.splines import _1406
            
            return self._parent._cast(_1406.SplineMaterial)

        @property
        def cycloidal_disc_material(self):
            from mastapy.cycloidal import _1446
            
            return self._parent._cast(_1446.CycloidalDiscMaterial)

        @property
        def ring_pins_material(self):
            from mastapy.cycloidal import _1453
            
            return self._parent._cast(_1453.RingPinsMaterial)

        @property
        def bolted_joint_material(self):
            from mastapy.bolts import _1456
            
            return self._parent._cast(_1456.BoltedJointMaterial)

        @property
        def bolt_geometry(self):
            from mastapy.bolts import _1458
            
            return self._parent._cast(_1458.BoltGeometry)

        @property
        def bolt_material(self):
            from mastapy.bolts import _1460
            
            return self._parent._cast(_1460.BoltMaterial)

        @property
        def pareto_optimisation_strategy(self):
            from mastapy.math_utility.optimisation import _1540
            
            return self._parent._cast(_1540.ParetoOptimisationStrategy)

        @property
        def bearing_settings_item(self):
            from mastapy.bearings import _1868
            
            return self._parent._cast(_1868.BearingSettingsItem)

        @property
        def iso14179_settings(self):
            from mastapy.bearings.bearing_results.rolling import _1961
            
            return self._parent._cast(_1961.ISO14179Settings)

        @property
        def conical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2213
            
            return self._parent._cast(_2213.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(self):
            from mastapy.system_model.optimization import _2216
            
            return self._parent._cast(_2216.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(self):
            from mastapy.system_model.optimization import _2222
            
            return self._parent._cast(_2222.OptimizationStrategy)

        @property
        def optimization_strategy_base(self):
            from mastapy.system_model.optimization import _2223
            
            return self._parent._cast(_2223.OptimizationStrategyBase)

        @property
        def supercharger_rotor_set(self):
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2545
            
            return self._parent._cast(_2545.SuperchargerRotorSet)

        @property
        def named_database_item(self) -> 'NamedDatabaseItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedDatabaseItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value is not None else ''

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def no_history(self) -> 'str':
        """str: 'NoHistory' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NoHistory

        if temp is None:
            return ''

        return temp

    @property
    def history(self) -> '_1573.FileHistory':
        """FileHistory: 'History' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def database_key(self) -> '_1819.NamedKey':
        """NamedKey: 'DatabaseKey' is the original name of this property."""

        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @database_key.setter
    def database_key(self, value: '_1819.NamedKey'):
        self.wrapped.DatabaseKey = value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'NamedDatabaseItem._Cast_NamedDatabaseItem':
        return self._Cast_NamedDatabaseItem(self)
