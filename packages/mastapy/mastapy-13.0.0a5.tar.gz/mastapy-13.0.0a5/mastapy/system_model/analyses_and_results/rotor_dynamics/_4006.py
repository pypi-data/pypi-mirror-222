"""_4006.py

RotorDynamicsDrawStyle
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.drawing import _2229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_DYNAMICS_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics', 'RotorDynamicsDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('RotorDynamicsDrawStyle',)


class RotorDynamicsDrawStyle(_2229.ContourDrawStyle):
    """RotorDynamicsDrawStyle

    This is a mastapy class.
    """

    TYPE = _ROTOR_DYNAMICS_DRAW_STYLE

    class _Cast_RotorDynamicsDrawStyle:
        """Special nested class for casting RotorDynamicsDrawStyle to subclasses."""

        def __init__(self, parent: 'RotorDynamicsDrawStyle'):
            self._parent = parent

        @property
        def contour_draw_style(self):
            return self._parent._cast(_2229.ContourDrawStyle)

        @property
        def draw_style_base(self):
            from mastapy.geometry import _306
            
            return self._parent._cast(_306.DrawStyleBase)

        @property
        def steady_state_synchronous_response_draw_style(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3072
            
            return self._parent._cast(_3072.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3851
            
            return self._parent._cast(_3851.StabilityAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6551
            
            return self._parent._cast(_6551.CriticalSpeedAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(self) -> 'RotorDynamicsDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotorDynamicsDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_whirl_orbits(self) -> 'bool':
        """bool: 'ShowWhirlOrbits' is the original name of this property."""

        temp = self.wrapped.ShowWhirlOrbits

        if temp is None:
            return False

        return temp

    @show_whirl_orbits.setter
    def show_whirl_orbits(self, value: 'bool'):
        self.wrapped.ShowWhirlOrbits = bool(value) if value is not None else False

    @property
    def cast_to(self) -> 'RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle':
        return self._Cast_RotorDynamicsDrawStyle(self)
