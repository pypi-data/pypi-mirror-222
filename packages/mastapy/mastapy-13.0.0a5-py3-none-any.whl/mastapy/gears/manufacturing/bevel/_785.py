"""_785.py

ConicalPinionManufacturingConfig
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _773
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CONICAL_PINION_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionManufacturingConfig')

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import (
        _782, _778, _803, _807
    )
    from mastapy.gears.manufacturing.bevel.cutters import _810, _811


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionManufacturingConfig',)


class ConicalPinionManufacturingConfig(_773.ConicalGearManufacturingConfig):
    """ConicalPinionManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MANUFACTURING_CONFIG

    class _Cast_ConicalPinionManufacturingConfig:
        """Special nested class for casting ConicalPinionManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalPinionManufacturingConfig'):
            self._parent = parent

        @property
        def conical_gear_manufacturing_config(self):
            return self._parent._cast(_773.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _775
            
            return self._parent._cast(_775.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1217
            
            return self._parent._cast(_1217.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def conical_pinion_manufacturing_config(self) -> 'ConicalPinionManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalPinionManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_finish_manufacturing_machine(self) -> 'str':
        """str: 'PinionFinishManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.PinionFinishManufacturingMachine.SelectedItemName

        if temp is None:
            return ''

        return temp

    @pinion_finish_manufacturing_machine.setter
    def pinion_finish_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionFinishManufacturingMachine.SetSelectedItem(str(value) if value is not None else '')

    @property
    def pinion_rough_manufacturing_machine(self) -> 'str':
        """str: 'PinionRoughManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.PinionRoughManufacturingMachine.SelectedItemName

        if temp is None:
            return ''

        return temp

    @pinion_rough_manufacturing_machine.setter
    def pinion_rough_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionRoughManufacturingMachine.SetSelectedItem(str(value) if value is not None else '')

    @property
    def mesh_config(self) -> '_782.ConicalMeshManufacturingConfig':
        """ConicalMeshManufacturingConfig: 'MeshConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_concave_ob_configuration(self) -> '_778.ConicalMeshFlankManufacturingConfig':
        """ConicalMeshFlankManufacturingConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_convex_ib_configuration(self) -> '_778.ConicalMeshFlankManufacturingConfig':
        """ConicalMeshFlankManufacturingConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave(self) -> '_803.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex(self) -> '_803.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_finish_cutter(self) -> '_810.PinionFinishCutter':
        """PinionFinishCutter: 'PinionFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_rough_cutter(self) -> '_811.PinionRoughCutter':
        """PinionRoughCutter: 'PinionRoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_rough_machine_setting(self) -> '_807.PinionRoughMachineSetting':
        """PinionRoughMachineSetting: 'PinionRoughMachineSetting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRoughMachineSetting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig':
        return self._Cast_ConicalPinionManufacturingConfig(self)
