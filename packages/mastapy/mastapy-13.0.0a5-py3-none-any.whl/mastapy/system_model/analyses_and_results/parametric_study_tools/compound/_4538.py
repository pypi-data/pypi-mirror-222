﻿"""_4538.py

TorqueConverterCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4458
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'TorqueConverterCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterCompoundParametricStudyTool',)


class TorqueConverterCompoundParametricStudyTool(_4458.CouplingCompoundParametricStudyTool):
    """TorqueConverterCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_TorqueConverterCompoundParametricStudyTool:
        """Special nested class for casting TorqueConverterCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'TorqueConverterCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def coupling_compound_parametric_study_tool(self):
            return self._parent._cast(_4458.CouplingCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4519
            
            return self._parent._cast(_4519.SpecialisedAssemblyCompoundParametricStudyTool)

        @property
        def abstract_assembly_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4421
            
            return self._parent._cast(_4421.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4500
            
            return self._parent._cast(_4500.PartCompoundParametricStudyTool)

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
        def torque_converter_compound_parametric_study_tool(self) -> 'TorqueConverterCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2589.TorqueConverter':
        """TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2589.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4410.TorqueConverterParametricStudyTool]':
        """List[TorqueConverterParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4410.TorqueConverterParametricStudyTool]':
        """List[TorqueConverterParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterCompoundParametricStudyTool._Cast_TorqueConverterCompoundParametricStudyTool':
        return self._Cast_TorqueConverterCompoundParametricStudyTool(self)
