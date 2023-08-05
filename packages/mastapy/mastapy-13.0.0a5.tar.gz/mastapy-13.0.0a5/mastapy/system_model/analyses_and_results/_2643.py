"""_2643.py

CompoundCriticalSpeedAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results import _2601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundCriticalSpeedAnalysis',)


class CompoundCriticalSpeedAnalysis(_2601.CompoundAnalysis):
    """CompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_CompoundCriticalSpeedAnalysis:
        """Special nested class for casting CompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'CompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def compound_analysis(self):
            return self._parent._cast(_2601.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7519
            
            return self._parent._cast(_7519.MarshalByRefObjectPermanent)

        @property
        def compound_critical_speed_analysis(self) -> 'CompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis':
        return self._Cast_CompoundCriticalSpeedAnalysis(self)
