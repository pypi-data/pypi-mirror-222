﻿"""_897.py

CylindricalGearTwoDimensionalFEAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TWO_DIMENSIONAL_FE_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearTwoDimensionalFEAnalysis')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _183
    from mastapy.gears.gear_two_d_fe_analysis import _898
    from mastapy.nodal_analysis.states import _124


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTwoDimensionalFEAnalysis',)


class CylindricalGearTwoDimensionalFEAnalysis(_0.APIBase):
    """CylindricalGearTwoDimensionalFEAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TWO_DIMENSIONAL_FE_ANALYSIS

    class _Cast_CylindricalGearTwoDimensionalFEAnalysis:
        """Special nested class for casting CylindricalGearTwoDimensionalFEAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearTwoDimensionalFEAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_two_dimensional_fe_analysis(self) -> 'CylindricalGearTwoDimensionalFEAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTwoDimensionalFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_stress_states(self) -> 'int':
        """int: 'NumberOfStressStates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfStressStates

        if temp is None:
            return 0

        return temp

    @property
    def fe_model(self) -> '_183.FEModel':
        """FEModel: 'FEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def findley_critical_plane_analysis(self) -> '_898.FindleyCriticalPlaneAnalysis':
        """FindleyCriticalPlaneAnalysis: 'FindleyCriticalPlaneAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FindleyCriticalPlaneAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def get_stress_states(self, index: 'int') -> '_124.NodeVectorState':
        """ 'GetStressStates' is the original name of this method.

        Args:
            index (int)

        Returns:
            mastapy.nodal_analysis.states.NodeVectorState
        """

        index = int(index)
        method_result = self.wrapped.GetStressStates(index if index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform(self):
        """ 'Perform' is the original name of this method."""

        self.wrapped.Perform()

    @property
    def cast_to(self) -> 'CylindricalGearTwoDimensionalFEAnalysis._Cast_CylindricalGearTwoDimensionalFEAnalysis':
        return self._Cast_CylindricalGearTwoDimensionalFEAnalysis(self)
