"""_1193.py

GearFEModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_GEAR_FLANKS = python_net_import('SMT.MastaAPI.Gears', 'GearFlanks')
_GEAR_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel', 'GearFEModel')

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1195
    from mastapy import _7525
    from mastapy.gears import _324


__docformat__ = 'restructuredtext en'
__all__ = ('GearFEModel',)


class GearFEModel(_1217.GearImplementationDetail):
    """GearFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_FE_MODEL

    class _Cast_GearFEModel:
        """Special nested class for casting GearFEModel to subclasses."""

        def __init__(self, parent: 'GearFEModel'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
            return self._parent._cast(_1217.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearAnalysis)

        @property
        def cylindrical_gear_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1197
            
            return self._parent._cast(_1197.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self):
            from mastapy.gears.fe_model.conical import _1200
            
            return self._parent._cast(_1200.ConicalGearFEModel)

        @property
        def gear_fe_model(self) -> 'GearFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_bore(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FEBore' is the original name of this property."""

        temp = self.wrapped.FEBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy('mastapy._internal.implicit.overridable', 'Overridable_float')(temp) if temp is not None else 0.0

    @fe_bore.setter
    def fe_bore(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FEBore = value

    @property
    def include_all_teeth_in_the_fe_mesh(self) -> 'bool':
        """bool: 'IncludeAllTeethInTheFEMesh' is the original name of this property."""

        temp = self.wrapped.IncludeAllTeethInTheFEMesh

        if temp is None:
            return False

        return temp

    @include_all_teeth_in_the_fe_mesh.setter
    def include_all_teeth_in_the_fe_mesh(self, value: 'bool'):
        self.wrapped.IncludeAllTeethInTheFEMesh = bool(value) if value is not None else False

    @property
    def element_settings(self) -> '_1195.GearMeshingElementOptions':
        """GearMeshingElementOptions: 'ElementSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def calculate_stiffness_from_fe(self):
        """ 'CalculateStiffnessFromFE' is the original name of this method."""

        self.wrapped.CalculateStiffnessFromFE()

    def calculate_stiffness_from_fe_with_progress(self, progress: '_7525.TaskProgress'):
        """ 'CalculateStiffnessFromFE' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)
        """

        self.wrapped.CalculateStiffnessFromFE.Overloads[_TASK_PROGRESS](progress.wrapped if progress else None)

    def get_stress_influence_coefficients_from_fe(self, flank: '_324.GearFlanks'):
        """ 'GetStressInfluenceCoefficientsFromFE' is the original name of this method.

        Args:
            flank (mastapy.gears.GearFlanks)
        """

        flank = conversion.mp_to_pn_enum(flank, 'SMT.MastaAPI.Gears.GearFlanks')
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[_GEAR_FLANKS](flank)

    def get_stress_influence_coefficients_from_fe_with_progress(self, flank: '_324.GearFlanks', progress: '_7525.TaskProgress'):
        """ 'GetStressInfluenceCoefficientsFromFE' is the original name of this method.

        Args:
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)
        """

        flank = conversion.mp_to_pn_enum(flank, 'SMT.MastaAPI.Gears.GearFlanks')
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[_GEAR_FLANKS, _TASK_PROGRESS](flank, progress.wrapped if progress else None)

    @property
    def cast_to(self) -> 'GearFEModel._Cast_GearFEModel':
        return self._Cast_GearFEModel(self)
