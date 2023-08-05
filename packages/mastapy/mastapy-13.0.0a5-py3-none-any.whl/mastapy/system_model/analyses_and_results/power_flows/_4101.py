"""_4101.py

PowerFlowDrawStyle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.geometry import _305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_FLOW_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'PowerFlowDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerFlowDrawStyle',)


class PowerFlowDrawStyle(_305.DrawStyle):
    """PowerFlowDrawStyle

    This is a mastapy class.
    """

    TYPE = _POWER_FLOW_DRAW_STYLE

    class _Cast_PowerFlowDrawStyle:
        """Special nested class for casting PowerFlowDrawStyle to subclasses."""

        def __init__(self, parent: 'PowerFlowDrawStyle'):
            self._parent = parent

        @property
        def draw_style(self):
            return self._parent._cast(_305.DrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _306
            
            return self._parent._cast(_306.DrawStyleBase)

        @property
        def cylindrical_gear_geometric_entity_draw_style(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4059
            
            return self._parent._cast(_4059.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(self) -> 'PowerFlowDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerFlowDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def colour_loaded_flanks(self) -> 'bool':
        """bool: 'ColourLoadedFlanks' is the original name of this property."""

        temp = self.wrapped.ColourLoadedFlanks

        if temp is None:
            return False

        return temp

    @colour_loaded_flanks.setter
    def colour_loaded_flanks(self, value: 'bool'):
        self.wrapped.ColourLoadedFlanks = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'PowerFlowDrawStyle._Cast_PowerFlowDrawStyle':
        return self._Cast_PowerFlowDrawStyle(self)
