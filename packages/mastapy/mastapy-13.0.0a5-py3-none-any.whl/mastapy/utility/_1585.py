"""_1585.py

PerMachineSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility import _1586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Utility', 'PerMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PerMachineSettings',)


class PerMachineSettings(_1586.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE = _PER_MACHINE_SETTINGS

    class _Cast_PerMachineSettings:
        """Special nested class for casting PerMachineSettings to subclasses."""

        def __init__(self, parent: 'PerMachineSettings'):
            self._parent = parent

        @property
        def persistent_singleton(self):
            return self._parent._cast(_1586.PersistentSingleton)

        @property
        def fe_user_settings(self):
            from mastapy.nodal_analysis import _68
            
            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _160
            
            return self._parent._cast(_160.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(self):
            from mastapy.gears.materials import _593
            
            return self._parent._cast(_593.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(self):
            from mastapy.gears.ltca.cylindrical import _852
            
            return self._parent._cast(_852.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(self):
            from mastapy.gears.gear_designs.cylindrical import _1008
            
            return self._parent._cast(_1008.CylindricalGearDefaults)

        @property
        def program_settings(self):
            from mastapy.utility import _1587
            
            return self._parent._cast(_1587.ProgramSettings)

        @property
        def pushbullet_settings(self):
            from mastapy.utility import _1588
            
            return self._parent._cast(_1588.PushbulletSettings)

        @property
        def measurement_settings(self):
            from mastapy.utility.units_and_measurements import _1597
            
            return self._parent._cast(_1597.MeasurementSettings)

        @property
        def scripting_setup(self):
            from mastapy.utility.scripting import _1730
            
            return self._parent._cast(_1730.ScriptingSetup)

        @property
        def database_settings(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.DatabaseSettings)

        @property
        def cad_export_settings(self):
            from mastapy.utility.cad_export import _1821
            
            return self._parent._cast(_1821.CADExportSettings)

        @property
        def skf_settings(self):
            from mastapy.bearings import _1886
            
            return self._parent._cast(_1886.SKFSettings)

        @property
        def planet_carrier_settings(self):
            from mastapy.system_model.part_model import _2453
            
            return self._parent._cast(_2453.PlanetCarrierSettings)

        @property
        def per_machine_settings(self) -> 'PerMachineSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PerMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def reset_to_defaults(self):
        """ 'ResetToDefaults' is the original name of this method."""

        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self) -> 'PerMachineSettings._Cast_PerMachineSettings':
        return self._Cast_PerMachineSettings(self)
