"""_6298.py

DynamicAnalysisDrawStyle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'DynamicAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAnalysisDrawStyle',)


class DynamicAnalysisDrawStyle(_2229.ContourDrawStyle):
    """DynamicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS_DRAW_STYLE

    class _Cast_DynamicAnalysisDrawStyle:
        """Special nested class for casting DynamicAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'DynamicAnalysisDrawStyle'):
            self._parent = parent

        @property
        def contour_draw_style(self):
            return self._parent._cast(_2229.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _306
            
            return self._parent._cast(_306.DrawStyleBase)

        @property
        def modal_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632
            
            return self._parent._cast(_4632.ModalAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5733
            
            return self._parent._cast(_5733.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(self) -> 'DynamicAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def animate_contour(self) -> 'bool':
        """bool: 'AnimateContour' is the original name of this property."""

        temp = self.wrapped.AnimateContour

        if temp is None:
            return False

        return temp

    @animate_contour.setter
    def animate_contour(self, value: 'bool'):
        self.wrapped.AnimateContour = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'DynamicAnalysisDrawStyle._Cast_DynamicAnalysisDrawStyle':
        return self._Cast_DynamicAnalysisDrawStyle(self)
