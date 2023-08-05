"""_2565.py

Coupling
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2566


__docformat__ = 'restructuredtext en'
__all__ = ('Coupling',)


class Coupling(_2459.SpecialisedAssembly):
    """Coupling

    This is a mastapy class.
    """

    TYPE = _COUPLING

    class _Cast_Coupling:
        """Special nested class for casting Coupling to subclasses."""

        def __init__(self, parent: 'Coupling'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def clutch(self):
            from mastapy.system_model.part_model.couplings import _2560
            
            return self._parent._cast(_2560.Clutch)

        @property
        def concept_coupling(self):
            from mastapy.system_model.part_model.couplings import _2563
            
            return self._parent._cast(_2563.ConceptCoupling)

        @property
        def part_to_part_shear_coupling(self):
            from mastapy.system_model.part_model.couplings import _2570
            
            return self._parent._cast(_2570.PartToPartShearCoupling)

        @property
        def spring_damper(self):
            from mastapy.system_model.part_model.couplings import _2582
            
            return self._parent._cast(_2582.SpringDamper)

        @property
        def torque_converter(self):
            from mastapy.system_model.part_model.couplings import _2589
            
            return self._parent._cast(_2589.TorqueConverter)

        @property
        def coupling(self) -> 'Coupling':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Coupling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property."""

        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    def axial_stiffness(self, value: 'float'):
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def radial_stiffness(self) -> 'float':
        """float: 'RadialStiffness' is the original name of this property."""

        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    def radial_stiffness(self, value: 'float'):
        self.wrapped.RadialStiffness = float(value) if value is not None else 0.0

    @property
    def tilt_stiffness(self) -> 'float':
        """float: 'TiltStiffness' is the original name of this property."""

        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    def tilt_stiffness(self, value: 'float'):
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def torsional_stiffness(self) -> 'float':
        """float: 'TorsionalStiffness' is the original name of this property."""

        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'float'):
        self.wrapped.TorsionalStiffness = float(value) if value is not None else 0.0

    @property
    def halves(self) -> 'List[_2566.CouplingHalf]':
        """List[CouplingHalf]: 'Halves' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Halves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def half_a(self) -> '_2566.CouplingHalf':
        """CouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b(self) -> '_2566.CouplingHalf':
        """CouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Coupling._Cast_Coupling':
        return self._Cast_Coupling(self)
