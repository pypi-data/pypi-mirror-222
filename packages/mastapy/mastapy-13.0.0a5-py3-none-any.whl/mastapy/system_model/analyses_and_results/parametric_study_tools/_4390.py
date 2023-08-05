"""_4390.py

SpecialisedAssemblyParametricStudyTool
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4274
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SpecialisedAssemblyParametricStudyTool')

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyParametricStudyTool',)


class SpecialisedAssemblyParametricStudyTool(_4274.AbstractAssemblyParametricStudyTool):
    """SpecialisedAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_PARAMETRIC_STUDY_TOOL

    class _Cast_SpecialisedAssemblyParametricStudyTool:
        """Special nested class for casting SpecialisedAssemblyParametricStudyTool to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyParametricStudyTool'):
            self._parent = parent

        @property
        def abstract_assembly_parametric_study_tool(self):
            return self._parent._cast(_4274.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartParametricStudyTool)

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
        def agma_gleason_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
            
            return self._parent._cast(_4280.AGMAGleasonConicalGearSetParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4284
            
            return self._parent._cast(_4284.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287
            
            return self._parent._cast(_4287.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
            
            return self._parent._cast(_4292.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
            
            return self._parent._cast(_4293.BoltedJointParametricStudyTool)

        @property
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4302
            
            return self._parent._cast(_4302.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4305
            
            return self._parent._cast(_4305.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
            
            return self._parent._cast(_4308.ConicalGearSetParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4313
            
            return self._parent._cast(_4313.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4315
            
            return self._parent._cast(_4315.CVTParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317
            
            return self._parent._cast(_4317.CycloidalAssemblyParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4323
            
            return self._parent._cast(_4323.CylindricalGearSetParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
            
            return self._parent._cast(_4336.FaceGearSetParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
            
            return self._parent._cast(_4338.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
            
            return self._parent._cast(_4341.GearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4345
            
            return self._parent._cast(_4345.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4349
            
            return self._parent._cast(_4349.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4352
            
            return self._parent._cast(_4352.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4355
            
            return self._parent._cast(_4355.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4374
            
            return self._parent._cast(_4374.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
            
            return self._parent._cast(_4376.PlanetaryGearSetParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
            
            return self._parent._cast(_4383.RollingRingAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
            
            return self._parent._cast(_4393.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4396
            
            return self._parent._cast(_4396.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4399
            
            return self._parent._cast(_4399.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4402
            
            return self._parent._cast(_4402.StraightBevelGearSetParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
            
            return self._parent._cast(_4406.SynchroniserParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4410
            
            return self._parent._cast(_4410.TorqueConverterParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4417
            
            return self._parent._cast(_4417.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4420
            
            return self._parent._cast(_4420.ZerolBevelGearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(self) -> 'SpecialisedAssemblyParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2459.SpecialisedAssembly':
        """SpecialisedAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpecialisedAssemblyParametricStudyTool._Cast_SpecialisedAssemblyParametricStudyTool':
        return self._Cast_SpecialisedAssemblyParametricStudyTool(self)
