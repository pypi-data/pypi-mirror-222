﻿"""_4445.py

CoaxialConnectionCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CoaxialConnectionCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2252
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionCompoundParametricStudyTool',)


class CoaxialConnectionCompoundParametricStudyTool(_4518.ShaftToMountableComponentConnectionCompoundParametricStudyTool):
    """CoaxialConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_CoaxialConnectionCompoundParametricStudyTool:
        """Special nested class for casting CoaxialConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CoaxialConnectionCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            return self._parent._cast(_4518.ShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4424
            
            return self._parent._cast(_4424.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4456
            
            return self._parent._cast(_4456.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4465
            
            return self._parent._cast(_4465.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(self) -> 'CoaxialConnectionCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2252.CoaxialConnection':
        """CoaxialConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2252.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4298.CoaxialConnectionParametricStudyTool]':
        """List[CoaxialConnectionParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4298.CoaxialConnectionParametricStudyTool]':
        """List[CoaxialConnectionParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CoaxialConnectionCompoundParametricStudyTool._Cast_CoaxialConnectionCompoundParametricStudyTool':
        return self._Cast_CoaxialConnectionCompoundParametricStudyTool(self)
