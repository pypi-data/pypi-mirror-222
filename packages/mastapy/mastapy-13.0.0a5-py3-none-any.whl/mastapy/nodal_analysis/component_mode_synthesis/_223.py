"""_223.py

CMSElementFaceGroup
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses import _179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'CMSElementFaceGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('CMSElementFaceGroup',)


class CMSElementFaceGroup(_179.ElementFaceGroup):
    """CMSElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP

    class _Cast_CMSElementFaceGroup:
        """Special nested class for casting CMSElementFaceGroup to subclasses."""

        def __init__(self, parent: 'CMSElementFaceGroup'):
            self._parent = parent

        @property
        def element_face_group(self):
            return self._parent._cast(_179.ElementFaceGroup)

        @property
        def fe_entity_group(self):
            from mastapy.nodal_analysis.dev_tools_analyses import _181
            from mastapy.fe_tools.vis_tools_global import _1229
            
            return self._parent._cast(_181.FEEntityGroup)

        @property
        def cms_element_face_group_of_all_free_faces(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _224
            
            return self._parent._cast(_224.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def cms_element_face_group(self) -> 'CMSElementFaceGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CMSElementFaceGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area(self) -> 'float':
        """float: 'Area' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Area

        if temp is None:
            return 0.0

        return temp

    def create_node_group(self):
        """ 'CreateNodeGroup' is the original name of this method."""

        self.wrapped.CreateNodeGroup()

    def populate_rms_values_cache(self):
        """ 'PopulateRMSValuesCache' is the original name of this method."""

        self.wrapped.PopulateRMSValuesCache()

    @property
    def cast_to(self) -> 'CMSElementFaceGroup._Cast_CMSElementFaceGroup':
        return self._Cast_CMSElementFaceGroup(self)
