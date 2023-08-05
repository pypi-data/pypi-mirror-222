"""_7533.py

PythonCommand
"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy.scripting import _7534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PYTHON_COMMAND = python_net_import('SMT.MastaAPIUtility.Scripting', 'PythonCommand')


__docformat__ = 'restructuredtext en'
__all__ = ('PythonCommand',)


T = TypeVar('T')


class PythonCommand(_7534.ScriptingCommand, Generic[T]):
    """PythonCommand

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _PYTHON_COMMAND

    class _Cast_PythonCommand:
        """Special nested class for casting PythonCommand to subclasses."""

        def __init__(self, parent: 'PythonCommand'):
            self._parent = parent

        @property
        def python_command(self) -> 'PythonCommand':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PythonCommand.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def execute(self):
        """ 'Execute' is the original name of this method."""

        self.wrapped.Execute()

    @property
    def cast_to(self) -> 'PythonCommand._Cast_PythonCommand':
        return self._Cast_PythonCommand(self)
