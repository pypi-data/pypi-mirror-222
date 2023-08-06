# coding: utf8

from typing import Optional, Union

from ......_types import OptDateTime
from .._base import BarrierDefinition
from .._enums import (
    BarrierMode,
    InOrOut,
    UpOrDown,
)


class FxBarrierDefinition(BarrierDefinition):
    """
    Parameters
    ----------
    barrier_mode : BarrierMode or str, optional
        Barrier Mode of the barrier option
    in_or_out : InOrOut or str, optional
        In/Out property of the barrier option
    up_or_down : UpOrDown or str, optional
        Up/Down property of the barrier option
    level : float, optional
        Barrier of the barrier option
    rebate_amount : float, optional
        Rebate of the barrier option
    window_end_date : str or date or datetime or timedelta, optional
        Window Start date of the barrier option
    window_start_date : str or date or datetime or timedelta, optional
        Window Start date of the barrier option
    """

    def __init__(
        self,
        barrier_mode: Union[BarrierMode, str] = None,
        in_or_out: Union[InOrOut, str] = None,
        up_or_down: Union[UpOrDown, str] = None,
        level: Optional[float] = None,
        rebate_amount: Optional[float] = None,
        window_end_date: "OptDateTime" = None,
        window_start_date: "OptDateTime" = None,
    ) -> None:
        super().__init__()
        self.barrier_mode = barrier_mode
        self.in_or_out = in_or_out
        self.up_or_down = up_or_down
        self.level = level
        self.rebate_amount = rebate_amount
        self.window_end_date = window_end_date
        self.window_start_date = window_start_date

    @property
    def barrier_mode(self):
        """
        Barrier Mode of the barrier option
        :return: enum BarrierMode
        """
        return self._get_enum_parameter(BarrierMode, "barrierMode")

    @barrier_mode.setter
    def barrier_mode(self, value):
        self._set_enum_parameter(BarrierMode, "barrierMode", value)

    @property
    def in_or_out(self):
        """
        In/Out property of the barrier option
        :return: enum InOrOut
        """
        return self._get_enum_parameter(InOrOut, "inOrOut")

    @in_or_out.setter
    def in_or_out(self, value):
        self._set_enum_parameter(InOrOut, "inOrOut", value)

    @property
    def up_or_down(self):
        """
        Up/Down property of the barrier option
        :return: enum UpOrDown
        """
        return self._get_enum_parameter(UpOrDown, "upOrDown")

    @up_or_down.setter
    def up_or_down(self, value):
        self._set_enum_parameter(UpOrDown, "upOrDown", value)

    @property
    def level(self):
        """
        Barrier of the barrier option
        :return: float
        """
        return self._get_parameter("level")

    @level.setter
    def level(self, value):
        self._set_parameter("level", value)

    @property
    def rebate_amount(self):
        """
        Rebate of the barrier option
        :return: float
        """
        return self._get_parameter("rebateAmount")

    @rebate_amount.setter
    def rebate_amount(self, value):
        self._set_parameter("rebateAmount", value)

    @property
    def window_end_date(self):
        """
        Window Start date of the barrier option
        :return: str
        """
        return self._get_parameter("windowEndDate")

    @window_end_date.setter
    def window_end_date(self, value):
        self._set_datetime_parameter("windowEndDate", value)

    @property
    def window_start_date(self):
        """
        Window Start date of the barrier option
        :return: str
        """
        return self._get_parameter("windowStartDate")

    @window_start_date.setter
    def window_start_date(self, value):
        self._set_datetime_parameter("windowStartDate", value)
