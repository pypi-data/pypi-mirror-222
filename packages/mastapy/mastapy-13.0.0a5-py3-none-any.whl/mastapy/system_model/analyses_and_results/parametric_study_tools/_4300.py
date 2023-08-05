"""_4300.py

ConceptCouplingConnectionParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConceptCouplingConnectionParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6806
    from mastapy.system_model.analyses_and_results.system_deflections import _2699


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionParametricStudyTool',)


class ConceptCouplingConnectionParametricStudyTool(_4311.CouplingConnectionParametricStudyTool):
    """ConceptCouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_ConceptCouplingConnectionParametricStudyTool:
        """Special nested class for casting ConceptCouplingConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def coupling_connection_parametric_study_tool(self):
            return self._parent._cast(_4311.CouplingConnectionParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
            
            return self._parent._cast(_4346.InterMountableComponentConnectionParametricStudyTool)

        @property
        def connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4309
            
            return self._parent._cast(_4309.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2631
            
            return self._parent._cast(_2631.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_parametric_study_tool(self) -> 'ConceptCouplingConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6806.ConceptCouplingConnectionLoadCase':
        """ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2699.ConceptCouplingConnectionSystemDeflection]':
        """List[ConceptCouplingConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptCouplingConnectionParametricStudyTool._Cast_ConceptCouplingConnectionParametricStudyTool':
        return self._Cast_ConceptCouplingConnectionParametricStudyTool(self)
