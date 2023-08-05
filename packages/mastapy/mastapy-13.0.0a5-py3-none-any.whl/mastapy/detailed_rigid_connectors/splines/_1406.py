"""_1406.py

SplineMaterial
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.materials import _267
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_MATERIAL = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'SplineMaterial')

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1388


__docformat__ = 'restructuredtext en'
__all__ = ('SplineMaterial',)


class SplineMaterial(_267.Material):
    """SplineMaterial

    This is a mastapy class.
    """

    TYPE = _SPLINE_MATERIAL

    class _Cast_SplineMaterial:
        """Special nested class for casting SplineMaterial to subclasses."""

        def __init__(self, parent: 'SplineMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_267.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1818
            
            return self._parent._cast(_1818.NamedDatabaseItem)

        @property
        def spline_material(self) -> 'SplineMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SplineMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def core_hardness_h_rc(self) -> 'float':
        """float: 'CoreHardnessHRc' is the original name of this property."""

        temp = self.wrapped.CoreHardnessHRc

        if temp is None:
            return 0.0

        return temp

    @core_hardness_h_rc.setter
    def core_hardness_h_rc(self, value: 'float'):
        self.wrapped.CoreHardnessHRc = float(value) if value is not None else 0.0

    @property
    def heat_treatment_type(self) -> '_1388.HeatTreatmentTypes':
        """HeatTreatmentTypes: 'HeatTreatmentType' is the original name of this property."""

        temp = self.wrapped.HeatTreatmentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.DetailedRigidConnectors.Splines.HeatTreatmentTypes')
        return constructor.new_from_mastapy('mastapy.detailed_rigid_connectors.splines._1388', 'HeatTreatmentTypes')(value) if value is not None else None

    @heat_treatment_type.setter
    def heat_treatment_type(self, value: '_1388.HeatTreatmentTypes'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.DetailedRigidConnectors.Splines.HeatTreatmentTypes')
        self.wrapped.HeatTreatmentType = value

    @property
    def cast_to(self) -> 'SplineMaterial._Cast_SplineMaterial':
        return self._Cast_SplineMaterial(self)
