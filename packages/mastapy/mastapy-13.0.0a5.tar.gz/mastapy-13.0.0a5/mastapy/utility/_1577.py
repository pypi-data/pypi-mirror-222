"""_1577.py

IndependentReportablePropertiesBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import('SMT.MastaAPI.Utility', 'IndependentReportablePropertiesBase')


__docformat__ = 'restructuredtext en'
__all__ = ('IndependentReportablePropertiesBase',)


T = TypeVar('T', bound='IndependentReportablePropertiesBase')


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(self, parent: 'IndependentReportablePropertiesBase'):
            self._parent = parent

        @property
        def oil_pump_detail(self):
            from mastapy.materials.efficiency import _296
            
            return self._parent._cast(_296.OilPumpDetail)

        @property
        def packaging_limits(self):
            from mastapy.geometry import _307
            
            return self._parent._cast(_307.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(self):
            from mastapy.gears import _344
            
            return self._parent._cast(_344.SpecificationForTheEffectOfOilKinematicViscosity)

        @property
        def cylindrical_gear_micro_geometry_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1017
            
            return self._parent._cast(_1017.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(self):
            from mastapy.gears.gear_designs.cylindrical import _1047
            
            return self._parent._cast(_1047.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1055
            
            return self._parent._cast(_1055.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1056
            
            return self._parent._cast(_1056.LTCASettings)

        @property
        def micropitting(self):
            from mastapy.gears.gear_designs.cylindrical import _1059
            
            return self._parent._cast(_1059.Micropitting)

        @property
        def scuffing(self):
            from mastapy.gears.gear_designs.cylindrical import _1066
            
            return self._parent._cast(_1066.Scuffing)

        @property
        def surface_roughness(self):
            from mastapy.gears.gear_designs.cylindrical import _1074
            
            return self._parent._cast(_1074.SurfaceRoughness)

        @property
        def tiff_analysis_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1076
            
            return self._parent._cast(_1076.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(self):
            from mastapy.gears.gear_designs.cylindrical import _1080
            
            return self._parent._cast(_1080.ToothFlankFractureAnalysisSettings)

        @property
        def usage(self):
            from mastapy.gears.gear_designs.cylindrical import _1084
            
            return self._parent._cast(_1084.Usage)

        @property
        def eccentricity(self):
            from mastapy.electric_machines import _1255
            
            return self._parent._cast(_1255.Eccentricity)

        @property
        def temperatures(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1367
            
            return self._parent._cast(_1367.Temperatures)

        @property
        def lookup_table_base(self):
            from mastapy.math_utility.measured_data import _1557
            
            return self._parent._cast(_1557.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1558
            
            return self._parent._cast(_1558.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(self):
            from mastapy.math_utility.measured_data import _1559
            
            return self._parent._cast(_1559.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(self):
            from mastapy.bearings.tolerances import _1905
            
            return self._parent._cast(_1905.RoundnessSpecification)

        @property
        def equivalent_load_factors(self):
            from mastapy.bearings.bearing_results import _1932
            
            return self._parent._cast(_1932.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(self):
            from mastapy.bearings.bearing_results.rolling import _1963
            
            return self._parent._cast(_1963.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(self):
            from mastapy.bearings.bearing_results.rolling import _2057
            
            return self._parent._cast(_2057.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6778
            
            return self._parent._cast(_6778.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(self) -> 'IndependentReportablePropertiesBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IndependentReportablePropertiesBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase':
        return self._Cast_IndependentReportablePropertiesBase(self)
