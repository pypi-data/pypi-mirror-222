﻿"""_1368.py

ElectricMachineHarmonicLoadDataBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from PIL.Image import Image

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines.harmonic_load_data import _1373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'ElectricMachineHarmonicLoadDataBase')

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import (
        _1372, _1369, _1375, _1376
    )
    from mastapy.utility_gui.charts import _1853, _1849
    from mastapy.electric_machines import _1287
    from mastapy.math_utility import _1511


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineHarmonicLoadDataBase',)


class ElectricMachineHarmonicLoadDataBase(_1373.SpeedDependentHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_BASE

    class _Cast_ElectricMachineHarmonicLoadDataBase:
        """Special nested class for casting ElectricMachineHarmonicLoadDataBase to subclasses."""

        def __init__(self, parent: 'ElectricMachineHarmonicLoadDataBase'):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(self):
            return self._parent._cast(_1373.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1370
            
            return self._parent._cast(_1370.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(self):
            from mastapy.electric_machines.results import _1312
            
            return self._parent._cast(_1312.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6839
            
            return self._parent._cast(_6839.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6840
            
            return self._parent._cast(_6840.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6841
            
            return self._parent._cast(_6841.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6842
            
            return self._parent._cast(_6842.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6843
            
            return self._parent._cast(_6843.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6844
            
            return self._parent._cast(_6844.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6845
            
            return self._parent._cast(_6845.ElectricMachineHarmonicLoadDataFromMotorPackages)

        @property
        def electric_machine_harmonic_load_data_base(self) -> 'ElectricMachineHarmonicLoadDataBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineHarmonicLoadDataBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(self) -> 'bool':
        """bool: 'CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads' is the original name of this property."""

        temp = self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads

        if temp is None:
            return False

        return temp

    @compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads.setter
    def compare_torque_ripple_and_stator_torque_reaction_derived_from_stator_tangential_loads(self, value: 'bool'):
        self.wrapped.CompareTorqueRippleAndStatorTorqueReactionDerivedFromStatorTangentialLoads = bool(value) if value is not None else False

    @property
    def data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts(self) -> 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType':
        """enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType: 'DataTypeForForceMomentDistributionAndTemporalSpatialHarmonicsCharts' is the original name of this property."""

        temp = self.wrapped.DataTypeForForceMomentDistributionAndTemporalSpatialHarmonicsCharts

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts.setter
    def data_type_for_force_moment_distribution_and_temporal_spatial_harmonics_charts(self, value: 'enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataTypeForForceMomentDistributionAndTemporalSpatialHarmonicsCharts = value

    @property
    def display_interpolated_data(self) -> 'bool':
        """bool: 'DisplayInterpolatedData' is the original name of this property."""

        temp = self.wrapped.DisplayInterpolatedData

        if temp is None:
            return False

        return temp

    @display_interpolated_data.setter
    def display_interpolated_data(self, value: 'bool'):
        self.wrapped.DisplayInterpolatedData = bool(value) if value is not None else False

    @property
    def display_option_for_slice_data(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption':
        """enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption: 'DisplayOptionForSliceData' is the original name of this property."""

        temp = self.wrapped.DisplayOptionForSliceData

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @display_option_for_slice_data.setter
    def display_option_for_slice_data(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ForceDisplayOption.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DisplayOptionForSliceData = value

    @property
    def force_distribution_3d(self) -> '_1853.ThreeDVectorChartDefinition':
        """ThreeDVectorChartDefinition: 'ForceDistribution3D' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceDistribution3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_moment_distribution(self) -> 'Image':
        """Image: 'ForceMomentDistribution' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceMomentDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def invert_axis(self) -> 'bool':
        """bool: 'InvertAxis' is the original name of this property."""

        temp = self.wrapped.InvertAxis

        if temp is None:
            return False

        return temp

    @invert_axis.setter
    def invert_axis(self, value: 'bool'):
        self.wrapped.InvertAxis = bool(value) if value is not None else False

    @property
    def plot_as_vectors(self) -> 'bool':
        """bool: 'PlotAsVectors' is the original name of this property."""

        temp = self.wrapped.PlotAsVectors

        if temp is None:
            return False

        return temp

    @plot_as_vectors.setter
    def plot_as_vectors(self, value: 'bool'):
        self.wrapped.PlotAsVectors = bool(value) if value is not None else False

    @property
    def show_all_forces(self) -> 'bool':
        """bool: 'ShowAllForces' is the original name of this property."""

        temp = self.wrapped.ShowAllForces

        if temp is None:
            return False

        return temp

    @show_all_forces.setter
    def show_all_forces(self, value: 'bool'):
        self.wrapped.ShowAllForces = bool(value) if value is not None else False

    @property
    def show_all_teeth(self) -> 'bool':
        """bool: 'ShowAllTeeth' is the original name of this property."""

        temp = self.wrapped.ShowAllTeeth

        if temp is None:
            return False

        return temp

    @show_all_teeth.setter
    def show_all_teeth(self, value: 'bool'):
        self.wrapped.ShowAllTeeth = bool(value) if value is not None else False

    @property
    def slice(self) -> 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice':
        """list_with_selected_item.ListWithSelectedItem_RotorSkewSlice: 'Slice' is the original name of this property."""

        temp = self.wrapped.Slice

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_RotorSkewSlice')(temp) if temp is not None else None

    @slice.setter
    def slice(self, value: 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Slice = value

    @property
    def speed_to_view(self) -> 'float':
        """float: 'SpeedToView' is the original name of this property."""

        temp = self.wrapped.SpeedToView

        if temp is None:
            return 0.0

        return temp

    @speed_to_view.setter
    def speed_to_view(self, value: 'float'):
        self.wrapped.SpeedToView = float(value) if value is not None else 0.0

    @property
    def stator_axial_loads_amplitude_cut_off(self) -> 'float':
        """float: 'StatorAxialLoadsAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.StatorAxialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_axial_loads_amplitude_cut_off.setter
    def stator_axial_loads_amplitude_cut_off(self, value: 'float'):
        self.wrapped.StatorAxialLoadsAmplitudeCutOff = float(value) if value is not None else 0.0

    @property
    def stator_radial_loads_amplitude_cut_off(self) -> 'float':
        """float: 'StatorRadialLoadsAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.StatorRadialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_radial_loads_amplitude_cut_off.setter
    def stator_radial_loads_amplitude_cut_off(self, value: 'float'):
        self.wrapped.StatorRadialLoadsAmplitudeCutOff = float(value) if value is not None else 0.0

    @property
    def stator_tangential_loads_amplitude_cut_off(self) -> 'float':
        """float: 'StatorTangentialLoadsAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.StatorTangentialLoadsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_tangential_loads_amplitude_cut_off.setter
    def stator_tangential_loads_amplitude_cut_off(self, value: 'float'):
        self.wrapped.StatorTangentialLoadsAmplitudeCutOff = float(value) if value is not None else 0.0

    @property
    def stator_tooth_moments_amplitude_cut_off(self) -> 'float':
        """float: 'StatorToothMomentsAmplitudeCutOff' is the original name of this property."""

        temp = self.wrapped.StatorToothMomentsAmplitudeCutOff

        if temp is None:
            return 0.0

        return temp

    @stator_tooth_moments_amplitude_cut_off.setter
    def stator_tooth_moments_amplitude_cut_off(self, value: 'float'):
        self.wrapped.StatorToothMomentsAmplitudeCutOff = float(value) if value is not None else 0.0

    @property
    def sum_over_all_nodes(self) -> 'bool':
        """bool: 'SumOverAllNodes' is the original name of this property."""

        temp = self.wrapped.SumOverAllNodes

        if temp is None:
            return False

        return temp

    @sum_over_all_nodes.setter
    def sum_over_all_nodes(self, value: 'bool'):
        self.wrapped.SumOverAllNodes = bool(value) if value is not None else False

    @property
    def temporal_spatial_harmonics_chart(self) -> '_1849.ScatterChartDefinition':
        """ScatterChartDefinition: 'TemporalSpatialHarmonicsChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemporalSpatialHarmonicsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def use_log_scale_for_temporal_spatial_harmonics_chart(self) -> 'bool':
        """bool: 'UseLogScaleForTemporalSpatialHarmonicsChart' is the original name of this property."""

        temp = self.wrapped.UseLogScaleForTemporalSpatialHarmonicsChart

        if temp is None:
            return False

        return temp

    @use_log_scale_for_temporal_spatial_harmonics_chart.setter
    def use_log_scale_for_temporal_spatial_harmonics_chart(self, value: 'bool'):
        self.wrapped.UseLogScaleForTemporalSpatialHarmonicsChart = bool(value) if value is not None else False

    @property
    def stator_axial_loads(self) -> '_1375.StatorToothLoadInterpolator':
        """StatorToothLoadInterpolator: 'StatorAxialLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorAxialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_radial_loads(self) -> '_1375.StatorToothLoadInterpolator':
        """StatorToothLoadInterpolator: 'StatorRadialLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorRadialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_tangential_loads(self) -> '_1375.StatorToothLoadInterpolator':
        """StatorToothLoadInterpolator: 'StatorTangentialLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorTangentialLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_tooth_moments(self) -> '_1376.StatorToothMomentInterpolator':
        """StatorToothMomentInterpolator: 'StatorToothMoments' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorToothMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def multiple_fourier_series_interpolator_for(self, harmonic_load_data_type: '_1372.HarmonicLoadDataType', slice_index: 'int') -> '_1511.MultipleFourierSeriesInterpolator':
        """ 'MultipleFourierSeriesInterpolatorFor' is the original name of this method.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)

        Returns:
            mastapy.math_utility.MultipleFourierSeriesInterpolator
        """

        harmonic_load_data_type = conversion.mp_to_pn_enum(harmonic_load_data_type, 'SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType')
        slice_index = int(slice_index)
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor(harmonic_load_data_type, slice_index if slice_index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def stator_tooth_load_interpolator_for(self, harmonic_load_data_type: '_1372.HarmonicLoadDataType', slice_index: 'int') -> '_1375.StatorToothLoadInterpolator':
        """ 'StatorToothLoadInterpolatorFor' is the original name of this method.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)

        Returns:
            mastapy.electric_machines.harmonic_load_data.StatorToothLoadInterpolator
        """

        harmonic_load_data_type = conversion.mp_to_pn_enum(harmonic_load_data_type, 'SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType')
        slice_index = int(slice_index)
        method_result = self.wrapped.StatorToothLoadInterpolatorFor(harmonic_load_data_type, slice_index if slice_index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def stator_tooth_moment_interpolator_for(self, harmonic_load_data_type: '_1372.HarmonicLoadDataType', slice_index: 'int') -> '_1376.StatorToothMomentInterpolator':
        """ 'StatorToothMomentInterpolatorFor' is the original name of this method.

        Args:
            harmonic_load_data_type (mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType)
            slice_index (int)

        Returns:
            mastapy.electric_machines.harmonic_load_data.StatorToothMomentInterpolator
        """

        harmonic_load_data_type = conversion.mp_to_pn_enum(harmonic_load_data_type, 'SMT.MastaAPI.ElectricMachines.HarmonicLoadData.HarmonicLoadDataType')
        slice_index = int(slice_index)
        method_result = self.wrapped.StatorToothMomentInterpolatorFor(harmonic_load_data_type, slice_index if slice_index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @property
    def cast_to(self) -> 'ElectricMachineHarmonicLoadDataBase._Cast_ElectricMachineHarmonicLoadDataBase':
        return self._Cast_ElectricMachineHarmonicLoadDataBase(self)
