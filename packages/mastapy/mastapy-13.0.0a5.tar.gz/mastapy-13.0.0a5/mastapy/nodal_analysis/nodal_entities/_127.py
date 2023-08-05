"""_127.py

BarElasticMBD
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy.nodal_analysis.nodal_entities import _128
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_ELASTIC_MBD = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'BarElasticMBD')


__docformat__ = 'restructuredtext en'
__all__ = ('BarElasticMBD',)


class BarElasticMBD(_128.BarMBD):
    """BarElasticMBD

    This is a mastapy class.
    """

    TYPE = _BAR_ELASTIC_MBD

    class _Cast_BarElasticMBD:
        """Special nested class for casting BarElasticMBD to subclasses."""

        def __init__(self, parent: 'BarElasticMBD'):
            self._parent = parent

        @property
        def bar_mbd(self):
            return self._parent._cast(_128.BarMBD)

        @property
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _133
            
            return self._parent._cast(_133.ComponentNodalComposite)

        @property
        def nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.NodalEntity)

        @property
        def bar_elastic_mbd(self) -> 'BarElasticMBD':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BarElasticMBD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'BarElasticMBD._Cast_BarElasticMBD':
        return self._Cast_BarElasticMBD(self)
