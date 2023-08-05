﻿"""_4755.py

DatumCompoundModalAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4729
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'DatumCompoundModalAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2431
    from mastapy.system_model.analyses_and_results.modal_analyses import _4602


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundModalAnalysis',)


class DatumCompoundModalAnalysis(_4729.ComponentCompoundModalAnalysis):
    """DatumCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MODAL_ANALYSIS

    class _Cast_DatumCompoundModalAnalysis:
        """Special nested class for casting DatumCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'DatumCompoundModalAnalysis'):
            self._parent = parent

        @property
        def component_compound_modal_analysis(self):
            return self._parent._cast(_4729.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4783
            
            return self._parent._cast(_4783.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def datum_compound_modal_analysis(self) -> 'DatumCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatumCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2431.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4602.DatumModalAnalysis]':
        """List[DatumModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4602.DatumModalAnalysis]':
        """List[DatumModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis':
        return self._Cast_DatumCompoundModalAnalysis(self)
