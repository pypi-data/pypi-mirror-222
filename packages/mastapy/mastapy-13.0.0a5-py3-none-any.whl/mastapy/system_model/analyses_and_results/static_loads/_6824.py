"""_6824.py

CVTPulleyLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTPulleyLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2569


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyLoadCase',)


class CVTPulleyLoadCase(_6908.PulleyLoadCase):
    """CVTPulleyLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_LOAD_CASE

    class _Cast_CVTPulleyLoadCase:
        """Special nested class for casting CVTPulleyLoadCase to subclasses."""

        def __init__(self, parent: 'CVTPulleyLoadCase'):
            self._parent = parent

        @property
        def pulley_load_case(self):
            return self._parent._cast(_6908.PulleyLoadCase)

        @property
        def coupling_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6820
            
            return self._parent._cast(_6820.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.MountableComponentLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6805
            
            return self._parent._cast(_6805.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PartLoadCase)

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
        def cvt_pulley_load_case(self) -> 'CVTPulleyLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTPulleyLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clamping_force(self) -> 'float':
        """float: 'ClampingForce' is the original name of this property."""

        temp = self.wrapped.ClampingForce

        if temp is None:
            return 0.0

        return temp

    @clamping_force.setter
    def clamping_force(self, value: 'float'):
        self.wrapped.ClampingForce = float(value) if value is not None else 0.0

    @property
    def effective_diameter(self) -> 'float':
        """float: 'EffectiveDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_nodes(self) -> 'int':
        """int: 'NumberOfNodes' is the original name of this property."""

        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @number_of_nodes.setter
    def number_of_nodes(self, value: 'int'):
        self.wrapped.NumberOfNodes = int(value) if value is not None else 0

    @property
    def component_design(self) -> '_2569.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTPulleyLoadCase._Cast_CVTPulleyLoadCase':
        return self._Cast_CVTPulleyLoadCase(self)
