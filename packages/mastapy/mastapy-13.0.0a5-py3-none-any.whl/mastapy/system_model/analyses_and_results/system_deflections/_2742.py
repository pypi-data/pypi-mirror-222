"""_2742.py

GearSetSystemDeflection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.system_deflections import _2788
from mastapy._internal.cast_exception import CastException

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationDetail')
_GEAR_SET_MODES = python_net_import('SMT.MastaAPI.Gears', 'GearSetModes')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_BOOLEAN = python_net_import('System', 'Boolean')
_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'GearSetSystemDeflection')

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.power_flows import _4073
    from mastapy.gears.analysis import _1227, _1224
    from mastapy.gears import _327
    from mastapy import _7525


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetSystemDeflection',)


class GearSetSystemDeflection(_2788.SpecialisedAssemblySystemDeflection):
    """GearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_SYSTEM_DEFLECTION

    class _Cast_GearSetSystemDeflection:
        """Special nested class for casting GearSetSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearSetSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(self):
            return self._parent._cast(_2788.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2667
            
            return self._parent._cast(_2667.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2767
            
            return self._parent._cast(_2767.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7513
            
            return self._parent._cast(_7513.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7514
            
            return self._parent._cast(_7514.PartStaticLoadAnalysisCase)

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
        def agma_gleason_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2672
            
            return self._parent._cast(_2672.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2684
            
            return self._parent._cast(_2684.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2689
            
            return self._parent._cast(_2689.BevelGearSetSystemDeflection)

        @property
        def concept_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2703
            
            return self._parent._cast(_2703.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2707
            
            return self._parent._cast(_2707.ConicalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2724
            
            return self._parent._cast(_2724.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2725
            
            return self._parent._cast(_2725.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2726
            
            return self._parent._cast(_2726.CylindricalGearSetSystemDeflectionWithLTCAResults)

        @property
        def face_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2737
            
            return self._parent._cast(_2737.FaceGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2746
            
            return self._parent._cast(_2746.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2751
            
            return self._parent._cast(_2751.KlingelnbergCycloPalloidConicalGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2754
            
            return self._parent._cast(_2754.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2757
            
            return self._parent._cast(_2757.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2790
            
            return self._parent._cast(_2790.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2796
            
            return self._parent._cast(_2796.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2799
            
            return self._parent._cast(_2799.StraightBevelGearSetSystemDeflection)

        @property
        def worm_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2819
            
            return self._parent._cast(_2819.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2822
            
            return self._parent._cast(_2822.ZerolBevelGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(self) -> 'GearSetSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2514.GearSet':
        """GearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_361.GearSetRating':
        """GearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4073.GearSetPowerFlow':
        """GearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_for(self, gear_set_imp_detail: '_1227.GearSetImplementationDetail', gear_set_mode: '_327.GearSetModes') -> '_1224.GearSetImplementationAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)

        Returns:
            mastapy.gears.analysis.GearSetImplementationAnalysis
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode, 'SMT.MastaAPI.Gears.GearSetModes')
        method_result = self.wrapped.AnalysisFor(gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def implementation_detail_results_failed_for(self, gear_set_imp_detail: '_1227.GearSetImplementationDetail', gear_set_mode: '_327.GearSetModes') -> 'bool':
        """ 'ImplementationDetailResultsFailedFor' is the original name of this method.

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)

        Returns:
            bool
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode, 'SMT.MastaAPI.Gears.GearSetModes')
        method_result = self.wrapped.ImplementationDetailResultsFailedFor(gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode)
        return method_result

    def perform_implementation_detail_analysis_with_progress(self, imp_detail: '_1227.GearSetImplementationDetail', gear_set_mode: '_327.GearSetModes', progress: '_7525.TaskProgress', run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            progress (mastapy.TaskProgress)
            run_all_planetary_meshes (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode, 'SMT.MastaAPI.Gears.GearSetModes')
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _TASK_PROGRESS, _BOOLEAN](imp_detail.wrapped if imp_detail else None, gear_set_mode, progress.wrapped if progress else None, run_all_planetary_meshes if run_all_planetary_meshes else False)

    def perform_implementation_detail_analysis(self, imp_detail: '_1227.GearSetImplementationDetail', gear_set_mode: '_327.GearSetModes', run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode, 'SMT.MastaAPI.Gears.GearSetModes')
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _BOOLEAN](imp_detail.wrapped if imp_detail else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False)

    @property
    def cast_to(self) -> 'GearSetSystemDeflection._Cast_GearSetSystemDeflection':
        return self._Cast_GearSetSystemDeflection(self)
