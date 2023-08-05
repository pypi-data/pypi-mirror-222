﻿"""_2620.py

ModalAnalysisForHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _2617
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ModalAnalysisForHarmonicAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisForHarmonicAnalysis',)


class ModalAnalysisForHarmonicAnalysis(_2617.ModalAnalysis):
    """ModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS

    class _Cast_ModalAnalysisForHarmonicAnalysis:
        """Special nested class for casting ModalAnalysisForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ModalAnalysisForHarmonicAnalysis'):
            self._parent = parent

        @property
        def modal_analysis(self):
            return self._parent._cast(_2617.ModalAnalysis)

        @property
        def static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7516
            
            return self._parent._cast(_7516.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.Context)

        @property
        def modal_analysis_for_harmonic_analysis(self) -> 'ModalAnalysisForHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ModalAnalysisForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_analysis_settings(self) -> '_5736.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis':
        return self._Cast_ModalAnalysisForHarmonicAnalysis(self)
