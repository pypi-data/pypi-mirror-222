# coding: utf8

from typing import Optional, Union

from .._base import BinaryDefinition
from .._enums import (
    BinaryType,
    UpOrDown,
)


class EtiBinaryDefinition(BinaryDefinition):
    """
    Parameters
    ----------
    notional_amount : float, optional

    binary_type : BinaryType or str, optional

    up_or_down : UpOrDown or str, optional

    level : float, optional

    """

    def __init__(
        self,
        notional_amount: Optional[float] = None,
        binary_type: Union[BinaryType, str] = None,
        up_or_down: Union[UpOrDown, str] = None,
        level: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.notional_amount = notional_amount
        self.binary_type = binary_type
        self.up_or_down = up_or_down
        self.level = level

    @property
    def binary_type(self):
        """
        :return: enum BinaryType
        """
        return self._get_enum_parameter(BinaryType, "binaryType")

    @binary_type.setter
    def binary_type(self, value):
        self._set_enum_parameter(BinaryType, "binaryType", value)

    @property
    def up_or_down(self):
        """
        :return: enum UpOrDown
        """
        return self._get_enum_parameter(UpOrDown, "upOrDown")

    @up_or_down.setter
    def up_or_down(self, value):
        self._set_enum_parameter(UpOrDown, "upOrDown", value)

    @property
    def level(self):
        """
        :return: float
        """
        return self._get_parameter("level")

    @level.setter
    def level(self, value):
        self._set_parameter("level", value)

    @property
    def notional_amount(self):
        """
        :return: float
        """
        return self._get_parameter("notionalAmount")

    @notional_amount.setter
    def notional_amount(self, value):
        self._set_parameter("notionalAmount", value)
