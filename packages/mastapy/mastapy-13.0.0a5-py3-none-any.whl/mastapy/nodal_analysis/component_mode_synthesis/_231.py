﻿"""_231.py

RealCMSResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.component_mode_synthesis import _228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_CMS_RESULTS = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'RealCMSResults')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _124


__docformat__ = 'restructuredtext en'
__all__ = ('RealCMSResults',)


class RealCMSResults(_228.CMSResults):
    """RealCMSResults

    This is a mastapy class.
    """

    TYPE = _REAL_CMS_RESULTS

    class _Cast_RealCMSResults:
        """Special nested class for casting RealCMSResults to subclasses."""

        def __init__(self, parent: 'RealCMSResults'):
            self._parent = parent

        @property
        def cms_results(self):
            return self._parent._cast(_228.CMSResults)

        @property
        def modal_cms_results(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _230
            
            return self._parent._cast(_230.ModalCMSResults)

        @property
        def static_cms_results(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _233
            
            return self._parent._cast(_233.StaticCMSResults)

        @property
        def real_cms_results(self) -> 'RealCMSResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RealCMSResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_displacements(self) -> '_124.NodeVectorState':
        """NodeVectorState: 'NodeDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeDisplacements

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RealCMSResults._Cast_RealCMSResults':
        return self._Cast_RealCMSResults(self)
