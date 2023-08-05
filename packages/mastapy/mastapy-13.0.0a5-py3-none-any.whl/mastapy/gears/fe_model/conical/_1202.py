"""_1202.py

ConicalSetFEModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.fe_model import _1196
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel.Conical', 'ConicalSetFEModel')

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _58
    from mastapy.gears.fe_model.conical import _1203
    from mastapy.gears.manufacturing.bevel import _788


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetFEModel',)


class ConicalSetFEModel(_1196.GearSetFEModel):
    """ConicalSetFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_FE_MODEL

    class _Cast_ConicalSetFEModel:
        """Special nested class for casting ConicalSetFEModel to subclasses."""

        def __init__(self, parent: 'ConicalSetFEModel'):
            self._parent = parent

        @property
        def gear_set_fe_model(self):
            return self._parent._cast(_1196.GearSetFEModel)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1227
            
            return self._parent._cast(_1227.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.AbstractGearSetAnalysis)

        @property
        def conical_set_fe_model(self) -> 'ConicalSetFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalSetFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_order(self) -> '_58.ElementOrder':
        """ElementOrder: 'ElementOrder' is the original name of this property."""

        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.ElementOrder')
        return constructor.new_from_mastapy('mastapy.nodal_analysis._58', 'ElementOrder')(value) if value is not None else None

    @element_order.setter
    def element_order(self, value: '_58.ElementOrder'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.NodalAnalysis.ElementOrder')
        self.wrapped.ElementOrder = value

    @property
    def flank_data_source(self) -> '_1203.FlankDataSource':
        """FlankDataSource: 'FlankDataSource' is the original name of this property."""

        temp = self.wrapped.FlankDataSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.FEModel.Conical.FlankDataSource')
        return constructor.new_from_mastapy('mastapy.gears.fe_model.conical._1203', 'FlankDataSource')(value) if value is not None else None

    @flank_data_source.setter
    def flank_data_source(self, value: '_1203.FlankDataSource'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.FEModel.Conical.FlankDataSource')
        self.wrapped.FlankDataSource = value

    @property
    def selected_design(self) -> 'list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig':
        """list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig: 'SelectedDesign' is the original name of this property."""

        temp = self.wrapped.SelectedDesign

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_ConicalSetManufacturingConfig')(temp) if temp is not None else None

    @selected_design.setter
    def selected_design(self, value: 'list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedDesign = value

    @property
    def cast_to(self) -> 'ConicalSetFEModel._Cast_ConicalSetFEModel':
        return self._Cast_ConicalSetFEModel(self)
