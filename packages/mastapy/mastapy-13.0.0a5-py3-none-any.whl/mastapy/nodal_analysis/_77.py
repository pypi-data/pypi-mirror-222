"""_77.py

MeshingOptions
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.nodal_analysis import _61
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESHING_OPTIONS = python_net_import('SMT.MastaAPI.NodalAnalysis', 'MeshingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshingOptions',)


class MeshingOptions(_61.FEMeshingOptions):
    """MeshingOptions

    This is a mastapy class.
    """

    TYPE = _MESHING_OPTIONS

    class _Cast_MeshingOptions:
        """Special nested class for casting MeshingOptions to subclasses."""

        def __init__(self, parent: 'MeshingOptions'):
            self._parent = parent

        @property
        def fe_meshing_options(self):
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def meshing_options(self) -> 'MeshingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementSize' is the original name of this property."""

        temp = self.wrapped.ElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @element_size.setter
    def element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementSize = value

    @property
    def cast_to(self) -> 'MeshingOptions._Cast_MeshingOptions':
        return self._Cast_MeshingOptions(self)
