"""_208.py

ElementPropertiesBeam
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_BEAM = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesBeam')

if TYPE_CHECKING:
    from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1230


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesBeam',)


class ElementPropertiesBeam(_215.ElementPropertiesWithMaterial):
    """ElementPropertiesBeam

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_BEAM

    class _Cast_ElementPropertiesBeam:
        """Special nested class for casting ElementPropertiesBeam to subclasses."""

        def __init__(self, parent: 'ElementPropertiesBeam'):
            self._parent = parent

        @property
        def element_properties_with_material(self):
            return self._parent._cast(_215.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _207
            
            return self._parent._cast(_207.ElementPropertiesBase)

        @property
        def element_properties_beam(self) -> 'ElementPropertiesBeam':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesBeam.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def section_dimensions(self) -> 'str':
        """str: 'SectionDimensions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionDimensions

        if temp is None:
            return ''

        return temp

    @property
    def section_type(self) -> '_1230.BeamSectionType':
        """BeamSectionType: 'SectionType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums.BeamSectionType')
        return constructor.new_from_mastapy('mastapy.fe_tools.vis_tools_global.vis_tools_global_enums._1230', 'BeamSectionType')(value) if value is not None else None

    @property
    def cast_to(self) -> 'ElementPropertiesBeam._Cast_ElementPropertiesBeam':
        return self._Cast_ElementPropertiesBeam(self)
