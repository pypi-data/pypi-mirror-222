"""_940.py

BevelHypoidGearRatingSettingsItem
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility.databases import _1818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearRatingSettingsItem')

if TYPE_CHECKING:
    from mastapy.gears.materials import _602
    from mastapy.gears.rating.iso_10300 import _418, _433, _426
    from mastapy.gears.rating.hypoid import _439


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettingsItem',)


class BevelHypoidGearRatingSettingsItem(_1818.NamedDatabaseItem):
    """BevelHypoidGearRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM

    class _Cast_BevelHypoidGearRatingSettingsItem:
        """Special nested class for casting BevelHypoidGearRatingSettingsItem to subclasses."""

        def __init__(self, parent: 'BevelHypoidGearRatingSettingsItem'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(self) -> 'BevelHypoidGearRatingSettingsItem':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_rating_method(self) -> '_602.RatingMethods':
        """RatingMethods: 'BevelGearRatingMethod' is the original name of this property."""

        temp = self.wrapped.BevelGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Materials.RatingMethods')
        return constructor.new_from_mastapy('mastapy.gears.materials._602', 'RatingMethods')(value) if value is not None else None

    @bevel_gear_rating_method.setter
    def bevel_gear_rating_method(self, value: '_602.RatingMethods'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Materials.RatingMethods')
        self.wrapped.BevelGearRatingMethod = value

    @property
    def bevel_general_load_factors_k_method(self) -> '_418.GeneralLoadFactorCalculationMethod':
        """GeneralLoadFactorCalculationMethod: 'BevelGeneralLoadFactorsKMethod' is the original name of this property."""

        temp = self.wrapped.BevelGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._418', 'GeneralLoadFactorCalculationMethod')(value) if value is not None else None

    @bevel_general_load_factors_k_method.setter
    def bevel_general_load_factors_k_method(self, value: '_418.GeneralLoadFactorCalculationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod')
        self.wrapped.BevelGeneralLoadFactorsKMethod = value

    @property
    def bevel_pitting_factor_calculation_method(self) -> '_433.PittingFactorCalculationMethod':
        """PittingFactorCalculationMethod: 'BevelPittingFactorCalculationMethod' is the original name of this property."""

        temp = self.wrapped.BevelPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._433', 'PittingFactorCalculationMethod')(value) if value is not None else None

    @bevel_pitting_factor_calculation_method.setter
    def bevel_pitting_factor_calculation_method(self, value: '_433.PittingFactorCalculationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod')
        self.wrapped.BevelPittingFactorCalculationMethod = value

    @property
    def hypoid_gear_rating_method(self) -> '_439.HypoidRatingMethod':
        """HypoidRatingMethod: 'HypoidGearRatingMethod' is the original name of this property."""

        temp = self.wrapped.HypoidGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating.hypoid._439', 'HypoidRatingMethod')(value) if value is not None else None

    @hypoid_gear_rating_method.setter
    def hypoid_gear_rating_method(self, value: '_439.HypoidRatingMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod')
        self.wrapped.HypoidGearRatingMethod = value

    @property
    def hypoid_general_load_factors_k_method(self) -> '_418.GeneralLoadFactorCalculationMethod':
        """GeneralLoadFactorCalculationMethod: 'HypoidGeneralLoadFactorsKMethod' is the original name of this property."""

        temp = self.wrapped.HypoidGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._418', 'GeneralLoadFactorCalculationMethod')(value) if value is not None else None

    @hypoid_general_load_factors_k_method.setter
    def hypoid_general_load_factors_k_method(self, value: '_418.GeneralLoadFactorCalculationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod')
        self.wrapped.HypoidGeneralLoadFactorsKMethod = value

    @property
    def hypoid_pitting_factor_calculation_method(self) -> '_433.PittingFactorCalculationMethod':
        """PittingFactorCalculationMethod: 'HypoidPittingFactorCalculationMethod' is the original name of this property."""

        temp = self.wrapped.HypoidPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._433', 'PittingFactorCalculationMethod')(value) if value is not None else None

    @hypoid_pitting_factor_calculation_method.setter
    def hypoid_pitting_factor_calculation_method(self, value: '_433.PittingFactorCalculationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod')
        self.wrapped.HypoidPittingFactorCalculationMethod = value

    @property
    def iso_rating_method_for_bevel_gears(self) -> '_426.ISO10300RatingMethod':
        """ISO10300RatingMethod: 'ISORatingMethodForBevelGears' is the original name of this property."""

        temp = self.wrapped.ISORatingMethodForBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._426', 'ISO10300RatingMethod')(value) if value is not None else None

    @iso_rating_method_for_bevel_gears.setter
    def iso_rating_method_for_bevel_gears(self, value: '_426.ISO10300RatingMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod')
        self.wrapped.ISORatingMethodForBevelGears = value

    @property
    def iso_rating_method_for_hypoid_gears(self) -> '_426.ISO10300RatingMethod':
        """ISO10300RatingMethod: 'ISORatingMethodForHypoidGears' is the original name of this property."""

        temp = self.wrapped.ISORatingMethodForHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod')
        return constructor.new_from_mastapy('mastapy.gears.rating._426', 'ISO10300RatingMethod')(value) if value is not None else None

    @iso_rating_method_for_hypoid_gears.setter
    def iso_rating_method_for_hypoid_gears(self, value: '_426.ISO10300RatingMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod')
        self.wrapped.ISORatingMethodForHypoidGears = value

    @property
    def include_mesh_node_misalignments_in_default_report(self) -> 'bool':
        """bool: 'IncludeMeshNodeMisalignmentsInDefaultReport' is the original name of this property."""

        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @include_mesh_node_misalignments_in_default_report.setter
    def include_mesh_node_misalignments_in_default_report(self, value: 'bool'):
        self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem':
        return self._Cast_BevelHypoidGearRatingSettingsItem(self)
