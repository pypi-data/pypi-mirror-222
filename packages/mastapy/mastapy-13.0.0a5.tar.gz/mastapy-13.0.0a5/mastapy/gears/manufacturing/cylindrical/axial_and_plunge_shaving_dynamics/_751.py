"""_751.py

ConventionalShavingDynamicsViewModel
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _767, _748
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ConventionalShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ConventionalShavingDynamicsViewModel',)


class ConventionalShavingDynamicsViewModel(_767.ShavingDynamicsViewModel['_748.ConventionalShavingDynamics']):
    """ConventionalShavingDynamicsViewModel

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL

    class _Cast_ConventionalShavingDynamicsViewModel:
        """Special nested class for casting ConventionalShavingDynamicsViewModel to subclasses."""

        def __init__(self, parent: 'ConventionalShavingDynamicsViewModel'):
            self._parent = parent

        @property
        def shaving_dynamics_view_model(self):
            return self._parent._cast(_767.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _768
            
            return self._parent._cast(_768.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(self):
            from mastapy.gears.manufacturing.cylindrical import _625
            
            return self._parent._cast(_625.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(self) -> 'ConventionalShavingDynamicsViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConventionalShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel':
        return self._Cast_ConventionalShavingDynamicsViewModel(self)
