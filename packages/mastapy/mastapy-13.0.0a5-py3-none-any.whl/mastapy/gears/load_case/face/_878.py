"""_878.py

FaceMeshLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.load_case import _872
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Face', 'FaceMeshLoadCase')

if TYPE_CHECKING:
    from mastapy.gears import _322


__docformat__ = 'restructuredtext en'
__all__ = ('FaceMeshLoadCase',)


class FaceMeshLoadCase(_872.MeshLoadCase):
    """FaceMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_MESH_LOAD_CASE

    class _Cast_FaceMeshLoadCase:
        """Special nested class for casting FaceMeshLoadCase to subclasses."""

        def __init__(self, parent: 'FaceMeshLoadCase'):
            self._parent = parent

        @property
        def mesh_load_case(self):
            return self._parent._cast(_872.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def face_mesh_load_case(self) -> 'FaceMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_misalignment_due_to_system_deflection(self) -> 'float':
        """float: 'EquivalentMisalignmentDueToSystemDeflection' is the original name of this property."""

        temp = self.wrapped.EquivalentMisalignmentDueToSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment_due_to_system_deflection.setter
    def equivalent_misalignment_due_to_system_deflection(self, value: 'float'):
        self.wrapped.EquivalentMisalignmentDueToSystemDeflection = float(value) if value is not None else 0.0

    @property
    def misalignment_source(self) -> '_322.CylindricalMisalignmentDataSource':
        """CylindricalMisalignmentDataSource: 'MisalignmentSource' is the original name of this property."""

        temp = self.wrapped.MisalignmentSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource')
        return constructor.new_from_mastapy('mastapy.gears._322', 'CylindricalMisalignmentDataSource')(value) if value is not None else None

    @misalignment_source.setter
    def misalignment_source(self, value: '_322.CylindricalMisalignmentDataSource'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource')
        self.wrapped.MisalignmentSource = value

    @property
    def cast_to(self) -> 'FaceMeshLoadCase._Cast_FaceMeshLoadCase':
        return self._Cast_FaceMeshLoadCase(self)
