﻿"""_4276.py

AbstractShaftParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'AbstractShaftParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2418


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftParametricStudyTool',)


class AbstractShaftParametricStudyTool(_4275.AbstractShaftOrHousingParametricStudyTool):
    """AbstractShaftParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_PARAMETRIC_STUDY_TOOL

    class _Cast_AbstractShaftParametricStudyTool:
        """Special nested class for casting AbstractShaftParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AbstractShaftParametricStudyTool'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_parametric_study_tool(self):
            return self._parent._cast(_4275.AbstractShaftOrHousingParametricStudyTool)

        @property
        def component_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartParametricStudyTool)

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
        def cycloidal_disc_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
            
            return self._parent._cast(_4319.CycloidalDiscParametricStudyTool)

        @property
        def shaft_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4388
            
            return self._parent._cast(_4388.ShaftParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(self) -> 'AbstractShaftParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2418.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftParametricStudyTool._Cast_AbstractShaftParametricStudyTool':
        return self._Cast_AbstractShaftParametricStudyTool(self)
