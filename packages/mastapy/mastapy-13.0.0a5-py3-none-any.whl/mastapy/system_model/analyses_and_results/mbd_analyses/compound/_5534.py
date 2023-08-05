"""_5534.py

ConicalGearCompoundMultibodyDynamicsAnalysis
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5560
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ConicalGearCompoundMultibodyDynamicsAnalysis')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5386


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCompoundMultibodyDynamicsAnalysis',)


class ConicalGearCompoundMultibodyDynamicsAnalysis(_5560.GearCompoundMultibodyDynamicsAnalysis):
    """ConicalGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_ConicalGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def gear_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5560.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5579
            
            return self._parent._cast(_5579.MountableComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
            
            return self._parent._cast(_5527.ComponentCompoundMultibodyDynamicsAnalysis)

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
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5506
            
            return self._parent._cast(_5506.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5513
            
            return self._parent._cast(_5513.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5516
            
            return self._parent._cast(_5516.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5517
            
            return self._parent._cast(_5517.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5518
            
            return self._parent._cast(_5518.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
            
            return self._parent._cast(_5564.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5568
            
            return self._parent._cast(_5568.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5571
            
            return self._parent._cast(_5571.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5574
            
            return self._parent._cast(_5574.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5601
            
            return self._parent._cast(_5601.SpiralBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5607
            
            return self._parent._cast(_5607.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5610
            
            return self._parent._cast(_5610.StraightBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5613
            
            return self._parent._cast(_5613.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5614
            
            return self._parent._cast(_5614.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5628
            
            return self._parent._cast(_5628.ZerolBevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_compound_multibody_dynamics_analysis(self) -> 'ConicalGearCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearCompoundMultibodyDynamicsAnalysis]':
        """List[ConicalGearCompoundMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5386.ConicalGearMultibodyDynamicsAnalysis]':
        """List[ConicalGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_5386.ConicalGearMultibodyDynamicsAnalysis]':
        """List[ConicalGearMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearCompoundMultibodyDynamicsAnalysis':
        return self._Cast_ConicalGearCompoundMultibodyDynamicsAnalysis(self)
