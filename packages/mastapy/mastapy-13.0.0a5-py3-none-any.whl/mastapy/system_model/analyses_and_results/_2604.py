"""_2604.py

AdvancedSystemDeflectionSubAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.system_model.analyses_and_results import _2602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'AdvancedSystemDeflectionSubAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedSystemDeflectionSubAnalysis',)


class AdvancedSystemDeflectionSubAnalysis(_2602.SingleAnalysis):
    """AdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS

    class _Cast_AdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting AdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(self, parent: 'AdvancedSystemDeflectionSubAnalysis'):
            self._parent = parent

        @property
        def single_analysis(self):
            return self._parent._cast(_2602.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self):
            from mastapy import _7519
            
            return self._parent._cast(_7519.MarshalByRefObjectPermanent)

        @property
        def advanced_system_deflection_sub_analysis(self) -> 'AdvancedSystemDeflectionSubAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AdvancedSystemDeflectionSubAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis':
        return self._Cast_AdvancedSystemDeflectionSubAnalysis(self)
