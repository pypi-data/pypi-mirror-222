"""_4382.py

RingPinsToDiscConnectionParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'RingPinsToDiscConnectionParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2324
    from mastapy.system_model.analyses_and_results.static_loads import _6912
    from mastapy.system_model.analyses_and_results.system_deflections import _2777


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionParametricStudyTool',)


class RingPinsToDiscConnectionParametricStudyTool(_4346.InterMountableComponentConnectionParametricStudyTool):
    """RingPinsToDiscConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_RingPinsToDiscConnectionParametricStudyTool:
        """Special nested class for casting RingPinsToDiscConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'RingPinsToDiscConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
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
        def ring_pins_to_disc_connection_parametric_study_tool(self) -> 'RingPinsToDiscConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2324.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6912.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2777.RingPinsToDiscConnectionSystemDeflection]':
        """List[RingPinsToDiscConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RingPinsToDiscConnectionParametricStudyTool._Cast_RingPinsToDiscConnectionParametricStudyTool':
        return self._Cast_RingPinsToDiscConnectionParametricStudyTool(self)
