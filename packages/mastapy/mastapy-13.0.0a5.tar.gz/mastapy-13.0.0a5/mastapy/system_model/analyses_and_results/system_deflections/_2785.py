"""_2785.py

ShaftSectionSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _126
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ShaftSectionSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2784


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSectionSystemDeflection',)


class ShaftSectionSystemDeflection(_126.Bar):
    """ShaftSectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_SYSTEM_DEFLECTION

    class _Cast_ShaftSectionSystemDeflection:
        """Special nested class for casting ShaftSectionSystemDeflection to subclasses."""

        def __init__(self, parent: 'ShaftSectionSystemDeflection'):
            self._parent = parent

        @property
        def bar(self):
            return self._parent._cast(_126.Bar)

        @property
        def nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def shaft_section_system_deflection(self) -> 'ShaftSectionSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftSectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_end(self) -> '_2784.ShaftSectionEndResultsSystemDeflection':
        """ShaftSectionEndResultsSystemDeflection: 'LeftEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_end(self) -> '_2784.ShaftSectionEndResultsSystemDeflection':
        """ShaftSectionEndResultsSystemDeflection: 'RightEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection':
        return self._Cast_ShaftSectionSystemDeflection(self)
