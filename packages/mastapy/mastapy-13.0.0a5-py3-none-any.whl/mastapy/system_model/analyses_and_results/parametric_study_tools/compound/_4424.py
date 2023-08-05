"""_4424.py

AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4456
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4277


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool',)


class AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool(_4456.ConnectionCompoundParametricStudyTool):
    """AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def connection_compound_parametric_study_tool(self):
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
        def coaxial_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4445
            
            return self._parent._cast(_4445.CoaxialConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4465
            
            return self._parent._cast(_4465.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4467
            
            return self._parent._cast(_4467.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool)

        @property
        def planetary_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4504
            
            return self._parent._cast(_4504.PlanetaryConnectionCompoundParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4518
            
            return self._parent._cast(_4518.ShaftToMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(self) -> 'AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4277.AbstractShaftToMountableComponentConnectionParametricStudyTool]':
        """List[AbstractShaftToMountableComponentConnectionParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4277.AbstractShaftToMountableComponentConnectionParametricStudyTool]':
        """List[AbstractShaftToMountableComponentConnectionParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool':
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool(self)
