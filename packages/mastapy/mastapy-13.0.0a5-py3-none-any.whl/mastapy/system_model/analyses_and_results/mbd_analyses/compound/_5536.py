"""_5536.py

ConicalGearSetCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ConicalGearSetCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5387


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetCompoundMultibodyDynamicsAnalysis',)


class ConicalGearSetCompoundMultibodyDynamicsAnalysis(_5562.GearSetCompoundMultibodyDynamicsAnalysis):
    """ConicalGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ConicalGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearSetCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5562.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5600
            
            return self._parent._cast(_5600.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5502
            
            return self._parent._cast(_5502.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5581
            
            return self._parent._cast(_5581.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7512
            
            return self._parent._cast(_7512.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2633
            
            return self._parent._cast(_2633.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5508
            
            return self._parent._cast(_5508.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5515
            
            return self._parent._cast(_5515.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5520
            
            return self._parent._cast(_5520.BevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
            
            return self._parent._cast(_5566.HypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5570
            
            return self._parent._cast(_5570.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5573
            
            return self._parent._cast(_5573.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
            
            return self._parent._cast(_5576.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5603
            
            return self._parent._cast(_5603.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5609
            
            return self._parent._cast(_5609.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5612
            
            return self._parent._cast(_5612.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5630
            
            return self._parent._cast(_5630.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self) -> 'ConicalGearSetCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5387.ConicalGearSetMultibodyDynamicsAnalysis]':
        """List[ConicalGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5387.ConicalGearSetMultibodyDynamicsAnalysis]':
        """List[ConicalGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearSetCompoundMultibodyDynamicsAnalysis':
        return self._Cast_ConicalGearSetCompoundMultibodyDynamicsAnalysis(self)
