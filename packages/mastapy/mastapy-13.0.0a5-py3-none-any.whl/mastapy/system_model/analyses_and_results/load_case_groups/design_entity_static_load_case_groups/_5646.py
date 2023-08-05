"""_5646.py

ComponentStaticLoadCaseGroup
"""
from __future__ import annotations

from typing import (
    TYPE_CHECKING, List, TypeVar, Generic
)

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5650
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'ComponentStaticLoadCaseGroup')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2427
    from mastapy.system_model.analyses_and_results.static_loads import _6805


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentStaticLoadCaseGroup',)


TReal = TypeVar('TReal', bound='_2427.Component')
TComponentStaticLoad = TypeVar('TComponentStaticLoad', bound='_6805.ComponentLoadCase')


class ComponentStaticLoadCaseGroup(_5650.PartStaticLoadCaseGroup, Generic[TReal, TComponentStaticLoad]):
    """ComponentStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TReal
        TComponentStaticLoad
    """

    TYPE = _COMPONENT_STATIC_LOAD_CASE_GROUP

    class _Cast_ComponentStaticLoadCaseGroup:
        """Special nested class for casting ComponentStaticLoadCaseGroup to subclasses."""

        def __init__(self, parent: 'ComponentStaticLoadCaseGroup'):
            self._parent = parent

        @property
        def part_static_load_case_group(self):
            return self._parent._cast(_5650.PartStaticLoadCaseGroup)

        @property
        def design_entity_static_load_case_group(self):
            from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5648
            
            return self._parent._cast(_5648.DesignEntityStaticLoadCaseGroup)

        @property
        def component_static_load_case_group(self) -> 'ComponentStaticLoadCaseGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ComponentStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TReal':
        """TReal: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component(self) -> 'TReal':
        """TReal: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TComponentStaticLoad]':
        """List[TComponentStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_load_cases(self) -> 'List[TComponentStaticLoad]':
        """List[TComponentStaticLoad]: 'ComponentLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ComponentStaticLoadCaseGroup._Cast_ComponentStaticLoadCaseGroup':
        return self._Cast_ComponentStaticLoadCaseGroup(self)
