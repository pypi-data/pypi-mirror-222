"""_6808.py

ConceptCouplingLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model import _2189
    from mastapy.math_utility import _1525
    from mastapy.system_model.part_model.couplings import _2563
    from mastapy.math_utility.control import _1567


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingLoadCase',)


class ConceptCouplingLoadCase(_6821.CouplingLoadCase):
    """ConceptCouplingLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_LOAD_CASE

    class _Cast_ConceptCouplingLoadCase:
        """Special nested class for casting ConceptCouplingLoadCase to subclasses."""

        def __init__(self, parent: 'ConceptCouplingLoadCase'):
            self._parent = parent

        @property
        def coupling_load_case(self):
            return self._parent._cast(_6821.CouplingLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractAssemblyLoadCase)

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
        def concept_coupling_load_case(self) -> 'ConceptCouplingLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Efficiency' is the original name of this property."""

        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @efficiency.setter
    def efficiency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Efficiency = value

    @property
    def power_load_for_reference_speed(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'PowerLoadForReferenceSpeed' is the original name of this property."""

        temp = self.wrapped.PowerLoadForReferenceSpeed

        if temp is None:
            return None

        return constructor.new_from_mastapy('mastapy._internal.implicit.list_with_selected_item', 'ListWithSelectedItem_PowerLoad')(temp) if temp is not None else None

    @power_load_for_reference_speed.setter
    def power_load_for_reference_speed(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.PowerLoadForReferenceSpeed = value

    @property
    def speed_ratio(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SpeedRatio' is the original name of this property."""

        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @speed_ratio.setter
    def speed_ratio(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SpeedRatio = value

    @property
    def speed_ratio_specification_method(self) -> '_2189.ConceptCouplingSpeedRatioSpecificationMethod':
        """ConceptCouplingSpeedRatioSpecificationMethod: 'SpeedRatioSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.SpeedRatioSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.SystemModel.ConceptCouplingSpeedRatioSpecificationMethod')
        return constructor.new_from_mastapy('mastapy.system_model._2189', 'ConceptCouplingSpeedRatioSpecificationMethod')(value) if value is not None else None

    @speed_ratio_specification_method.setter
    def speed_ratio_specification_method(self, value: '_2189.ConceptCouplingSpeedRatioSpecificationMethod'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.SystemModel.ConceptCouplingSpeedRatioSpecificationMethod')
        self.wrapped.SpeedRatioSpecificationMethod = value

    @property
    def speed_ratio_vs_time(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'SpeedRatioVsTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioVsTime

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2563.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def speed_ratio_pid_control(self) -> '_1567.PIDControlSettings':
        """PIDControlSettings: 'SpeedRatioPIDControl' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioPIDControl

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConceptCouplingLoadCase._Cast_ConceptCouplingLoadCase':
        return self._Cast_ConceptCouplingLoadCase(self)
