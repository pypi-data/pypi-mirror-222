"""_6806.py

ConceptCouplingConnectionLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6819
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingConnectionLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2327


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionLoadCase',)


class ConceptCouplingConnectionLoadCase(_6819.CouplingConnectionLoadCase):
    """ConceptCouplingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_LOAD_CASE

    class _Cast_ConceptCouplingConnectionLoadCase:
        """Special nested class for casting ConceptCouplingConnectionLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptCouplingConnectionLoadCase'):
            self._parent = parent

        @property
        def coupling_connection_load_case(self):
            return self._parent._cast(_6819.CouplingConnectionLoadCase)

        @property
        def inter_mountable_component_connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6879
            
            return self._parent._cast(_6879.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6817
            
            return self._parent._cast(_6817.ConnectionLoadCase)

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
        def concept_coupling_connection_load_case(self) -> 'ConceptCouplingConnectionLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionLoadCase.TYPE'):
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
    def cast_to(self) -> 'ConceptCouplingConnectionLoadCase._Cast_ConceptCouplingConnectionLoadCase':
        return self._Cast_ConceptCouplingConnectionLoadCase(self)
