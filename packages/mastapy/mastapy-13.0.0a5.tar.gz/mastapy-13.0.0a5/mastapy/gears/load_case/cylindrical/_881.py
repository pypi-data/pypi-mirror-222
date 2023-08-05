"""_881.py

CylindricalMeshLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.load_case import _872
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Cylindrical', 'CylindricalMeshLoadCase')

if TYPE_CHECKING:
    from mastapy.gears import _321, _322
    from mastapy.gears.gear_designs.cylindrical import _1055


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshLoadCase',)


class CylindricalMeshLoadCase(_872.MeshLoadCase):
    """CylindricalMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_CASE

    class _Cast_CylindricalMeshLoadCase:
        """Special nested class for casting CylindricalMeshLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalMeshLoadCase'):
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
        def cylindrical_mesh_load_case(self) -> 'CylindricalMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_321.CylindricalFlanks':
        """CylindricalFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.Gears.CylindricalFlanks')
        return constructor.new_from_mastapy('mastapy.gears._321', 'CylindricalFlanks')(value) if value is not None else None

    @property
    def equivalent_misalignment(self) -> 'float':
        """float: 'EquivalentMisalignment' is the original name of this property."""

        temp = self.wrapped.EquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment.setter
    def equivalent_misalignment(self, value: 'float'):
        self.wrapped.EquivalentMisalignment = float(value) if value is not None else 0.0

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
    def misalignment_due_to_micro_geometry_lead_relief(self) -> 'float':
        """float: 'MisalignmentDueToMicroGeometryLeadRelief' is the original name of this property."""

        temp = self.wrapped.MisalignmentDueToMicroGeometryLeadRelief

        if temp is None:
            return 0.0

        return temp

    @misalignment_due_to_micro_geometry_lead_relief.setter
    def misalignment_due_to_micro_geometry_lead_relief(self, value: 'float'):
        self.wrapped.MisalignmentDueToMicroGeometryLeadRelief = float(value) if value is not None else 0.0

    @property
    def pitch_line_velocity_at_operating_pitch_diameter(self) -> 'float':
        """float: 'PitchLineVelocityAtOperatingPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityAtOperatingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_modifiable_settings(self) -> '_1055.LTCALoadCaseModifiableSettings':
        """LTCALoadCaseModifiableSettings: 'LoadCaseModifiableSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseModifiableSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase':
        return self._Cast_CylindricalMeshLoadCase(self)
