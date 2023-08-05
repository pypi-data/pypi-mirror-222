"""_229.py

HarmonicCMSResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.component_mode_synthesis import _228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_CMS_RESULTS = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'HarmonicCMSResults')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicCMSResults',)


class HarmonicCMSResults(_228.CMSResults):
    """HarmonicCMSResults

    This is a mastapy class.
    """

    TYPE = _HARMONIC_CMS_RESULTS

    class _Cast_HarmonicCMSResults:
        """Special nested class for casting HarmonicCMSResults to subclasses."""

        def __init__(self, parent: 'HarmonicCMSResults'):
            self._parent = parent

        @property
        def cms_results(self):
            return self._parent._cast(_228.CMSResults)

        @property
        def harmonic_cms_results(self) -> 'HarmonicCMSResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicCMSResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HarmonicCMSResults._Cast_HarmonicCMSResults':
        return self._Cast_HarmonicCMSResults(self)
