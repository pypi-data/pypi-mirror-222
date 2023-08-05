"""_2187.py

Design
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, Optional, TypeVar
)
from os import path

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.class_property import classproperty
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy._math.vector_3d import Vector3D
from mastapy.utility import _1572
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_STRING = python_net_import('System', 'String')
_BOOLEAN = python_net_import('System', 'Boolean')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_DESIGN = python_net_import('SMT.MastaAPI.SystemModel', 'Design')

if TYPE_CHECKING:
    from mastapy.system_model_gui import _1834
    from mastapy.gears import _320, _326
    from mastapy.materials.efficiency import _290
    from mastapy.system_model.part_model import (
        _2455, _2458, _2461, _2457,
        _2451, _2416, _2417, _2418,
        _2419, _2422, _2425, _2426,
        _2427, _2430, _2431, _2435,
        _2436, _2437, _2438, _2445,
        _2446, _2447, _2449, _2452,
        _2454, _2459, _2460, _2462
    )
    from mastapy.system_model import (
        _2210, _2211, _2195, _2192,
        _2209, _2199
    )
    from mastapy.detailed_rigid_connectors.splines import _1381
    from mastapy.system_model.fe import _2344
    from mastapy.utility import _1573, _1574
    from mastapy.gears.materials import _595
    from mastapy.system_model.part_model.gears import (
        _2494, _2515, _2495, _2496,
        _2497, _2498, _2499, _2500,
        _2501, _2502, _2503, _2504,
        _2505, _2506, _2507, _2508,
        _2509, _2510, _2511, _2512,
        _2514, _2516, _2517, _2518,
        _2519, _2520, _2521, _2522,
        _2523, _2524, _2525, _2526,
        _2527, _2528, _2529, _2530,
        _2531, _2532, _2533, _2534,
        _2535, _2536
    )
    from mastapy.shafts import _35
    from mastapy.system_model.part_model.configurations import _2597, _2594, _2596
    from mastapy.bearings.bearing_results.rolling import _1963
    from mastapy.system_model.database_access import _2247
    from mastapy.system_model.analyses_and_results.load_case_groups import _5636, _5637, _5644
    from mastapy.system_model.analyses_and_results.static_loads import _6772, _6771
    from mastapy.utility.model_validation import _1784
    from mastapy.system_model.analyses_and_results.synchroniser_analysis import _2964
    from mastapy.system_model.part_model.creation_options import (
        _2553, _2554, _2555, _2556,
        _2557
    )
    from mastapy.gears.gear_designs.creation_options import _1142, _1144, _1145
    from mastapy.nodal_analysis import _79
    from mastapy.bearings.bearing_designs.rolling import _2152
    from mastapy import _7525
    from mastapy.system_model.part_model.shaft_model import _2465
    from mastapy.system_model.part_model.cycloidal import _2550, _2551, _2552
    from mastapy.system_model.part_model.couplings import (
        _2558, _2560, _2561, _2563,
        _2564, _2565, _2566, _2568,
        _2569, _2570, _2571, _2572,
        _2578, _2579, _2580, _2582,
        _2583, _2584, _2586, _2587,
        _2588, _2589, _2590, _2592
    )


__docformat__ = 'restructuredtext en'
__all__ = ('Design',)


class Design(_0.APIBase):
    """Design

    This is a mastapy class.
    """

    TYPE = _DESIGN

    class _Cast_Design:
        """Special nested class for casting Design to subclasses."""

        def __init__(self, parent: 'Design'):
            self._parent = parent

        @property
        def design(self) -> 'Design':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Design.TYPE' = None):
        super().__init__(instance_to_wrap if instance_to_wrap else Design.TYPE())
        self._freeze()

    @classproperty
    def available_examples(cls) -> 'List[str]':
        """List[str]: 'AvailableExamples' is the original name of this property."""

        temp = Design.TYPE.AvailableExamples

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def masta_gui(self) -> '_1834.MASTAGUI':
        """MASTAGUI: 'MastaGUI' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MastaGUI

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def axial_contact_ratio_requirement(self) -> '_320.ContactRatioRequirements':
        """ContactRatioRequirements: 'AxialContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.ContactRatioRequirements')
        return constructor.new_from_mastapy('mastapy.gears._320', 'ContactRatioRequirements')(value) if value is not None else None

    @axial_contact_ratio_requirement.setter
    def axial_contact_ratio_requirement(self, value: '_320.ContactRatioRequirements'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.ContactRatioRequirements')
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def bearing_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'BearingConfiguration' is the original name of this property."""

        temp = self.wrapped.BearingConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @bearing_configuration.setter
    def bearing_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.BearingConfiguration = value

    @property
    def coefficient_of_friction(self) -> 'float':
        """float: 'CoefficientOfFriction' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'float'):
        self.wrapped.CoefficientOfFriction = float(value) if value is not None else 0.0

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
    def default_save_location_path(self) -> 'str':
        """str: 'DefaultSaveLocationPath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DefaultSaveLocationPath

        if temp is None:
            return ''

        return temp

    @property
    def design_name(self) -> 'str':
        """str: 'DesignName' is the original name of this property."""

        temp = self.wrapped.DesignName

        if temp is None:
            return ''

        return temp

    @design_name.setter
    def design_name(self, value: 'str'):
        self.wrapped.DesignName = str(value) if value is not None else ''

    @property
    def efficiency_rating_method_for_bearings(self) -> '_290.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodForBearings' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethodForBearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Materials.Efficiency.BearingEfficiencyRatingMethod')
        return constructor.new_from_mastapy('mastapy.materials.efficiency._290', 'BearingEfficiencyRatingMethod')(value) if value is not None else None

    @efficiency_rating_method_for_bearings.setter
    def efficiency_rating_method_for_bearings(self, value: '_290.BearingEfficiencyRatingMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Materials.Efficiency.BearingEfficiencyRatingMethod')
        self.wrapped.EfficiencyRatingMethodForBearings = value

    @property
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod':
        """enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @efficiency_rating_method_if_skf_loss_model_does_not_provide_losses.setter
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses = value

    @property
    def fe_substructure_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'FESubstructureConfiguration' is the original name of this property."""

        temp = self.wrapped.FESubstructureConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @fe_substructure_configuration.setter
    def fe_substructure_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.FESubstructureConfiguration = value

    @property
    def file_name(self) -> 'str':
        """str: 'FileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileName

        if temp is None:
            return ''

        return temp

    @property
    def gear_set_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'GearSetConfiguration' is the original name of this property."""

        temp = self.wrapped.GearSetConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @gear_set_configuration.setter
    def gear_set_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.GearSetConfiguration = value

    @property
    def gravity_magnitude(self) -> 'float':
        """float: 'GravityMagnitude' is the original name of this property."""

        temp = self.wrapped.GravityMagnitude

        if temp is None:
            return 0.0

        return temp

    @gravity_magnitude.setter
    def gravity_magnitude(self, value: 'float'):
        self.wrapped.GravityMagnitude = float(value) if value is not None else 0.0

    @property
    def housing_material_for_grounded_connections(self) -> 'str':
        """str: 'HousingMaterialForGroundedConnections' is the original name of this property."""

        temp = self.wrapped.HousingMaterialForGroundedConnections.SelectedItemName

        if temp is None:
            return ''

        return temp

    @housing_material_for_grounded_connections.setter
    def housing_material_for_grounded_connections(self, value: 'str'):
        self.wrapped.HousingMaterialForGroundedConnections.SetSelectedItem(str(value) if value is not None else '')

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self) -> 'str':
        """str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase' is the original name of this property."""

        temp = self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SetSelectedItem(str(value) if value is not None else '')

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self) -> 'str':
        """str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase' is the original name of this property."""

        temp = self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SetSelectedItem(str(value) if value is not None else '')

    @property
    def input_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'InputPowerLoad' is the original name of this property."""

        temp = self.wrapped.InputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_PowerLoad')(temp) if temp is not None else None

    @input_power_load.setter
    def input_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.InputPowerLoad = value

    @property
    def manufacturer(self) -> 'str':
        """str: 'Manufacturer' is the original name of this property."""

        temp = self.wrapped.Manufacturer

        if temp is None:
            return ''

        return temp

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value is not None else ''

    @property
    def maximum_acceptable_axial_contact_ratio(self) -> 'float':
        """float: 'MaximumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_axial_contact_ratio.setter
    def maximum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatio = float(value) if value is not None else 0.0

    @property
    def maximum_acceptable_axial_contact_ratio_above_integer(self) -> 'float':
        """float: 'MaximumAcceptableAxialContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_axial_contact_ratio_above_integer.setter
    def maximum_acceptable_axial_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger = float(value) if value is not None else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio(self) -> 'float':
        """float: 'MaximumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_transverse_contact_ratio.setter
    def maximum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatio = float(value) if value is not None else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio_above_integer(self) -> 'float':
        """float: 'MaximumAcceptableTransverseContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_transverse_contact_ratio_above_integer.setter
    def maximum_acceptable_transverse_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger = float(value) if value is not None else 0.0

    @property
    def maximum_number_of_teeth(self) -> 'Optional[int]':
        """Optional[int]: 'MaximumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTeeth

        if temp is None:
            return None

        return temp

    @maximum_number_of_teeth.setter
    def maximum_number_of_teeth(self, value: 'Optional[int]'):
        self.wrapped.MaximumNumberOfTeeth = value

    @property
    def minimum_acceptable_axial_contact_ratio(self) -> 'float':
        """float: 'MinimumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_axial_contact_ratio.setter
    def minimum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatio = float(value) if value is not None else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio_below_integer(self) -> 'float':
        """float: 'MinimumAcceptableAxialContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_axial_contact_ratio_below_integer.setter
    def minimum_acceptable_axial_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger = float(value) if value is not None else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_transverse_contact_ratio.setter
    def minimum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatio = float(value) if value is not None else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio_below_integer(self) -> 'float':
        """float: 'MinimumAcceptableTransverseContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_transverse_contact_ratio_below_integer.setter
    def minimum_acceptable_transverse_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger = float(value) if value is not None else 0.0

    @property
    def minimum_number_of_teeth(self) -> 'Optional[int]':
        """Optional[int]: 'MinimumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfTeeth

        if temp is None:
            return None

        return temp

    @minimum_number_of_teeth.setter
    def minimum_number_of_teeth(self, value: 'Optional[int]'):
        self.wrapped.MinimumNumberOfTeeth = value

    @property
    def node_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeSize' is the original name of this property."""

        temp = self.wrapped.NodeSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @node_size.setter
    def node_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeSize = value

    @property
    def number_of_gear_set_configurations(self) -> 'int':
        """int: 'NumberOfGearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfGearSetConfigurations

        if temp is None:
            return 0

        return temp

    @property
    def output_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'OutputPowerLoad' is the original name of this property."""

        temp = self.wrapped.OutputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_PowerLoad')(temp) if temp is not None else None

    @output_power_load.setter
    def output_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.OutputPowerLoad = value

    @property
    def save_external_fe_files_in_the_default_subfolder(self) -> 'bool':
        """bool: 'SaveExternalFEFilesInTheDefaultSubfolder' is the original name of this property."""

        temp = self.wrapped.SaveExternalFEFilesInTheDefaultSubfolder

        if temp is None:
            return False

        return temp

    @save_external_fe_files_in_the_default_subfolder.setter
    def save_external_fe_files_in_the_default_subfolder(self, value: 'bool'):
        self.wrapped.SaveExternalFEFilesInTheDefaultSubfolder = bool(value) if value is not None else False

    @property
    def shaft_detail_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ShaftDetailConfiguration' is the original name of this property."""

        temp = self.wrapped.ShaftDetailConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_str')(temp) if temp is not None else ''

    @shaft_detail_configuration.setter
    def shaft_detail_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ShaftDetailConfiguration = value

    @property
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing':
        """enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing: 'ShaftDiameterModificationDueToRollingBearingRings' is the original name of this property."""

        temp = self.wrapped.ShaftDiameterModificationDueToRollingBearingRings

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @shaft_diameter_modification_due_to_rolling_bearing_rings.setter
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftDiameterModificationDueToRollingBearingRings = value

    @property
    def thermal_expansion_for_grounded_nodes(self) -> '_2210.ThermalExpansionOptionForGroundedNodes':
        """ThermalExpansionOptionForGroundedNodes: 'ThermalExpansionForGroundedNodes' is the original name of this property."""

        temp = self.wrapped.ThermalExpansionForGroundedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.ThermalExpansionOptionForGroundedNodes')
        return constructor.new_from_mastapy('mastapy.system_model._2210', 'ThermalExpansionOptionForGroundedNodes')(value) if value is not None else None

    @thermal_expansion_for_grounded_nodes.setter
    def thermal_expansion_for_grounded_nodes(self, value: '_2210.ThermalExpansionOptionForGroundedNodes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.ThermalExpansionOptionForGroundedNodes')
        self.wrapped.ThermalExpansionForGroundedNodes = value

    @property
    def transverse_contact_ratio_requirement(self) -> '_320.ContactRatioRequirements':
        """ContactRatioRequirements: 'TransverseContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.ContactRatioRequirements')
        return constructor.new_from_mastapy('mastapy.gears._320', 'ContactRatioRequirements')(value) if value is not None else None

    @transverse_contact_ratio_requirement.setter
    def transverse_contact_ratio_requirement(self, value: '_320.ContactRatioRequirements'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.ContactRatioRequirements')
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def unbalanced_mass_inclusion(self) -> '_2461.UnbalancedMassInclusionOption':
        """UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property."""

        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.PartModel.UnbalancedMassInclusionOption')
        return constructor.new_from_mastapy('mastapy.system_model.part_model._2461', 'UnbalancedMassInclusionOption')(value) if value is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: '_2461.UnbalancedMassInclusionOption'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.PartModel.UnbalancedMassInclusionOption')
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self) -> 'bool':
        """bool: 'UseElementContactAnglesForAngularVelocitiesInBallBearings' is the original name of this property."""

        temp = self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings

        if temp is None:
            return False

        return temp

    @use_element_contact_angles_for_angular_velocities_in_ball_bearings.setter
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self, value: 'bool'):
        self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings = bool(value) if value is not None else False

    @property
    def use_expanded_2d_projection_mode(self) -> 'bool':
        """bool: 'UseExpanded2DProjectionMode' is the original name of this property."""

        temp = self.wrapped.UseExpanded2DProjectionMode

        if temp is None:
            return False

        return temp

    @use_expanded_2d_projection_mode.setter
    def use_expanded_2d_projection_mode(self, value: 'bool'):
        self.wrapped.UseExpanded2DProjectionMode = bool(value) if value is not None else False

    @property
    def volumetric_oil_air_mixture_ratio(self) -> 'float':
        """float: 'VolumetricOilAirMixtureRatio' is the original name of this property."""

        temp = self.wrapped.VolumetricOilAirMixtureRatio

        if temp is None:
            return 0.0

        return temp

    @volumetric_oil_air_mixture_ratio.setter
    def volumetric_oil_air_mixture_ratio(self, value: 'float'):
        self.wrapped.VolumetricOilAirMixtureRatio = float(value) if value is not None else 0.0

    @property
    def default_system_temperatures(self) -> '_2211.TransmissionTemperatureSet':
        """TransmissionTemperatureSet: 'DefaultSystemTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DefaultSystemTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detailed_spline_settings(self) -> '_1381.DetailedSplineJointSettings':
        """DetailedSplineJointSettings: 'DetailedSplineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DetailedSplineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_group(self) -> '_2195.ElectricMachineGroup':
        """ElectricMachineGroup: 'ElectricMachineGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fe_batch_operations(self) -> '_2344.BatchOperations':
        """BatchOperations: 'FEBatchOperations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEBatchOperations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file_save_details_all(self) -> '_1573.FileHistory':
        """FileHistory: 'FileSaveDetailsAll' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileSaveDetailsAll

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file_save_details_most_recent(self) -> '_1574.FileHistoryItem':
        """FileHistoryItem: 'FileSaveDetailsMostRecent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileSaveDetailsMostRecent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_group(self) -> '_326.GearSetDesignGroup':
        """GearSetDesignGroup: 'GearSetDesignGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gravity_orientation(self) -> 'Vector3D':
        """Vector3D: 'GravityOrientation' is the original name of this property."""

        temp = self.wrapped.GravityOrientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @gravity_orientation.setter
    def gravity_orientation(self, value: 'Vector3D'):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityOrientation = value

    @property
    def gravity_vector_components(self) -> 'Vector3D':
        """Vector3D: 'GravityVectorComponents' is the original name of this property."""

        temp = self.wrapped.GravityVectorComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @gravity_vector_components.setter
    def gravity_vector_components(self, value: 'Vector3D'):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityVectorComponents = value

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_external_external_meshes(self) -> '_595.ISOTR1417912001CoefficientOfFrictionConstants':
        """ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes(self) -> '_595.ISOTR1417912001CoefficientOfFrictionConstants':
        """ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_gear_set_selection_group(self) -> '_2494.ActiveGearSetDesignSelectionGroup':
        """ActiveGearSetDesignSelectionGroup: 'SelectedGearSetSelectionGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedGearSetSelectionGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def settings(self) -> '_2192.DesignSettings':
        """DesignSettings: 'Settings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shafts(self) -> '_35.ShaftSafetyFactorSettings':
        """ShaftSafetyFactorSettings: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system(self) -> '_2209.SystemReporting':
        """SystemReporting: 'System' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.System

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_detail_configurations(self) -> 'List[_2597.BearingDetailConfiguration]':
        """List[BearingDetailConfiguration]: 'BearingDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_substructure_configurations(self) -> 'List[_2594.ActiveFESubstructureSelectionGroup]':
        """List[ActiveFESubstructureSelectionGroup]: 'FESubstructureConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESubstructureConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_configurations(self) -> 'List[_2494.ActiveGearSetDesignSelectionGroup]':
        """List[ActiveGearSetDesignSelectionGroup]: 'GearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def iso14179_settings_per_bearing_type(self) -> 'List[_1963.ISO14179SettingsPerBearingType]':
        """List[ISO14179SettingsPerBearingType]: 'ISO14179SettingsPerBearingType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179SettingsPerBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_detail_configurations(self) -> 'List[_2596.ActiveShaftDesignSelectionGroup]':
        """List[ActiveShaftDesignSelectionGroup]: 'ShaftDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def databases(self) -> '_2247.Databases':
        """Databases: 'Databases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Databases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_states(self) -> 'List[_5636.DesignState]':
        """List[DesignState]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def duty_cycles(self) -> 'List[_5637.DutyCycle]':
        """List[DutyCycle]: 'DutyCycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_config(self) -> '_2515.GearSetConfiguration':
        """GearSetConfiguration: 'GearSetConfig' is the original name of this property."""

        temp = self.wrapped.GearSetConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @gear_set_config.setter
    def gear_set_config(self, value: '_2515.GearSetConfiguration'):
        self.wrapped.GearSetConfig = value

    @property
    def masta_settings(self) -> '_2199.MASTASettings':
        """MASTASettings: 'MastaSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MastaSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly(self) -> '_2457.RootAssembly':
        """RootAssembly: 'RootAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_loads(self) -> 'List[_6772.StaticLoadCase]':
        """List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def status(self) -> '_1784.Status':
        """Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case_groups(self) -> 'List[_5644.TimeSeriesLoadCaseGroup]':
        """List[TimeSeriesLoadCaseGroup]: 'TimeSeriesLoadCaseGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCaseGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_design_state(self, name: Optional['str'] = 'New Design State') -> '_5636.DesignState':
        """ 'AddDesignState' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.AddDesignState(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_duty_cycle(self, name: Optional['str'] = 'New Duty Cycle') -> '_5637.DutyCycle':
        """ 'AddDutyCycle' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        """

        name = str(name)
        method_result = self.wrapped.AddDutyCycle(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser_shift_empty(self) -> '_2964.SynchroniserShift':
        """ 'AddSynchroniserShift' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        """

        method_result = self.wrapped.AddSynchroniserShift()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser_shift(self, name: 'str') -> '_2964.SynchroniserShift':
        """ 'AddSynchroniserShift' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        """

        name = str(name)
        method_result = self.wrapped.AddSynchroniserShift.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def clear_design(self):
        """ 'ClearDesign' is the original name of this method."""

        self.wrapped.ClearDesign()

    def __copy__(self) -> 'Design':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def __deepcopy__(self, memo) -> 'Design':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def copy_with_results(self) -> 'Design':
        """ 'CopyWithResults' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.CopyWithResults()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def design_state_load_case_group_named(self, name: 'str') -> '_5636.DesignState':
        """ 'DesignStateLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.DesignStateLoadCaseGroupNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def design_state_named(self, name: 'str') -> '_5636.DesignState':
        """ 'DesignStateNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.DesignStateNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def dispose(self):
        """ 'Dispose' is the original name of this method."""

        self.wrapped.Dispose()

    def duty_cycle_named(self, name: 'str') -> '_5637.DutyCycle':
        """ 'DutyCycleNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        """

        name = str(name)
        method_result = self.wrapped.DutyCycleNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def load_results(self, file_name: 'str'):
        """ 'LoadResults' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.LoadResults(file_name if file_name else '')

    def new_belt_creation_options(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2553.BeltCreationOptions':
        """ 'NewBeltCreationOptions' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.BeltCreationOptions
        """

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.NewBeltCreationOptions(centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cycloidal_assembly_creation_options(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2554.CycloidalAssemblyCreationOptions':
        """ 'NewCycloidalAssemblyCreationOptions' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions
        """

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.NewCycloidalAssemblyCreationOptions(number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cylindrical_gear_linear_train_creation_options(self, number_of_gears: Optional['int'] = 3, name: Optional['str'] = 'Gear Train') -> '_2555.CylindricalGearLinearTrainCreationOptions':
        """ 'NewCylindricalGearLinearTrainCreationOptions' is the original name of this method.

        Args:
            number_of_gears (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions
        """

        number_of_gears = int(number_of_gears)
        name = str(name)
        method_result = self.wrapped.NewCylindricalGearLinearTrainCreationOptions(number_of_gears if number_of_gears else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cylindrical_gear_pair_creation_options(self) -> '_1142.CylindricalGearPairCreationOptions':
        """ 'NewCylindricalGearPairCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions
        """

        method_result = self.wrapped.NewCylindricalGearPairCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_hypoid_gear_set_creation_options(self) -> '_1144.HypoidGearSetCreationOptions':
        """ 'NewHypoidGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.HypoidGearSetCreationOptions
        """

        method_result = self.wrapped.NewHypoidGearSetCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_nodal_matrix(self, dense_matrix: 'List[List[float]]') -> '_79.NodalMatrix':
        """ 'NewNodalMatrix' is the original name of this method.

        Args:
            dense_matrix (List[List[float]])

        Returns:
            mastapy.nodal_analysis.NodalMatrix
        """

        dense_matrix = conversion.mp_to_pn_list_float_2d(dense_matrix)
        method_result = self.wrapped.NewNodalMatrix(dense_matrix)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_planet_carrier_creation_options(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2556.PlanetCarrierCreationOptions':
        """ 'NewPlanetCarrierCreationOptions' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions
        """

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.NewPlanetCarrierCreationOptions(number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_shaft_creation_options(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2557.ShaftCreationOptions':
        """ 'NewShaftCreationOptions' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.ShaftCreationOptions
        """

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.NewShaftCreationOptions(length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_spiral_bevel_gear_set_creation_options(self) -> '_1145.SpiralBevelGearSetCreationOptions':
        """ 'NewSpiralBevelGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions
        """

        method_result = self.wrapped.NewSpiralBevelGearSetCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_bearing_from_database(self, rolling_bearing: '_2152.RollingBearing'):
        """ 'RemoveBearingFromDatabase' is the original name of this method.

        Args:
            rolling_bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """

        self.wrapped.RemoveBearingFromDatabase(rolling_bearing.wrapped if rolling_bearing else None)

    def remove_synchroniser_shift(self, shift: '_2964.SynchroniserShift'):
        """ 'RemoveSynchroniserShift' is the original name of this method.

        Args:
            shift (mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift)
        """

        self.wrapped.RemoveSynchroniserShift(shift.wrapped if shift else None)

    def save(self, file_name: 'str', save_results: 'bool') -> '_1784.Status':
        """ 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)

        Returns:
            mastapy.utility.model_validation.Status
        """

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN](file_name if file_name else '', save_results if save_results else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def save_with_progress(self, file_name: 'str', save_results: 'bool', progress: '_7525.TaskProgress') -> '_1784.Status':
        """ 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)
            progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.model_validation.Status
        """

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN, _TASK_PROGRESS](file_name if file_name else '', save_results if save_results else False, progress.wrapped if progress else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def save_load_case_results(self, file_name: 'str', load_cases: 'List[_6771.LoadCase]'):
        """ 'SaveLoadCaseResults' is the original name of this method.

        Args:
            file_name (str)
            load_cases (List[mastapy.system_model.analyses_and_results.static_loads.LoadCase])
        """

        file_name = str(file_name)
        load_cases = conversion.mp_to_pn_objects_in_list(load_cases)
        self.wrapped.SaveLoadCaseResults(file_name if file_name else '', load_cases)

    def save_results(self, file_name: 'str'):
        """ 'SaveResults' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.SaveResults(file_name if file_name else '')

    def time_series_load_case_group_named(self, name: 'str') -> '_5644.TimeSeriesLoadCaseGroup':
        """ 'TimeSeriesLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup
        """

        name = str(name)
        method_result = self.wrapped.TimeSeriesLoadCaseGroupNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def all_parts(self) -> 'List[_2451.Part]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_assembly(self) -> 'List[_2416.Assembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2417.AbstractAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2418.AbstractShaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaft')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2419.AbstractShaftOrHousing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bearing(self) -> 'List[_2422.Bearing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bolt(self) -> 'List[_2425.Bolt]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bolted_joint(self) -> 'List[_2426.BoltedJoint]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_component(self) -> 'List[_2427.Component]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_connector(self) -> 'List[_2430.Connector]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_datum(self) -> 'List[_2431.Datum]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_external_cad_model(self) -> 'List[_2435.ExternalCADModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_fe_part(self) -> 'List[_2436.FEPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FEPart')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2437.FlexiblePinAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2438.GuideDxfModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'GuideDxfModel')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_mass_disc(self) -> 'List[_2445.MassDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_measurement_component(self) -> 'List[_2446.MeasurementComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_mountable_component(self) -> 'List[_2447.MountableComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_oil_seal(self) -> 'List[_2449.OilSeal]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_planet_carrier(self) -> 'List[_2452.PlanetCarrier]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_point_load(self) -> 'List[_2454.PointLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_power_load(self) -> 'List[_2455.PowerLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_root_assembly(self) -> 'List[_2457.RootAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2459.SpecialisedAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2460.UnbalancedMass]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_virtual_component(self) -> 'List[_2462.VirtualComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_shaft(self) -> 'List[_2465.Shaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ShaftModel', 'Shaft')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2495.AGMAGleasonConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2496.AGMAGleasonConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2497.BevelDifferentialGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2498.BevelDifferentialGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2499.BevelDifferentialPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2500.BevelDifferentialSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_gear(self) -> 'List[_2501.BevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2502.BevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_gear(self) -> 'List[_2503.ConceptGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2504.ConceptGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_conical_gear(self) -> 'List[_2505.ConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2506.ConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2507.CylindricalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2508.CylindricalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2509.CylindricalPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_face_gear(self) -> 'List[_2510.FaceGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_face_gear_set(self) -> 'List[_2511.FaceGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_gear(self) -> 'List[_2512.Gear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_gear_set(self) -> 'List[_2514.GearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2516.HypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2517.HypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2518.KlingelnbergCycloPalloidConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2519.KlingelnbergCycloPalloidConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2520.KlingelnbergCycloPalloidHypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2521.KlingelnbergCycloPalloidHypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2522.KlingelnbergCycloPalloidSpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2523.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2524.PlanetaryGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2525.SpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2526.SpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2527.StraightBevelDiffGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2528.StraightBevelDiffGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2529.StraightBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2530.StraightBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2531.StraightBevelPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelPlanetGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2532.StraightBevelSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_worm_gear(self) -> 'List[_2533.WormGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2534.WormGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2535.ZerolBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2536.ZerolBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2550.CycloidalAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2551.CycloidalDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'CycloidalDisc')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_ring_pins(self) -> 'List[_2552.RingPins]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'RingPins')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_belt_drive(self) -> 'List[_2558.BeltDrive]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_clutch(self) -> 'List[_2560.Clutch]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Clutch')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_clutch_half(self) -> 'List[_2561.ClutchHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_coupling(self) -> 'List[_2563.ConceptCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2564.ConceptCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_coupling(self) -> 'List[_2565.Coupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_coupling_half(self) -> 'List[_2566.CouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cvt(self) -> 'List[_2568.CVT]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2569.CVTPulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2570.PartToPartShearCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2571.PartToPartShearCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_pulley(self) -> 'List[_2572.Pulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_rolling_ring(self) -> 'List[_2578.RollingRing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2579.RollingRingAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2580.ShaftHubConnection]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spring_damper(self) -> 'List[_2582.SpringDamper]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2583.SpringDamperHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamperHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser(self) -> 'List[_2584.Synchroniser]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2586.SynchroniserHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserHalf')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2587.SynchroniserPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2588.SynchroniserSleeve]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter(self) -> 'List[_2589.TorqueConverter]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2590.TorqueConverterPump]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterPump')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2592.TorqueConverterTurbine]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        """

        cast_type = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')
        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[cast_type]())

    @staticmethod
    def load(file_path: 'str', load_full_fe_option: Optional['_1572.ExternalFullFEFileOption'] = _1572.ExternalFullFEFileOption.MESH_AND_EXPANSION_VECTORS) -> 'Design':
        """ 'Load' is the original name of this method.

        Args:
            file_path (str)
            load_full_fe_option (mastapy.utility.ExternalFullFEFileOption, optional)

        Returns:
            mastapy.system_model.Design
        """

        file_path = str(file_path)
        file_path = path.abspath(file_path)
        load_full_fe_option = conversion.mp_to_pn_enum(load_full_fe_option, 'SMT.MastaAPI.Utility.ExternalFullFEFileOption')
        method_result = Design.TYPE.Load(file_path if file_path else '', load_full_fe_option)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @staticmethod
    def load_example(example_string: 'str') -> 'Design':
        """ 'LoadExample' is the original name of this method.

        Args:
            example_string (str)

        Returns:
            mastapy.system_model.Design
        """

        example_string = str(example_string)
        method_result = Design.TYPE.LoadExample(example_string if example_string else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def compare_for_test_only(self, design: 'Design', sb: 'str') -> 'bool':
        """ 'CompareForTestOnly' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
            sb (str)

        Returns:
            bool
        """

        sb = str(sb)
        method_result = self.wrapped.CompareForTestOnly(design.wrapped if design else None, sb if sb else '')
        return method_result

    def add_bearing_detail_configuration_all_bearings(self):
        """ 'AddBearingDetailConfigurationAllBearings' is the original name of this method."""

        self.wrapped.AddBearingDetailConfigurationAllBearings()

    def add_bearing_detail_configuration_rolling_bearings(self):
        """ 'AddBearingDetailConfigurationRollingBearings' is the original name of this method."""

        self.wrapped.AddBearingDetailConfigurationRollingBearings()

    def add_fe_substructure_configuration(self):
        """ 'AddFESubstructureConfiguration' is the original name of this method."""

        self.wrapped.AddFESubstructureConfiguration()

    def add_gear_set_configuration(self):
        """ 'AddGearSetConfiguration' is the original name of this method."""

        self.wrapped.AddGearSetConfiguration()

    def add_shaft_detail_configuration(self):
        """ 'AddShaftDetailConfiguration' is the original name of this method."""

        self.wrapped.AddShaftDetailConfiguration()

    def change_gears_to_clones_where_suitable(self):
        """ 'ChangeGearsToClonesWhereSuitable' is the original name of this method."""

        self.wrapped.ChangeGearsToClonesWhereSuitable()

    def clear_undo_redo_stacks(self):
        """ 'ClearUndoRedoStacks' is the original name of this method."""

        self.wrapped.ClearUndoRedoStacks()

    def compare_results_to_previous_masta_version(self):
        """ 'CompareResultsToPreviousMASTAVersion' is the original name of this method."""

        self.wrapped.CompareResultsToPreviousMASTAVersion()

    def delete_all_gear_set_configurations_that_have_errors_or_warnings(self):
        """ 'DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings' is the original name of this method."""

        self.wrapped.DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings()

    def delete_all_gear_sets_designs_that_are_not_used_in_configurations(self):
        """ 'DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations' is the original name of this method."""

        self.wrapped.DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations()

    def delete_all_inactive_gear_set_designs(self):
        """ 'DeleteAllInactiveGearSetDesigns' is the original name of this method."""

        self.wrapped.DeleteAllInactiveGearSetDesigns()

    def delete_multiple_bearing_detail_configurations(self):
        """ 'DeleteMultipleBearingDetailConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleBearingDetailConfigurations()

    def delete_multiple_fe_substructure_configurations(self):
        """ 'DeleteMultipleFESubstructureConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleFESubstructureConfigurations()

    def delete_multiple_gear_set_configurations(self):
        """ 'DeleteMultipleGearSetConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleGearSetConfigurations()

    def delete_multiple_shaft_detail_configurations(self):
        """ 'DeleteMultipleShaftDetailConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleShaftDetailConfigurations()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()

    @property
    def cast_to(self) -> 'Design._Cast_Design':
        return self._Cast_Design(self)
