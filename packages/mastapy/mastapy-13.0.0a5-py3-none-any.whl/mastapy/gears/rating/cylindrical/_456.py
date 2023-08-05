"""_456.py

CylindricalGearMeshRating
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearMeshRating')

if TYPE_CHECKING:
    from mastapy.gears import _321, _339
    from mastapy.utility_gui.charts import _1854
    from mastapy.gears.rating.cylindrical.agma import _532
    from mastapy.gears.gear_designs.cylindrical import _1015
    from mastapy.gears.rating.cylindrical import _465, _462, _458
    from mastapy.gears.rating.cylindrical.iso6336 import _517
    from mastapy.gears.load_case.cylindrical import _881
    from mastapy.gears.rating.cylindrical.vdi import _486


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshRating',)


class CylindricalGearMeshRating(_358.GearMeshRating):
    """CylindricalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_RATING

    class _Cast_CylindricalGearMeshRating:
        """Special nested class for casting CylindricalGearMeshRating to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshRating'):
            self._parent = parent

        @property
        def gear_mesh_rating(self):
            return self._parent._cast(_358.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_rating(self) -> 'CylindricalGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_321.CylindricalFlanks':
        """CylindricalFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.CylindricalFlanks')
        return constructor.new_from_mastapy('mastapy.gears._321', 'CylindricalFlanks')(value) if value is not None else None

    @property
    def load_intensity(self) -> 'float':
        """float: 'LoadIntensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadIntensity

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor(self) -> 'float':
        """float: 'LoadSharingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor_source(self) -> '_339.PlanetaryRatingLoadSharingOption':
        """PlanetaryRatingLoadSharingOption: 'LoadSharingFactorSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactorSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption')
        return constructor.new_from_mastapy('mastapy.gears._339', 'PlanetaryRatingLoadSharingOption')(value) if value is not None else None

    @property
    def mechanical_advantage(self) -> 'float':
        """float: 'MechanicalAdvantage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalAdvantage

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction(self) -> 'float':
        """float: 'MeshCoefficientOfFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_benedict_and_kelley(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionBenedictAndKelley' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_drozdov_and_gavrikov(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionDrozdovAndGavrikov' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionDrozdovAndGavrikov

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotc60(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionISOTC60' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionISOTC60

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionISOTR1417912001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417912001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001_with_surface_roughness_parameter(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001_martins_et_al(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionISOTR1417922001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_misharin(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionMisharin' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionMisharin

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_o_donoghue_and_cameron(self) -> 'float':
        """float: 'MeshCoefficientOfFrictionODonoghueAndCameron' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionODonoghueAndCameron

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_at_diameter_benedict_and_kelley(self) -> '_1854.TwoDChartDefinition':
        """TwoDChartDefinition: 'MeshCoefficientOfFrictionAtDiameterBenedictAndKelley' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshCoefficientOfFrictionAtDiameterBenedictAndKelley

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def sliding_ratio_at_end_of_recess(self) -> 'float':
        """float: 'SlidingRatioAtEndOfRecess' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingRatioAtEndOfRecess

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_ratio_at_start_of_approach(self) -> 'float':
        """float: 'SlidingRatioAtStartOfApproach' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingRatioAtStartOfApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_loss_factor(self) -> 'float':
        """float: 'ToothLossFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def agma_cylindrical_mesh_single_flank_rating(self) -> '_532.AGMA2101MeshSingleFlankRating':
        """AGMA2101MeshSingleFlankRating: 'AGMACylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMACylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_mesh(self) -> '_1015.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'CylindricalGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_mesh_single_flank_rating(self) -> '_465.CylindricalMeshSingleFlankRating':
        """CylindricalMeshSingleFlankRating: 'CylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_rating(self) -> '_462.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'GearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isodin_cylindrical_mesh_single_flank_rating(self) -> '_517.ISO6336AbstractMetalMeshSingleFlankRating':
        """ISO6336AbstractMetalMeshSingleFlankRating: 'ISODINCylindricalMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISODINCylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_load_case(self) -> '_881.CylindricalMeshLoadCase':
        """CylindricalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_single_flank_rating(self) -> '_465.CylindricalMeshSingleFlankRating':
        """CylindricalMeshSingleFlankRating: 'MeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def vdi_cylindrical_gear_single_flank_rating(self) -> '_486.VDI2737InternalGearSingleFlankRating':
        """VDI2737InternalGearSingleFlankRating: 'VDICylindricalGearSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VDICylindricalGearSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_ratings(self) -> 'List[_458.CylindricalGearRating]':
        """List[CylindricalGearRating]: 'CylindricalGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearMeshRating._Cast_CylindricalGearMeshRating':
        return self._Cast_CylindricalGearMeshRating(self)
