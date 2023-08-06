# coding: utf8

from typing import Optional

from ......_types import OptDateTime
from ..._instrument_definition import ObjectDefinition


class FxDualCurrencyDefinition(ObjectDefinition):
    """
    Parameters
    ----------
    deposit_start_date : str or date or datetime or timedelta, optional
        Deposit Start Date for the DualCurrencyDeposit option
    margin_percent : float, optional
        Margin for the DualCurrencyDeposit option
    """

    def __init__(
        self,
        deposit_start_date: "OptDateTime" = None,
        margin_percent: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.deposit_start_date = deposit_start_date
        self.margin_percent = margin_percent

    @property
    def deposit_start_date(self):
        """
        Deposit Start Date for the DualCurrencyDeposit option
        :return: str
        """
        return self._get_parameter("depositStartDate")

    @deposit_start_date.setter
    def deposit_start_date(self, value):
        self._set_date_parameter("depositStartDate", value)

    @property
    def margin_percent(self):
        """
        Margin for the DualCurrencyDeposit option
        :return: float
        """
        return self._get_parameter("marginPercent")

    @margin_percent.setter
    def margin_percent(self, value):
        self._set_parameter("marginPercent", value)
