﻿"""_2226.py

AbstractSystemDeflectionViewable
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'AbstractSystemDeflectionViewable')

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2229
    from mastapy.system_model.analyses_and_results.system_deflections import _2808


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractSystemDeflectionViewable',)


class AbstractSystemDeflectionViewable(_2236.PartAnalysisCaseWithContourViewable):
    """AbstractSystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SYSTEM_DEFLECTION_VIEWABLE

    class _Cast_AbstractSystemDeflectionViewable:
        """Special nested class for casting AbstractSystemDeflectionViewable to subclasses."""

        def __init__(self, parent: 'AbstractSystemDeflectionViewable'):
            self._parent = parent

        @property
        def part_analysis_case_with_contour_viewable(self):
            return self._parent._cast(_2236.PartAnalysisCaseWithContourViewable)

        @property
        def advanced_system_deflection_viewable(self):
            from mastapy.system_model.drawing import _2227
            
            return self._parent._cast(_2227.AdvancedSystemDeflectionViewable)

        @property
        def system_deflection_viewable(self):
            from mastapy.system_model.drawing import _2243
            
            return self._parent._cast(_2243.SystemDeflectionViewable)

        @property
        def abstract_system_deflection_viewable(self) -> 'AbstractSystemDeflectionViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractSystemDeflectionViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour_draw_style(self) -> '_2229.ContourDrawStyle':
        """ContourDrawStyle: 'ContourDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContourDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_draw_style(self) -> '_2808.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'SystemDeflectionDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def fe_results(self):
        """ 'FEResults' is the original name of this method."""

        self.wrapped.FEResults()

    @property
    def cast_to(self) -> 'AbstractSystemDeflectionViewable._Cast_AbstractSystemDeflectionViewable':
        return self._Cast_AbstractSystemDeflectionViewable(self)
