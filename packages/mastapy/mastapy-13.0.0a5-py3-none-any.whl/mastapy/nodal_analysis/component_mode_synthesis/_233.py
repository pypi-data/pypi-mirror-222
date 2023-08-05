"""_233.py

StaticCMSResults
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.nodal_analysis.component_mode_synthesis import _231
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_CMS_RESULTS = python_net_import('SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis', 'StaticCMSResults')

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _124


__docformat__ = 'restructuredtext en'
__all__ = ('StaticCMSResults',)


class StaticCMSResults(_231.RealCMSResults):
    """StaticCMSResults

    This is a mastapy class.
    """

    TYPE = _STATIC_CMS_RESULTS

    class _Cast_StaticCMSResults:
        """Special nested class for casting StaticCMSResults to subclasses."""

        def __init__(self, parent: 'StaticCMSResults'):
            self._parent = parent

        @property
        def real_cms_results(self):
            return self._parent._cast(_231.RealCMSResults)

        @property
        def cms_results(self):
            from mastapy.nodal_analysis.component_mode_synthesis import _228
            
            return self._parent._cast(_228.CMSResults)

        @property
        def static_cms_results(self) -> 'StaticCMSResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StaticCMSResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_stress_tensors(self) -> '_124.NodeVectorState':
        """NodeVectorState: 'NodeStressTensors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeStressTensors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def calculate_stress(self):
        """ 'CalculateStress' is the original name of this method."""

        self.wrapped.CalculateStress()

    @property
    def cast_to(self) -> 'StaticCMSResults._Cast_StaticCMSResults':
        return self._Cast_StaticCMSResults(self)
