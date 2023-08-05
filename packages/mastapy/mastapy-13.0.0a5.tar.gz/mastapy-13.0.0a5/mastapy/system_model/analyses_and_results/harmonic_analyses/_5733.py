"""_5733.py

HarmonicAnalysisDrawStyle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisDrawStyle',)


class HarmonicAnalysisDrawStyle(_6298.DynamicAnalysisDrawStyle):
    """HarmonicAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_DRAW_STYLE

    class _Cast_HarmonicAnalysisDrawStyle:
        """Special nested class for casting HarmonicAnalysisDrawStyle to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisDrawStyle'):
            self._parent = parent

        @property
        def dynamic_analysis_draw_style(self):
            return self._parent._cast(_6298.DynamicAnalysisDrawStyle)

        @property
        def contour_draw_style(self):
            from mastapy.system_model.drawing import _2229
            
            return self._parent._cast(_2229.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _306
            
            return self._parent._cast(_306.DrawStyleBase)

        @property
        def harmonic_analysis_draw_style(self) -> 'HarmonicAnalysisDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HarmonicAnalysisDrawStyle._Cast_HarmonicAnalysisDrawStyle':
        return self._Cast_HarmonicAnalysisDrawStyle(self)
