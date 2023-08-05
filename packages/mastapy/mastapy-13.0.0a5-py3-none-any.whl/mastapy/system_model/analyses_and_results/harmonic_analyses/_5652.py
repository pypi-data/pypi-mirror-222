"""_5652.py

AbstractPeriodicExcitationDetail
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AbstractPeriodicExcitationDetail')

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1370


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractPeriodicExcitationDetail',)


class AbstractPeriodicExcitationDetail(_0.APIBase):
    """AbstractPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_PERIODIC_EXCITATION_DETAIL

    class _Cast_AbstractPeriodicExcitationDetail:
        """Special nested class for casting AbstractPeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'AbstractPeriodicExcitationDetail'):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
            
            return self._parent._cast(_5705.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5706
            
            return self._parent._cast(_5706.ElectricMachineRotorXForcePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5707
            
            return self._parent._cast(_5707.ElectricMachineRotorXMomentPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708
            
            return self._parent._cast(_5708.ElectricMachineRotorYForcePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5709
            
            return self._parent._cast(_5709.ElectricMachineRotorYMomentPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
            
            return self._parent._cast(_5710.ElectricMachineRotorZForcePeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711
            
            return self._parent._cast(_5711.ElectricMachineStatorToothAxialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5712
            
            return self._parent._cast(_5712.ElectricMachineStatorToothLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
            
            return self._parent._cast(_5713.ElectricMachineStatorToothMomentsExcitationDetail)

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
            
            return self._parent._cast(_5714.ElectricMachineStatorToothRadialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
            
            return self._parent._cast(_5715.ElectricMachineStatorToothTangentialLoadsExcitationDetail)

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5716
            
            return self._parent._cast(_5716.ElectricMachineTorqueRipplePeriodicExcitationDetail)

        @property
        def gear_mesh_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5726
            
            return self._parent._cast(_5726.GearMeshExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5728
            
            return self._parent._cast(_5728.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5729
            
            return self._parent._cast(_5729.GearMeshTEExcitationDetail)

        @property
        def general_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5731
            
            return self._parent._cast(_5731.GeneralPeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
            
            return self._parent._cast(_5762.PeriodicExcitationWithReferenceShaft)

        @property
        def single_node_periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5779
            
            return self._parent._cast(_5779.SingleNodePeriodicExcitationWithReferenceShaft)

        @property
        def unbalanced_mass_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5805
            
            return self._parent._cast(_5805.UnbalancedMassExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(self) -> 'AbstractPeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractPeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_load_data(self) -> '_1370.HarmonicLoadDataBase':
        """HarmonicLoadDataBase: 'HarmonicLoadData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail':
        return self._Cast_AbstractPeriodicExcitationDetail(self)
