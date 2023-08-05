﻿"""_2620.py

ModalAnalysisForHarmonicAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results import _2602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'ModalAnalysisForHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisForHarmonicAnalysis',)


class ModalAnalysisForHarmonicAnalysis(_2602.SingleAnalysis):
    """ModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS

    class _Cast_ModalAnalysisForHarmonicAnalysis:
        """Special nested class for casting ModalAnalysisForHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'ModalAnalysisForHarmonicAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2602.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7519
            
            return self._parent._cast(_7519.MarshalByRefObjectPermanent)

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
    def cast_to(self) -> 'ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis':
        return self._Cast_ModalAnalysisForHarmonicAnalysis(self)
