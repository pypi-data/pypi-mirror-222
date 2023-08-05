"""_5645.py

AbstractAssemblyStaticLoadCaseGroup
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'AbstractAssemblyStaticLoadCaseGroup')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2417
    from mastapy.system_model.analyses_and_results.static_loads import _6774


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyStaticLoadCaseGroup',)


TAssembly = TypeVar('TAssembly', bound='_2417.AbstractAssembly')
TAssemblyStaticLoad = TypeVar('TAssemblyStaticLoad', bound='_6774.AbstractAssemblyLoadCase')


class AbstractAssemblyStaticLoadCaseGroup(_5650.PartStaticLoadCaseGroup, Generic[TAssembly, TAssemblyStaticLoad]):
    """AbstractAssemblyStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TAssembly
        TAssemblyStaticLoad
    """

    TYPE = _ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP

    class _Cast_AbstractAssemblyStaticLoadCaseGroup:
        """Special nested class for casting AbstractAssemblyStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def part_static_load_case_group(self):
            return self._parent._cast(_5650.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5648
            
            return self._parent._cast(_5648.DesignEntityStaticLoadCaseGroup)

        @property
        def abstract_assembly_static_load_case_group(self) -> 'AbstractAssemblyStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TAssembly':
        """TAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly(self) -> 'TAssembly':
        """TAssembly: 'Assembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Assembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TAssemblyStaticLoad]':
        """List[TAssemblyStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_load_cases(self) -> 'List[TAssemblyStaticLoad]':
        """List[TAssemblyStaticLoad]: 'AssemblyLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyStaticLoadCaseGroup._Cast_AbstractAssemblyStaticLoadCaseGroup':
        return self._Cast_AbstractAssemblyStaticLoadCaseGroup(self)
