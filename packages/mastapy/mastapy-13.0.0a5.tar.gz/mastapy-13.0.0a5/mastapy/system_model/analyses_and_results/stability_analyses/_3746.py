﻿"""_3746.py

AbstractShaftOrHousingStabilityAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'AbstractShaftOrHousingStabilityAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2419


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingStabilityAnalysis',)


class AbstractShaftOrHousingStabilityAnalysis(_3770.ComponentStabilityAnalysis):
    """AbstractShaftOrHousingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS

    class _Cast_AbstractShaftOrHousingStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingStabilityAnalysis'):
            self._parent = parent

        @property
        def component_stability_analysis(self):
            return self._parent._cast(_3770.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3825
            
            return self._parent._cast(_3825.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def abstract_shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3747
            
            return self._parent._cast(_3747.AbstractShaftStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3792
            
            return self._parent._cast(_3792.CycloidalDiscStabilityAnalysis)

        @property
        def fe_part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3802
            
            return self._parent._cast(_3802.FEPartStabilityAnalysis)

        @property
        def shaft_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3842
            
            return self._parent._cast(_3842.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(self) -> 'AbstractShaftOrHousingStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2419.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis':
        return self._Cast_AbstractShaftOrHousingStabilityAnalysis(self)
