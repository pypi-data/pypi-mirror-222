"""_211.py

ElementPropertiesRigid
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _207
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_RIGID = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesRigid')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _219


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesRigid',)


class ElementPropertiesRigid(_207.ElementPropertiesBase):
    """ElementPropertiesRigid

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_RIGID

    class _Cast_ElementPropertiesRigid:
        """Special nested class for casting ElementPropertiesRigid to subclasses."""

        def __init__(self, parent: 'ElementPropertiesRigid'):
            self._parent = parent

        @property
        def element_properties_base(self):
            return self._parent._cast(_207.ElementPropertiesBase)

        @property
        def element_properties_rigid(self) -> 'ElementPropertiesRigid':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesRigid.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_degree_of_freedom_inputs(self) -> 'int':
        """int: 'NumberOfDegreeOfFreedomInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfDegreeOfFreedomInputs

        if temp is None:
            return 0

        return temp

    @property
    def degrees_of_freedom_list(self) -> 'List[_219.RigidElementNodeDegreesOfFreedom]':
        """List[RigidElementNodeDegreesOfFreedom]: 'DegreesOfFreedomList' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreesOfFreedomList

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ElementPropertiesRigid._Cast_ElementPropertiesRigid':
        return self._Cast_ElementPropertiesRigid(self)
