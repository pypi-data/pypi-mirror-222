"""_2584.py

Synchroniser
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2325
    from mastapy.system_model.part_model.couplings import _2588, _2586


__docformat__ = 'restructuredtext en'
__all__ = ('Synchroniser',)


class Synchroniser(_2459.SpecialisedAssembly):
    """Synchroniser

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER

    class _Cast_Synchroniser:
        """Special nested class for casting Synchroniser to subclasses."""

        def __init__(self, parent: 'Synchroniser'):
            self._parent = parent

        @property
        def specialised_assembly(self):
            return self._parent._cast(_2459.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2417
            
            return self._parent._cast(_2417.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2190
            
            return self._parent._cast(_2190.DesignEntity)

        @property
        def synchroniser(self) -> 'Synchroniser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Synchroniser.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_left_cone(self) -> 'bool':
        """bool: 'HasLeftCone' is the original name of this property."""

        temp = self.wrapped.HasLeftCone

        if temp is None:
            return False

        return temp

    @has_left_cone.setter
    def has_left_cone(self, value: 'bool'):
        self.wrapped.HasLeftCone = bool(value) if value is not None else False

    @property
    def has_right_cone(self) -> 'bool':
        """bool: 'HasRightCone' is the original name of this property."""

        temp = self.wrapped.HasRightCone

        if temp is None:
            return False

        return temp

    @has_right_cone.setter
    def has_right_cone(self, value: 'bool'):
        self.wrapped.HasRightCone = bool(value) if value is not None else False

    @property
    def clutch_connection_left(self) -> '_2325.ClutchConnection':
        """ClutchConnection: 'ClutchConnectionLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnectionLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clutch_connection_right(self) -> '_2325.ClutchConnection':
        """ClutchConnection: 'ClutchConnectionRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnectionRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hub_and_sleeve(self) -> '_2588.SynchroniserSleeve':
        """SynchroniserSleeve: 'HubAndSleeve' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HubAndSleeve

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_cone(self) -> '_2586.SynchroniserHalf':
        """SynchroniserHalf: 'LeftCone' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftCone

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_cone(self) -> '_2586.SynchroniserHalf':
        """SynchroniserHalf: 'RightCone' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightCone

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Synchroniser._Cast_Synchroniser':
        return self._Cast_Synchroniser(self)
