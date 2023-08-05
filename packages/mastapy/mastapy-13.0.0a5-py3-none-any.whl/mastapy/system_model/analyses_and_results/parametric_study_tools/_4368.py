﻿"""_4368.py

ParametricStudyToolResultsForReporting
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_TOOL_RESULTS_FOR_REPORTING = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ParametricStudyToolResultsForReporting')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyToolResultsForReporting',)


class ParametricStudyToolResultsForReporting(_0.APIBase):
    """ParametricStudyToolResultsForReporting

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_TOOL_RESULTS_FOR_REPORTING

    class _Cast_ParametricStudyToolResultsForReporting:
        """Special nested class for casting ParametricStudyToolResultsForReporting to subclasses."""

        def __init__(self, parent: 'ParametricStudyToolResultsForReporting'):
            self._parent = parent

        @property
        def parametric_study_tool_results_for_reporting(self) -> 'ParametricStudyToolResultsForReporting':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParametricStudyToolResultsForReporting.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParametricStudyToolResultsForReporting._Cast_ParametricStudyToolResultsForReporting':
        return self._Cast_ParametricStudyToolResultsForReporting(self)
