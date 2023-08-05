"""list_with_selected_item.py

Implementations of 'ListWithSelectedItem' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from typing import List, Generic, TypeVar

from mastapy._internal import mixins, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.ltca.cylindrical import _853, _854
from mastapy.gears.manufacturing.cylindrical import _622
from mastapy.gears.manufacturing.bevel import _788
from mastapy.electric_machines import _1261, _1287, _1256
from mastapy.electric_machines.results import _1317
from mastapy.utility import _1591
from mastapy.utility.units_and_measurements import _1601, _1596
from mastapy.utility.file_access_helpers import _1806
from mastapy.system_model.part_model import (
    _2455, _2427, _2431, _2438,
    _2436, _2454
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5652, _5740
from mastapy._internal.tuple_with_name import TupleWithName
from mastapy.system_model.analyses_and_results.system_deflections import _2741, _2727
from mastapy.system_model.part_model.gears import _2514, _2507, _2508
from mastapy.system_model.fe import _2368, _2366, _2356
from mastapy.nodal_analysis.component_mode_synthesis import _223
from mastapy.system_model.fe.links import _2401
from mastapy.system_model.part_model.part_groups import _2470
from mastapy.gears.gear_designs import _947
from mastapy.system_model.part_model.couplings import _2580
from mastapy.system_model.analyses_and_results.load_case_groups import _5636, _5637
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5821
from mastapy.system_model.analyses_and_results.static_loads import _6772

_ARRAY = python_net_import('System', 'Array')
_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'ListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = (
    'ListWithSelectedItem_str', 'ListWithSelectedItem_int',
    'ListWithSelectedItem_T', 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis',
    'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis', 'ListWithSelectedItem_CylindricalSetManufacturingConfig',
    'ListWithSelectedItem_ConicalSetManufacturingConfig', 'ListWithSelectedItem_ElectricMachineSetup',
    'ListWithSelectedItem_float', 'ListWithSelectedItem_ElectricMachineResults',
    'ListWithSelectedItem_RotorSkewSlice', 'ListWithSelectedItem_SystemDirectory',
    'ListWithSelectedItem_Unit', 'ListWithSelectedItem_MeasurementBase',
    'ListWithSelectedItem_ColumnTitle', 'ListWithSelectedItem_PowerLoad',
    'ListWithSelectedItem_AbstractPeriodicExcitationDetail', 'ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase',
    'ListWithSelectedItem_TupleWithName', 'ListWithSelectedItem_GearMeshSystemDeflection',
    'ListWithSelectedItem_GearSet', 'ListWithSelectedItem_FESubstructureNode',
    'ListWithSelectedItem_FESubstructure', 'ListWithSelectedItem_CMSElementFaceGroup',
    'ListWithSelectedItem_Component', 'ListWithSelectedItem_Datum',
    'ListWithSelectedItem_FELink', 'ListWithSelectedItem_CylindricalGear',
    'ListWithSelectedItem_ElectricMachineDetail', 'ListWithSelectedItem_GuideDxfModel',
    'ListWithSelectedItem_ConcentricPartGroup', 'ListWithSelectedItem_CylindricalGearSet',
    'ListWithSelectedItem_GearSetDesign', 'ListWithSelectedItem_ShaftHubConnection',
    'ListWithSelectedItem_TSelectableItem', 'ListWithSelectedItem_CylindricalGearSystemDeflection',
    'ListWithSelectedItem_DesignState', 'ListWithSelectedItem_FEPart',
    'ListWithSelectedItem_TPartAnalysis', 'ListWithSelectedItem_ResultLocationSelectionGroup',
    'ListWithSelectedItem_StaticLoadCase', 'ListWithSelectedItem_DutyCycle',
    'ListWithSelectedItem_ElectricMachineDataSet', 'ListWithSelectedItem_PointLoad'
)


T = TypeVar('T')
TSelectableItem = TypeVar('TSelectableItem')
TPartAnalysis = TypeVar('TPartAnalysis')


class ListWithSelectedItem_str(str, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_str

    A specific implementation of 'ListWithSelectedItem' for 'str' types.
    """
    __qualname__ = 'str'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        return str.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else '')

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'str':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return str

    @property
    def selected_value(self) -> 'str':
        """str: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return ''

        return temp

    @property
    def available_values(self) -> 'List[str]':
        """List[str]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    """
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'int':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def selected_value(self) -> 'int':
        """int: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0

        return temp

    @property
    def available_values(self) -> 'List[int]':
        """List[int]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value


class ListWithSelectedItem_T(Generic[T], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_T

    A specific implementation of 'ListWithSelectedItem' for 'T' types.
    """
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'T':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def selected_value(self) -> 'T':
        """T: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[T]':
        """List[T]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis(_853.CylindricalGearLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_853.CylindricalGearLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _853.CylindricalGearLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_853.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_853.CylindricalGearLoadDistributionAnalysis]':
        """List[CylindricalGearLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis(_854.CylindricalGearMeshLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearMeshLoadDistributionAnalysis' types.
    """
    __qualname__ = 'CylindricalGearMeshLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_854.CylindricalGearMeshLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _854.CylindricalGearMeshLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_854.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_854.CylindricalGearMeshLoadDistributionAnalysis]':
        """List[CylindricalGearMeshLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalSetManufacturingConfig(_622.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    """
    __qualname__ = 'CylindricalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_622.CylindricalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _622.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_622.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_622.CylindricalSetManufacturingConfig]':
        """List[CylindricalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConicalSetManufacturingConfig(_788.ConicalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConicalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'ConicalSetManufacturingConfig' types.
    """
    __qualname__ = 'ConicalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConicalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_788.ConicalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _788.ConicalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_788.ConicalSetManufacturingConfig':
        """ConicalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_788.ConicalSetManufacturingConfig]':
        """List[ConicalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineSetup(_1261.ElectricMachineSetup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineSetup

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineSetup' types.
    """
    __qualname__ = 'ElectricMachineSetup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineSetup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1261.ElectricMachineSetup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1261.ElectricMachineSetup.TYPE

    @property
    def selected_value(self) -> '_1261.ElectricMachineSetup':
        """ElectricMachineSetup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1261.ElectricMachineSetup]':
        """List[ElectricMachineSetup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_float(float, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_float

    A specific implementation of 'ListWithSelectedItem' for 'float' types.
    """
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0.0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'float':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return float

    @property
    def selected_value(self) -> 'float':
        """float: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return 0.0

        return temp

    @property
    def available_values(self) -> 'List[float]':
        """List[float]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value


class ListWithSelectedItem_ElectricMachineResults(_1317.ElectricMachineResults, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineResults

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineResults' types.
    """
    __qualname__ = 'ElectricMachineResults'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineResults.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1317.ElectricMachineResults.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1317.ElectricMachineResults.TYPE

    @property
    def selected_value(self) -> '_1317.ElectricMachineResults':
        """ElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1317.ElectricMachineResults]':
        """List[ElectricMachineResults]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_RotorSkewSlice(_1287.RotorSkewSlice, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_RotorSkewSlice

    A specific implementation of 'ListWithSelectedItem' for 'RotorSkewSlice' types.
    """
    __qualname__ = 'RotorSkewSlice'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_RotorSkewSlice.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1287.RotorSkewSlice.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1287.RotorSkewSlice.TYPE

    @property
    def selected_value(self) -> '_1287.RotorSkewSlice':
        """RotorSkewSlice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1287.RotorSkewSlice]':
        """List[RotorSkewSlice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_SystemDirectory(_1591.SystemDirectory, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_SystemDirectory

    A specific implementation of 'ListWithSelectedItem' for 'SystemDirectory' types.
    """
    __qualname__ = 'SystemDirectory'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_SystemDirectory.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1591.SystemDirectory.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1591.SystemDirectory.TYPE

    @property
    def selected_value(self) -> '_1591.SystemDirectory':
        """SystemDirectory: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1591.SystemDirectory]':
        """List[SystemDirectory]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Unit(_1601.Unit, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Unit

    A specific implementation of 'ListWithSelectedItem' for 'Unit' types.
    """
    __qualname__ = 'Unit'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Unit.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1601.Unit.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1601.Unit.TYPE

    @property
    def selected_value(self) -> '_1601.Unit':
        """Unit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1601.Unit]':
        """List[Unit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_MeasurementBase(_1596.MeasurementBase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_MeasurementBase

    A specific implementation of 'ListWithSelectedItem' for 'MeasurementBase' types.
    """
    __qualname__ = 'MeasurementBase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_MeasurementBase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1596.MeasurementBase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1596.MeasurementBase.TYPE

    @property
    def selected_value(self) -> '_1596.MeasurementBase':
        """MeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1596.MeasurementBase]':
        """List[MeasurementBase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ColumnTitle(_1806.ColumnTitle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    """
    __qualname__ = 'ColumnTitle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ColumnTitle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1806.ColumnTitle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1806.ColumnTitle.TYPE

    @property
    def selected_value(self) -> '_1806.ColumnTitle':
        """ColumnTitle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1806.ColumnTitle]':
        """List[ColumnTitle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PowerLoad(_2455.PowerLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PowerLoad

    A specific implementation of 'ListWithSelectedItem' for 'PowerLoad' types.
    """
    __qualname__ = 'PowerLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PowerLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2455.PowerLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2455.PowerLoad.TYPE

    @property
    def selected_value(self) -> '_2455.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2455.PowerLoad]':
        """List[PowerLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_AbstractPeriodicExcitationDetail(_5652.AbstractPeriodicExcitationDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_AbstractPeriodicExcitationDetail

    A specific implementation of 'ListWithSelectedItem' for 'AbstractPeriodicExcitationDetail' types.
    """
    __qualname__ = 'AbstractPeriodicExcitationDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_AbstractPeriodicExcitationDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5652.AbstractPeriodicExcitationDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5652.AbstractPeriodicExcitationDetail.TYPE

    @property
    def selected_value(self) -> '_5652.AbstractPeriodicExcitationDetail':
        """AbstractPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5652.AbstractPeriodicExcitationDetail]':
        """List[AbstractPeriodicExcitationDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase(_5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'HarmonicAnalysisWithVaryingStiffnessStaticLoadCase' types.
    """
    __qualname__ = 'HarmonicAnalysisWithVaryingStiffnessStaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase':
        """HarmonicAnalysisWithVaryingStiffnessStaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5740.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase]':
        """List[HarmonicAnalysisWithVaryingStiffnessStaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TupleWithName(TupleWithName, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TupleWithName

    A specific implementation of 'ListWithSelectedItem' for 'TupleWithName' types.
    """
    __qualname__ = 'TupleWithName'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TupleWithName.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TupleWithName.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TupleWithName.TYPE

    @property
    def selected_value(self) -> 'TupleWithName':
        """TupleWithName: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        value = conversion.pn_to_mp_tuple_with_name(temp, (None))
        return constructor.new_from_mastapy_class(TupleWithName)(value) if value is not None else None

    @property
    def available_values(self) -> 'TupleWithName':
        """TupleWithName: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return constructor.new_from_mastapy_class(TupleWithName)(value) if value is not None else None


class ListWithSelectedItem_GearMeshSystemDeflection(_2741.GearMeshSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearMeshSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'GearMeshSystemDeflection' types.
    """
    __qualname__ = 'GearMeshSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearMeshSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2741.GearMeshSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2741.GearMeshSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2741.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2741.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSet(_2514.GearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSet

    A specific implementation of 'ListWithSelectedItem' for 'GearSet' types.
    """
    __qualname__ = 'GearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2514.GearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2514.GearSet.TYPE

    @property
    def selected_value(self) -> '_2514.GearSet':
        """GearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2514.GearSet]':
        """List[GearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructureNode(_2368.FESubstructureNode, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructureNode

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructureNode' types.
    """
    __qualname__ = 'FESubstructureNode'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructureNode.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2368.FESubstructureNode.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2368.FESubstructureNode.TYPE

    @property
    def selected_value(self) -> '_2368.FESubstructureNode':
        """FESubstructureNode: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2368.FESubstructureNode]':
        """List[FESubstructureNode]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructure(_2366.FESubstructure, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructure

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructure' types.
    """
    __qualname__ = 'FESubstructure'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructure.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2366.FESubstructure.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2366.FESubstructure.TYPE

    @property
    def selected_value(self) -> '_2366.FESubstructure':
        """FESubstructure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2366.FESubstructure]':
        """List[FESubstructure]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CMSElementFaceGroup(_223.CMSElementFaceGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CMSElementFaceGroup

    A specific implementation of 'ListWithSelectedItem' for 'CMSElementFaceGroup' types.
    """
    __qualname__ = 'CMSElementFaceGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CMSElementFaceGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_223.CMSElementFaceGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _223.CMSElementFaceGroup.TYPE

    @property
    def selected_value(self) -> '_223.CMSElementFaceGroup':
        """CMSElementFaceGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_223.CMSElementFaceGroup]':
        """List[CMSElementFaceGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Component(_2427.Component, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Component

    A specific implementation of 'ListWithSelectedItem' for 'Component' types.
    """
    __qualname__ = 'Component'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Component.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2427.Component.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2427.Component.TYPE

    @property
    def selected_value(self) -> '_2427.Component':
        """Component: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2427.Component]':
        """List[Component]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Datum(_2431.Datum, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Datum

    A specific implementation of 'ListWithSelectedItem' for 'Datum' types.
    """
    __qualname__ = 'Datum'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Datum.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2431.Datum.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2431.Datum.TYPE

    @property
    def selected_value(self) -> '_2431.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2431.Datum]':
        """List[Datum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FELink(_2401.FELink, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FELink

    A specific implementation of 'ListWithSelectedItem' for 'FELink' types.
    """
    __qualname__ = 'FELink'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FELink.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2401.FELink.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2401.FELink.TYPE

    @property
    def selected_value(self) -> '_2401.FELink':
        """FELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2401.FELink]':
        """List[FELink]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGear(_2507.CylindricalGear, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGear

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGear' types.
    """
    __qualname__ = 'CylindricalGear'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGear.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2507.CylindricalGear.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2507.CylindricalGear.TYPE

    @property
    def selected_value(self) -> '_2507.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2507.CylindricalGear]':
        """List[CylindricalGear]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDetail(_1256.ElectricMachineDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDetail

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDetail' types.
    """
    __qualname__ = 'ElectricMachineDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1256.ElectricMachineDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1256.ElectricMachineDetail.TYPE

    @property
    def selected_value(self) -> '_1256.ElectricMachineDetail':
        """ElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1256.ElectricMachineDetail]':
        """List[ElectricMachineDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GuideDxfModel(_2438.GuideDxfModel, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GuideDxfModel

    A specific implementation of 'ListWithSelectedItem' for 'GuideDxfModel' types.
    """
    __qualname__ = 'GuideDxfModel'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GuideDxfModel.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2438.GuideDxfModel.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2438.GuideDxfModel.TYPE

    @property
    def selected_value(self) -> '_2438.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2438.GuideDxfModel]':
        """List[GuideDxfModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConcentricPartGroup(_2470.ConcentricPartGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConcentricPartGroup

    A specific implementation of 'ListWithSelectedItem' for 'ConcentricPartGroup' types.
    """
    __qualname__ = 'ConcentricPartGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConcentricPartGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2470.ConcentricPartGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2470.ConcentricPartGroup.TYPE

    @property
    def selected_value(self) -> '_2470.ConcentricPartGroup':
        """ConcentricPartGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2470.ConcentricPartGroup]':
        """List[ConcentricPartGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSet(_2508.CylindricalGearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSet

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSet' types.
    """
    __qualname__ = 'CylindricalGearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2508.CylindricalGearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2508.CylindricalGearSet.TYPE

    @property
    def selected_value(self) -> '_2508.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2508.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSetDesign(_947.GearSetDesign, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSetDesign

    A specific implementation of 'ListWithSelectedItem' for 'GearSetDesign' types.
    """
    __qualname__ = 'GearSetDesign'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSetDesign.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_947.GearSetDesign.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _947.GearSetDesign.TYPE

    @property
    def selected_value(self) -> '_947.GearSetDesign':
        """GearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_947.GearSetDesign]':
        """List[GearSetDesign]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ShaftHubConnection(_2580.ShaftHubConnection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ShaftHubConnection

    A specific implementation of 'ListWithSelectedItem' for 'ShaftHubConnection' types.
    """
    __qualname__ = 'ShaftHubConnection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ShaftHubConnection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2580.ShaftHubConnection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2580.ShaftHubConnection.TYPE

    @property
    def selected_value(self) -> '_2580.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2580.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TSelectableItem(Generic[TSelectableItem], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    """
    __qualname__ = 'TSelectableItem'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TSelectableItem.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TSelectableItem':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TSelectableItem

    @property
    def selected_value(self) -> 'TSelectableItem':
        """TSelectableItem: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TSelectableItem]':
        """List[TSelectableItem]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSystemDeflection(_2727.CylindricalGearSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSystemDeflection' types.
    """
    __qualname__ = 'CylindricalGearSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2727.CylindricalGearSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2727.CylindricalGearSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2727.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2727.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DesignState(_5636.DesignState, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DesignState

    A specific implementation of 'ListWithSelectedItem' for 'DesignState' types.
    """
    __qualname__ = 'DesignState'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DesignState.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5636.DesignState.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5636.DesignState.TYPE

    @property
    def selected_value(self) -> '_5636.DesignState':
        """DesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5636.DesignState]':
        """List[DesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FEPart(_2436.FEPart, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FEPart

    A specific implementation of 'ListWithSelectedItem' for 'FEPart' types.
    """
    __qualname__ = 'FEPart'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FEPart.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2436.FEPart.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2436.FEPart.TYPE

    @property
    def selected_value(self) -> '_2436.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2436.FEPart]':
        """List[FEPart]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TPartAnalysis(Generic[TPartAnalysis], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TPartAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'TPartAnalysis' types.
    """
    __qualname__ = 'TPartAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TPartAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TPartAnalysis':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TPartAnalysis

    @property
    def selected_value(self) -> 'TPartAnalysis':
        """TPartAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TPartAnalysis]':
        """List[TPartAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ResultLocationSelectionGroup(_5821.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    """
    __qualname__ = 'ResultLocationSelectionGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ResultLocationSelectionGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5821.ResultLocationSelectionGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5821.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self) -> '_5821.ResultLocationSelectionGroup':
        """ResultLocationSelectionGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5821.ResultLocationSelectionGroup]':
        """List[ResultLocationSelectionGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_StaticLoadCase(_6772.StaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_StaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'StaticLoadCase' types.
    """
    __qualname__ = 'StaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_StaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_6772.StaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6772.StaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_6772.StaticLoadCase':
        """StaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_6772.StaticLoadCase]':
        """List[StaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DutyCycle(_5637.DutyCycle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DutyCycle

    A specific implementation of 'ListWithSelectedItem' for 'DutyCycle' types.
    """
    __qualname__ = 'DutyCycle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DutyCycle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5637.DutyCycle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5637.DutyCycle.TYPE

    @property
    def selected_value(self) -> '_5637.DutyCycle':
        """DutyCycle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5637.DutyCycle]':
        """List[DutyCycle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDataSet(_2356.ElectricMachineDataSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDataSet

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDataSet' types.
    """
    __qualname__ = 'ElectricMachineDataSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDataSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2356.ElectricMachineDataSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2356.ElectricMachineDataSet.TYPE

    @property
    def selected_value(self) -> '_2356.ElectricMachineDataSet':
        """ElectricMachineDataSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2356.ElectricMachineDataSet]':
        """List[ElectricMachineDataSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PointLoad(_2454.PointLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PointLoad

    A specific implementation of 'ListWithSelectedItem' for 'PointLoad' types.
    """
    __qualname__ = 'PointLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PointLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2454.PointLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2454.PointLoad.TYPE

    @property
    def selected_value(self) -> '_2454.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2454.PointLoad]':
        """List[PointLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
