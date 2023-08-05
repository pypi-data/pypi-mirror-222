"""_4313.py

CouplingParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CouplingParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2565


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingParametricStudyTool',)


class CouplingParametricStudyTool(_4390.SpecialisedAssemblyParametricStudyTool):
    """CouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_PARAMETRIC_STUDY_TOOL

    class _Cast_CouplingParametricStudyTool:
        """Special nested class for casting CouplingParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CouplingParametricStudyTool'):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(self):
            return self._parent._cast(_4390.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4274
            
            return self._parent._cast(_4274.AbstractAssemblyParametricStudyTool)

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
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
            
            return self._parent._cast(_4302.ConceptCouplingParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4374
            
            return self._parent._cast(_4374.PartToPartShearCouplingParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
            
            return self._parent._cast(_4396.SpringDamperParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
            
            return self._parent._cast(_4410.TorqueConverterParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self) -> 'CouplingParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2565.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingParametricStudyTool._Cast_CouplingParametricStudyTool':
        return self._Cast_CouplingParametricStudyTool(self)
