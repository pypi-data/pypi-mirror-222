"""_2642.py

CompoundAdvancedTimeSteppingAnalysisForModulation
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results import _2601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedTimeSteppingAnalysisForModulation',)


class CompoundAdvancedTimeSteppingAnalysisForModulation(_2601.CompoundAnalysis):
    """CompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_CompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'CompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2601.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7519
            
            return self._parent._cast(_7519.MarshalByRefObjectPermanent)

        @property
        def compound_advanced_time_stepping_analysis_for_modulation(self) -> 'CompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_CompoundAdvancedTimeSteppingAnalysisForModulation(self)
