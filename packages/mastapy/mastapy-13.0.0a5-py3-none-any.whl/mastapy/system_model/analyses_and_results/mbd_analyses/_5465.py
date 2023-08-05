"""_5465.py

SpiralBevelGearSetMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5370
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'SpiralBevelGearSetMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6923
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5464, _5463


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetMultibodyDynamicsAnalysis',)


class SpiralBevelGearSetMultibodyDynamicsAnalysis(_5370.BevelGearSetMultibodyDynamicsAnalysis):
    """SpiralBevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_SpiralBevelGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_multibody_dynamics_analysis(self):
            return self._parent._cast(_5370.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5356
            
            return self._parent._cast(_5356.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387
            
            return self._parent._cast(_5387.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
            
            return self._parent._cast(_5414.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
            
            return self._parent._cast(_5462.SpecialisedAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5350
            
            return self._parent._cast(_5350.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
            
            return self._parent._cast(_5440.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7515
            
            return self._parent._cast(_7515.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartAnalysisCase)

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
        def spiral_bevel_gear_set_multibody_dynamics_analysis(self) -> 'SpiralBevelGearSetMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2526.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6923.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_5464.SpiralBevelGearMultibodyDynamicsAnalysis]':
        """List[SpiralBevelGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_multibody_dynamics_analysis(self) -> 'List[_5464.SpiralBevelGearMultibodyDynamicsAnalysis]':
        """List[SpiralBevelGearMultibodyDynamicsAnalysis]: 'SpiralBevelGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_multibody_dynamics_analysis(self) -> 'List[_5463.SpiralBevelGearMeshMultibodyDynamicsAnalysis]':
        """List[SpiralBevelGearMeshMultibodyDynamicsAnalysis]: 'SpiralBevelMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetMultibodyDynamicsAnalysis._Cast_SpiralBevelGearSetMultibodyDynamicsAnalysis':
        return self._Cast_SpiralBevelGearSetMultibodyDynamicsAnalysis(self)
