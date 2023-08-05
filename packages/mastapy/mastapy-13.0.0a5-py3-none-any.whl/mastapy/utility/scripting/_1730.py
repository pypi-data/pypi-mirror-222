﻿"""_1730.py

ScriptingSetup
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.utility import _1585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SCRIPTING_SETUP = python_net_import('SMT.MastaAPI.Utility.Scripting', 'ScriptingSetup')


__docformat__ = 'restructuredtext en'
__all__ = ('ScriptingSetup',)


class ScriptingSetup(_1585.PerMachineSettings):
    """ScriptingSetup

    This is a mastapy class.
    """

    TYPE = _SCRIPTING_SETUP

    class _Cast_ScriptingSetup:
        """Special nested class for casting ScriptingSetup to subclasses."""

        def __init__(self, parent: 'ScriptingSetup'):
            self._parent = parent

        @property
        def per_machine_settings(self):
            return self._parent._cast(_1585.PerMachineSettings)

        @property
        def persistent_singleton(self):
            from mastapy.utility import _1586
            
            return self._parent._cast(_1586.PersistentSingleton)

        @property
        def scripting_setup(self) -> 'ScriptingSetup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ScriptingSetup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def image_height(self) -> 'int':
        """int: 'ImageHeight' is the original name of this property."""

        temp = self.wrapped.ImageHeight

        if temp is None:
            return 0

        return temp

    @image_height.setter
    def image_height(self, value: 'int'):
        self.wrapped.ImageHeight = int(value) if value is not None else 0

    @property
    def image_width(self) -> 'int':
        """int: 'ImageWidth' is the original name of this property."""

        temp = self.wrapped.ImageWidth

        if temp is None:
            return 0

        return temp

    @image_width.setter
    def image_width(self, value: 'int'):
        self.wrapped.ImageWidth = int(value) if value is not None else 0

    @property
    def load_scripted_properties_when_opening_masta(self) -> 'bool':
        """bool: 'LoadScriptedPropertiesWhenOpeningMASTA' is the original name of this property."""

        temp = self.wrapped.LoadScriptedPropertiesWhenOpeningMASTA

        if temp is None:
            return False

        return temp

    @load_scripted_properties_when_opening_masta.setter
    def load_scripted_properties_when_opening_masta(self, value: 'bool'):
        self.wrapped.LoadScriptedPropertiesWhenOpeningMASTA = bool(value) if value is not None else False

    @property
    def python_exe_path(self) -> 'str':
        """str: 'PythonExePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PythonExePath

        if temp is None:
            return ''

        return temp

    @property
    def python_home_directory(self) -> 'str':
        """str: 'PythonHomeDirectory' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PythonHomeDirectory

        if temp is None:
            return ''

        return temp

    @property
    def python_install_directory(self) -> 'str':
        """str: 'PythonInstallDirectory' is the original name of this property."""

        temp = self.wrapped.PythonInstallDirectory

        if temp is None:
            return ''

        return temp

    @python_install_directory.setter
    def python_install_directory(self, value: 'str'):
        self.wrapped.PythonInstallDirectory = str(value) if value is not None else ''

    @property
    def python_remote_host(self) -> 'str':
        """str: 'PythonRemoteHost' is the original name of this property."""

        temp = self.wrapped.PythonRemoteHost

        if temp is None:
            return ''

        return temp

    @python_remote_host.setter
    def python_remote_host(self, value: 'str'):
        self.wrapped.PythonRemoteHost = str(value) if value is not None else ''

    @property
    def python_remote_port(self) -> 'int':
        """int: 'PythonRemotePort' is the original name of this property."""

        temp = self.wrapped.PythonRemotePort

        if temp is None:
            return 0

        return temp

    @python_remote_port.setter
    def python_remote_port(self, value: 'int'):
        self.wrapped.PythonRemotePort = int(value) if value is not None else 0

    @property
    def run_scripts_in_separate_threads(self) -> 'bool':
        """bool: 'RunScriptsInSeparateThreads' is the original name of this property."""

        temp = self.wrapped.RunScriptsInSeparateThreads

        if temp is None:
            return False

        return temp

    @run_scripts_in_separate_threads.setter
    def run_scripts_in_separate_threads(self, value: 'bool'):
        self.wrapped.RunScriptsInSeparateThreads = bool(value) if value is not None else False

    @property
    def use_default_net_solution_directory(self) -> 'bool':
        """bool: 'UseDefaultNETSolutionDirectory' is the original name of this property."""

        temp = self.wrapped.UseDefaultNETSolutionDirectory

        if temp is None:
            return False

        return temp

    @use_default_net_solution_directory.setter
    def use_default_net_solution_directory(self, value: 'bool'):
        self.wrapped.UseDefaultNETSolutionDirectory = bool(value) if value is not None else False

    @property
    def use_default_plugin_directory(self) -> 'bool':
        """bool: 'UseDefaultPluginDirectory' is the original name of this property."""

        temp = self.wrapped.UseDefaultPluginDirectory

        if temp is None:
            return False

        return temp

    @use_default_plugin_directory.setter
    def use_default_plugin_directory(self, value: 'bool'):
        self.wrapped.UseDefaultPluginDirectory = bool(value) if value is not None else False

    @property
    def use_default_python_scripts_directory(self) -> 'bool':
        """bool: 'UseDefaultPythonScriptsDirectory' is the original name of this property."""

        temp = self.wrapped.UseDefaultPythonScriptsDirectory

        if temp is None:
            return False

        return temp

    @use_default_python_scripts_directory.setter
    def use_default_python_scripts_directory(self, value: 'bool'):
        self.wrapped.UseDefaultPythonScriptsDirectory = bool(value) if value is not None else False

    @property
    def mastapy_version(self) -> 'str':
        """str: 'MastapyVersion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MastapyVersion

        if temp is None:
            return ''

        return temp

    def add_existing_net_solution(self):
        """ 'AddExistingNETSolution' is the original name of this method."""

        self.wrapped.AddExistingNETSolution()

    def restore_api_packages(self):
        """ 'RestoreAPIPackages' is the original name of this method."""

        self.wrapped.RestoreAPIPackages()

    def select_net_solution_directory(self):
        """ 'SelectNETSolutionDirectory' is the original name of this method."""

        self.wrapped.SelectNETSolutionDirectory()

    def select_plugin_directory(self):
        """ 'SelectPluginDirectory' is the original name of this method."""

        self.wrapped.SelectPluginDirectory()

    def select_python_install_directory(self):
        """ 'SelectPythonInstallDirectory' is the original name of this method."""

        self.wrapped.SelectPythonInstallDirectory()

    def select_python_scripts_directory(self):
        """ 'SelectPythonScriptsDirectory' is the original name of this method."""

        self.wrapped.SelectPythonScriptsDirectory()

    @property
    def cast_to(self) -> 'ScriptingSetup._Cast_ScriptingSetup':
        return self._Cast_ScriptingSetup(self)
