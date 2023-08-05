"""_2563.py

ConceptCoupling
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.part_model.couplings import _2565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _54
    from mastapy.math_utility import _1525


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCoupling',)


class ConceptCoupling(_2565.Coupling):
    """ConceptCoupling

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING

    class _Cast_ConceptCoupling:
        """Special nested class for casting ConceptCoupling to subclasses."""

        def __init__(self, parent: 'ConceptCoupling'):
            self._parent = parent

        @property
        def coupling(self):
            return self._parent._cast(_2565.Coupling)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2459
            
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
        def concept_coupling(self) -> 'ConceptCoupling':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCoupling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coupling_type(self) -> '_54.CouplingType':
        """CouplingType: 'CouplingType' is the original name of this property."""

        temp = self.wrapped.CouplingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, 'SMT.MastaAPI.NodalAnalysis.CouplingType')
        return constructor.new_from_mastapy('mastapy.nodal_analysis._54', 'CouplingType')(value) if value is not None else None

    @coupling_type.setter
    def coupling_type(self, value: '_54.CouplingType'):
        value = conversion.mp_to_pn_enum(value, 'SMT.MastaAPI.NodalAnalysis.CouplingType')
        self.wrapped.CouplingType = value

    @property
    def default_efficiency(self) -> 'float':
        """float: 'DefaultEfficiency' is the original name of this property."""

        temp = self.wrapped.DefaultEfficiency

        if temp is None:
            return 0.0

        return temp

    @default_efficiency.setter
    def default_efficiency(self, value: 'float'):
        self.wrapped.DefaultEfficiency = float(value) if value is not None else 0.0

    @property
    def default_speed_ratio(self) -> 'float':
        """float: 'DefaultSpeedRatio' is the original name of this property."""

        temp = self.wrapped.DefaultSpeedRatio

        if temp is None:
            return 0.0

        return temp

    @default_speed_ratio.setter
    def default_speed_ratio(self, value: 'float'):
        self.wrapped.DefaultSpeedRatio = float(value) if value is not None else 0.0

    @property
    def display_tilt_in_2d_drawing(self) -> 'bool':
        """bool: 'DisplayTiltIn2DDrawing' is the original name of this property."""

        temp = self.wrapped.DisplayTiltIn2DDrawing

        if temp is None:
            return False

        return temp

    @display_tilt_in_2d_drawing.setter
    def display_tilt_in_2d_drawing(self, value: 'bool'):
        self.wrapped.DisplayTiltIn2DDrawing = bool(value) if value is not None else False

    @property
    def efficiency_vs_speed_ratio(self) -> '_1525.Vector2DListAccessor':
        """Vector2DListAccessor: 'EfficiencyVsSpeedRatio' is the original name of this property."""

        temp = self.wrapped.EfficiencyVsSpeedRatio

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @efficiency_vs_speed_ratio.setter
    def efficiency_vs_speed_ratio(self, value: '_1525.Vector2DListAccessor'):
        self.wrapped.EfficiencyVsSpeedRatio = value

    @property
    def halves_are_coincident(self) -> 'bool':
        """bool: 'HalvesAreCoincident' is the original name of this property."""

        temp = self.wrapped.HalvesAreCoincident

        if temp is None:
            return False

        return temp

    @halves_are_coincident.setter
    def halves_are_coincident(self, value: 'bool'):
        self.wrapped.HalvesAreCoincident = bool(value) if value is not None else False

    @property
    def specify_efficiency_vs_speed_ratio(self) -> 'bool':
        """bool: 'SpecifyEfficiencyVsSpeedRatio' is the original name of this property."""

        temp = self.wrapped.SpecifyEfficiencyVsSpeedRatio

        if temp is None:
            return False

        return temp

    @specify_efficiency_vs_speed_ratio.setter
    def specify_efficiency_vs_speed_ratio(self, value: 'bool'):
        self.wrapped.SpecifyEfficiencyVsSpeedRatio = bool(value) if value is not None else False

    @property
    def tilt_about_x(self) -> 'float':
        """float: 'TiltAboutX' is the original name of this property."""

        temp = self.wrapped.TiltAboutX

        if temp is None:
            return 0.0

        return temp

    @tilt_about_x.setter
    def tilt_about_x(self, value: 'float'):
        self.wrapped.TiltAboutX = float(value) if value is not None else 0.0

    @property
    def tilt_about_y(self) -> 'float':
        """float: 'TiltAboutY' is the original name of this property."""

        temp = self.wrapped.TiltAboutY

        if temp is None:
            return 0.0

        return temp

    @tilt_about_y.setter
    def tilt_about_y(self, value: 'float'):
        self.wrapped.TiltAboutY = float(value) if value is not None else 0.0

    @property
    def torsional_damping(self) -> 'float':
        """float: 'TorsionalDamping' is the original name of this property."""

        temp = self.wrapped.TorsionalDamping

        if temp is None:
            return 0.0

        return temp

    @torsional_damping.setter
    def torsional_damping(self, value: 'float'):
        self.wrapped.TorsionalDamping = float(value) if value is not None else 0.0

    @property
    def translational_stiffness(self) -> 'float':
        """float: 'TranslationalStiffness' is the original name of this property."""

        temp = self.wrapped.TranslationalStiffness

        if temp is None:
            return 0.0

        return temp

    @translational_stiffness.setter
    def translational_stiffness(self, value: 'float'):
        self.wrapped.TranslationalStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self) -> 'ConceptCoupling._Cast_ConceptCoupling':
        return self._Cast_ConceptCoupling(self)
