"""_781.py

ConicalMeshManufacturingAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingAnalysis')

if TYPE_CHECKING:
    from mastapy.gears.load_case.conical import _884
    from mastapy.gears.manufacturing.bevel import _792, _776


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingAnalysis',)


class ConicalMeshManufacturingAnalysis(_1219.GearMeshImplementationAnalysis):
    """ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS

    class _Cast_ConicalMeshManufacturingAnalysis:
        """Special nested class for casting ConicalMeshManufacturingAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalMeshManufacturingAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(self):
            return self._parent._cast(_1219.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_analysis(self) -> 'ConicalMeshManufacturingAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_load_case(self) -> '_884.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tca(self) -> '_792.EaseOffBasedTCA':
        """EaseOffBasedTCA: 'TCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TCA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_776.ConicalMeshedGearManufacturingAnalysis]':
        """List[ConicalMeshedGearManufacturingAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalMeshManufacturingAnalysis._Cast_ConicalMeshManufacturingAnalysis':
        return self._Cast_ConicalMeshManufacturingAnalysis(self)
