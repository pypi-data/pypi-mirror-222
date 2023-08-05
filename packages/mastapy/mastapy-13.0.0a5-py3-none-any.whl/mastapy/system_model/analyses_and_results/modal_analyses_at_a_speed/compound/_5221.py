"""_5221.py

AbstractAssemblyCompoundModalAnalysisAtASpeed
"""
from __future__ import annotations

from typing import TYPE_CHECKING, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'AbstractAssemblyCompoundModalAnalysisAtASpeed')

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5092


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundModalAnalysisAtASpeed',)


class AbstractAssemblyCompoundModalAnalysisAtASpeed(_5300.PartCompoundModalAnalysisAtASpeed):
    """AbstractAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5300.PartCompoundModalAnalysisAtASpeed)

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
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5227
            
            return self._parent._cast(_5227.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5228
            
            return self._parent._cast(_5228.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5231
            
            return self._parent._cast(_5231.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5234
            
            return self._parent._cast(_5234.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5239
            
            return self._parent._cast(_5239.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5241
            
            return self._parent._cast(_5241.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5242
            
            return self._parent._cast(_5242.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5247
            
            return self._parent._cast(_5247.ConceptCouplingCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5252
            
            return self._parent._cast(_5252.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5255
            
            return self._parent._cast(_5255.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5258
            
            return self._parent._cast(_5258.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5262
            
            return self._parent._cast(_5262.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5264
            
            return self._parent._cast(_5264.CycloidalAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5270
            
            return self._parent._cast(_5270.CylindricalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5276
            
            return self._parent._cast(_5276.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5278
            
            return self._parent._cast(_5278.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5281
            
            return self._parent._cast(_5281.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5285
            
            return self._parent._cast(_5285.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5289
            
            return self._parent._cast(_5289.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5292
            
            return self._parent._cast(_5292.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5295
            
            return self._parent._cast(_5295.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5301
            
            return self._parent._cast(_5301.PartToPartShearCouplingCompoundModalAnalysisAtASpeed)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5305
            
            return self._parent._cast(_5305.PlanetaryGearSetCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5312
            
            return self._parent._cast(_5312.RollingRingAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5315
            
            return self._parent._cast(_5315.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5319
            
            return self._parent._cast(_5319.SpecialisedAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5322
            
            return self._parent._cast(_5322.SpiralBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5323
            
            return self._parent._cast(_5323.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5328
            
            return self._parent._cast(_5328.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5331
            
            return self._parent._cast(_5331.StraightBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5334
            
            return self._parent._cast(_5334.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5338
            
            return self._parent._cast(_5338.TorqueConverterCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5346
            
            return self._parent._cast(_5346.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5349
            
            return self._parent._cast(_5349.ZerolBevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(self) -> 'AbstractAssemblyCompoundModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5092.AbstractAssemblyModalAnalysisAtASpeed]':
        """List[AbstractAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5092.AbstractAssemblyModalAnalysisAtASpeed]':
        """List[AbstractAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed':
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed(self)
