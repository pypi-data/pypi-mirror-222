﻿"""_2245.py

ExcitationAnalysisViewOption
"""
from __future__ import annotations

from typing import TYPE_CHECKING
from enum import Enum

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCITATION_ANALYSIS_VIEW_OPTION = python_net_import('SMT.MastaAPI.SystemModel.Drawing.Options', 'ExcitationAnalysisViewOption')


__docformat__ = 'restructuredtext en'
__all__ = ('ExcitationAnalysisViewOption',)


class ExcitationAnalysisViewOption(Enum):
    """ExcitationAnalysisViewOption

    This is a mastapy class.

    Note:
        This class is an Enum.
    """

    @classmethod
    def type_(cls):
        return _EXCITATION_ANALYSIS_VIEW_OPTION

    COUPLED_MODES = 0
    UNCOUPLED_MODES = 1
    OPERATING_DEFLECTION_SHAPES_BY_EXCITATION = 2
    OPERATING_DEFLECTION_SHAPES_BY_ORDER = 3


def __enum_setattr(self, attr, value):
    raise AttributeError('Cannot set the attributes of an Enum.') from None


def __enum_delattr(self, attr):
    raise AttributeError('Cannot delete the attributes of an Enum.') from None


ExcitationAnalysisViewOption.__setattr__ = __enum_setattr
ExcitationAnalysisViewOption.__delattr__ = __enum_delattr
