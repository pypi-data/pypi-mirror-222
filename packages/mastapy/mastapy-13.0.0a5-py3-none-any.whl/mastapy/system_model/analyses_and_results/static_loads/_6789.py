"""_6789.py

BeltDriveLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltDriveLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2558


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveLoadCase',)


class BeltDriveLoadCase(_6920.SpecialisedAssemblyLoadCase):
    """BeltDriveLoadCase

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_LOAD_CASE

    class _Cast_BeltDriveLoadCase:
        """Special nested class for casting BeltDriveLoadCase to subclasses."""

        def __init__(self, parent: 'BeltDriveLoadCase'):
            self._parent = parent

        @property
        def specialised_assembly_load_case(self):
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
        def cvt_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6823
            
            return self._parent._cast(_6823.CVTLoadCase)

        @property
        def belt_drive_load_case(self) -> 'BeltDriveLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pre_tension(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PreTension' is the original name of this property."""

        temp = self.wrapped.PreTension

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @pre_tension.setter
    def pre_tension(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PreTension = value

    @property
    def assembly_design(self) -> '_2558.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltDriveLoadCase._Cast_BeltDriveLoadCase':
        return self._Cast_BeltDriveLoadCase(self)
