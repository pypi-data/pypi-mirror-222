"""_162.py

MeshRequest
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_REQUEST = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'MeshRequest')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import _155, _156


__docformat__ = 'restructuredtext en'
__all__ = ('MeshRequest',)


class MeshRequest(_0.APIBase):
    """MeshRequest

    This is a mastapy class.
    """

    TYPE = _MESH_REQUEST

    class _Cast_MeshRequest:
        """Special nested class for casting MeshRequest to subclasses."""

        def __init__(self, parent: 'MeshRequest'):
            self._parent = parent

        @property
        def mesh_request(self) -> 'MeshRequest':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshRequest.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_face_group(self) -> 'bool':
        """bool: 'CADFaceGroup' is the original name of this property."""

        temp = self.wrapped.CADFaceGroup

        if temp is None:
            return False

        return temp

    @cad_face_group.setter
    def cad_face_group(self, value: 'bool'):
        self.wrapped.CADFaceGroup = bool(value) if value is not None else False

    @property
    def geometry_modeller_design_information(self) -> '_155.GeometryModellerDesignInformation':
        """GeometryModellerDesignInformation: 'GeometryModellerDesignInformation' is the original name of this property."""

        temp = self.wrapped.GeometryModellerDesignInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @geometry_modeller_design_information.setter
    def geometry_modeller_design_information(self, value: '_155.GeometryModellerDesignInformation'):
        self.wrapped.GeometryModellerDesignInformation = value

    @property
    def moniker(self) -> 'str':
        """str: 'Moniker' is the original name of this property."""

        temp = self.wrapped.Moniker

        if temp is None:
            return ''

        return temp

    @moniker.setter
    def moniker(self, value: 'str'):
        self.wrapped.Moniker = str(value) if value is not None else ''

    def geometry_modeller_dimensions(self) -> 'Dict[str, _156.GeometryModellerDimension]':
        """ 'GeometryModellerDimensions' is the original name of this method.

        Returns:
            Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension]
        """

        method_result = self.wrapped.GeometryModellerDimensions()
        return method_result

    @property
    def cast_to(self) -> 'MeshRequest._Cast_MeshRequest':
        return self._Cast_MeshRequest(self)
