"""_6885.py

KlingelnbergCycloPalloidHypoidGearSetLoadCase
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6882
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearSetLoadCase')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.static_loads import _6883, _6884


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetLoadCase',)


class KlingelnbergCycloPalloidHypoidGearSetLoadCase(_6882.KlingelnbergCycloPalloidConicalGearSetLoadCase):
    """KlingelnbergCycloPalloidHypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetLoadCase to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetLoadCase'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(self):
            return self._parent._cast(_6882.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6816
            
            return self._parent._cast(_6816.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6863
            
            return self._parent._cast(_6863.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6920
            
            return self._parent._cast(_6920.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6774
            
            return self._parent._cast(_6774.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6896
            
            return self._parent._cast(_6896.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2639
            
            return self._parent._cast(_2639.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2635
            
            return self._parent._cast(_2635.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self) -> 'KlingelnbergCycloPalloidHypoidGearSetLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2521.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6883.KlingelnbergCycloPalloidHypoidGearLoadCase]':
        """List[KlingelnbergCycloPalloidHypoidGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_load_case(self) -> 'List[_6883.KlingelnbergCycloPalloidHypoidGearLoadCase]':
        """List[KlingelnbergCycloPalloidHypoidGearLoadCase]: 'KlingelnbergCycloPalloidHypoidGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_load_case(self) -> 'List[_6884.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshLoadCase]: 'KlingelnbergCycloPalloidHypoidMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase(self)
