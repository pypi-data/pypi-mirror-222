﻿"""_826.py

CylindricalGearFilletNodeStressResultsColumn
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.gears.ltca import _835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN = python_net_import('SMT.MastaAPI.Gears.LTCA', 'CylindricalGearFilletNodeStressResultsColumn')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFilletNodeStressResultsColumn',)


class CylindricalGearFilletNodeStressResultsColumn(_835.GearFilletNodeStressResultsColumn):
    """CylindricalGearFilletNodeStressResultsColumn

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS_COLUMN

    class _Cast_CylindricalGearFilletNodeStressResultsColumn:
        """Special nested class for casting CylindricalGearFilletNodeStressResultsColumn to subclasses."""

        def __init__(self, parent: 'CylindricalGearFilletNodeStressResultsColumn'):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results_column(self):
            return self._parent._cast(_835.GearFilletNodeStressResultsColumn)

        @property
        def cylindrical_gear_fillet_node_stress_results_column(self) -> 'CylindricalGearFilletNodeStressResultsColumn':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearFilletNodeStressResultsColumn.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_position(self) -> 'float':
        """float: 'FaceWidthPosition' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'CylindricalGearFilletNodeStressResultsColumn._Cast_CylindricalGearFilletNodeStressResultsColumn':
        return self._Cast_CylindricalGearFilletNodeStressResultsColumn(self)
