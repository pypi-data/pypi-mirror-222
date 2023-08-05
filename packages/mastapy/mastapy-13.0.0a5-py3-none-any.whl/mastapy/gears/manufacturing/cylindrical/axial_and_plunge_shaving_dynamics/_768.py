"""_768.py

ShavingDynamicsViewModelBase
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.gears.manufacturing.cylindrical import _625
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsViewModelBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsViewModelBase',)


class ShavingDynamicsViewModelBase(_625.GearManufacturingConfigurationViewModel):
    """ShavingDynamicsViewModelBase

    This is a mastapy class.
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL_BASE

    class _Cast_ShavingDynamicsViewModelBase:
        """Special nested class for casting ShavingDynamicsViewModelBase to subclasses."""

        def __init__(self, parent: 'ShavingDynamicsViewModelBase'):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(self):
            return self._parent._cast(_625.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _751
            
            return self._parent._cast(_751.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _757
            
            return self._parent._cast(_757.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _767
            
            return self._parent._cast(_767.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(self) -> 'ShavingDynamicsViewModelBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsViewModelBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase':
        return self._Cast_ShavingDynamicsViewModelBase(self)
