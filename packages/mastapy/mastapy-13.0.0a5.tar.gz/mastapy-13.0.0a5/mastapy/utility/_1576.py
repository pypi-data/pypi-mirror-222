﻿"""_1576.py

IHaveAllSettings
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_I_HAVE_ALL_SETTINGS = python_net_import('SMT.MastaAPI.Utility', 'IHaveAllSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('IHaveAllSettings',)


class IHaveAllSettings:
    """This class is a public interface.
    The class body has intentionally been left empty.
    """
