"""_2830.py

RigidlyConnectedComponentGroupSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results import _2634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting', 'RigidlyConnectedComponentGroupSystemDeflection')

if TYPE_CHECKING:
    from mastapy.math_utility import _1508
    from mastapy.system_model.analyses_and_results.system_deflections import _2697


__docformat__ = 'restructuredtext en'
__all__ = ('RigidlyConnectedComponentGroupSystemDeflection',)


class RigidlyConnectedComponentGroupSystemDeflection(_2634.DesignEntityGroupAnalysis):
    """RigidlyConnectedComponentGroupSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION

    class _Cast_RigidlyConnectedComponentGroupSystemDeflection:
        """Special nested class for casting RigidlyConnectedComponentGroupSystemDeflection to subclasses."""

        def __init__(self, parent: 'RigidlyConnectedComponentGroupSystemDeflection'):
            self._parent = parent

        @property
        def design_entity_group_analysis(self):
            return self._parent._cast(_2634.DesignEntityGroupAnalysis)

        @property
        def rigidly_connected_component_group_system_deflection(self) -> 'RigidlyConnectedComponentGroupSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RigidlyConnectedComponentGroupSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_properties(self) -> '_1508.MassProperties':
        """MassProperties: 'MassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def components(self) -> 'List[_2697.ComponentSystemDeflection]':
        """List[ComponentSystemDeflection]: 'Components' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Components

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection':
        return self._Cast_RigidlyConnectedComponentGroupSystemDeflection(self)
