# coding: utf8
from typing import Optional, Union

from ....._types import OptDateTime
from ..._enums import (
    BusinessDayConvention,
    DateRollingConvention,
    DayCountBasis,
    Frequency,
)
from .._instrument_definition import InstrumentDefinition


class TermDepositInstrumentDefinition(InstrumentDefinition):
    """
        API endpoint for Financial Contract analytics,
    that returns calculations relevant to each contract type.

    Parameters
    ----------
    instrument_tag : str, optional
        User defined string to identify the instrument. It can be used to link output
        results to the instrument definition. Only alphabetic, numeric and '- _.#=@'
        characters are supported.
    instrument_code : str, optional
        Code to define the term deposit instrument. For the moment, only RICs for CDs
        and Wholesales deposits are supported, with deposit code (ex:"EUR1MD=").
    start_date : str or date or datetime or timedelta, optional
        The date the term deposit starts accruing interest. Its effective date.
        By default it is derived from the ValuationDate and the day to spot convention
        of the contract currency.
    end_date : str or date or datetime or timedelta, optional
        The maturity date of the term deposit contract. Either the endDate or the tenor
        must be provided.
    tenor : str, optional
        The period code that represents the time between the start date and end date of
        the contract.
        Mandatory if instrumentCode is null. Either the endDate or the tenor must be
        provided.
    notional_ccy : str, optional
        The ISO code of the notional currency.
        Should be explicitly specified if InstrumentCode hasn't been specified.
        May be retrieved from reference data.
    notional_amount : float, optional
        The notional amount of the term deposit at the start date.
        By default 1,000,000 is used.
    fixed_rate_percent : float, optional
        Fixed interest rate percent to be applied for notional by deal terms.
        Mandatory if instrument_code is None.
    payment_business_day_convention : BusinessDayConvention or str, optional
        The method to adjust dates to a working day.
        By default 'ModifiedFollowing'.
    payment_roll_convention : DateRollingConvention or str, optional
        Method to adjust payment dates when they fall at the end of the month.
        By default 'Last'.
    year_basis : DayCountBasis or str, optional
        The Day Count Basis method used to calculate the interest payments.
        By default 'Dcb_Actual_365'.
    calendar : str, optional
        Calendar used to adjust deposit duration calculation.
        By default the calendar corresponding to notional currency is used.
    interest_payment_frequency : Frequency or str, optional
        The interest payment frequency.
    interest_calculation_method : DayCountBasis or str, optional
        The day count basis method used to calculate the interest payments.
    """

    def __init__(
        self,
        *,
        instrument_tag: Optional[str] = None,
        instrument_code: Optional[str] = None,
        start_date: "OptDateTime" = None,
        end_date: "OptDateTime" = None,
        tenor: Optional[str] = None,
        notional_ccy: Optional[str] = None,
        notional_amount: Optional[float] = None,
        fixed_rate_percent: Optional[float] = None,
        payment_business_day_convention: Union[BusinessDayConvention, str] = None,
        payment_roll_convention: Union[DateRollingConvention, str] = None,
        year_basis: Union[DayCountBasis, str] = None,
        calendar: Optional[str] = None,
        interest_payment_frequency: Union[Frequency, str] = None,
        interest_calculation_method: Union[DayCountBasis, str] = None,
        payment_business_days: Optional[str] = None,
        start_tenor: Optional[str] = None,
    ):
        super().__init__()
        self.instrument_tag = instrument_tag
        self.instrument_code = instrument_code
        self.start_date = start_date
        self.end_date = end_date
        self.tenor = tenor
        self.notional_ccy = notional_ccy
        self.notional_amount = notional_amount
        self.fixed_rate_percent = fixed_rate_percent
        self.payment_business_day_convention = payment_business_day_convention
        self.payment_roll_convention = payment_roll_convention
        self.year_basis = year_basis
        self.calendar = calendar
        self.interest_payment_frequency = interest_payment_frequency
        self.interest_calculation_method = interest_calculation_method
        self.payment_business_days = payment_business_days
        self.start_tenor = start_tenor

    def get_instrument_type(self):
        return "TermDeposit"

    @property
    def payment_business_day_convention(self):
        """
        The method to adjust dates to a working day.
        The possible values are:
         - ModifiedFollowing (adjusts dates according to the Modified Following convention - next business day unless is it goes
         into the next month,
            preceeding is used in that  case),
         - NextBusinessDay (adjusts dates according to the Following convention - Next Business Day),
         - PreviousBusinessDay (adjusts dates  according to the Preceeding convention - Previous Business Day),
         - NoMoving (does not adjust dates),
         - BbswModifiedFollowing (adjusts dates  according to the BBSW Modified Following convention).
        Optional. In case an instrument code/style has been defined, value comes from bond reference data. Otherwise
        'ModifiedFollowing' is used.
        :return: enum BusinessDayConvention
        """
        return self._get_enum_parameter(BusinessDayConvention, "paymentBusinessDayConvention")

    @payment_business_day_convention.setter
    def payment_business_day_convention(self, value):
        self._set_enum_parameter(BusinessDayConvention, "paymentBusinessDayConvention", value)

    @property
    def payment_roll_convention(self):
        """
        Method to adjust payment dates when they fall at the end of the month (28th of February, 30th, 31st).
        The possible values are:
         - Last (For setting the calculated date to the last working day),
         - Same (For setting the calculated date to the same day . In this latter case, the date may be moved according to the date
         moving
            convention if it is a non-working day),
         - Last28 (For setting the calculated date to the last working day. 28FEB being always considered as the last working day),
         - Same28 (For setting the calculated date to the same day .28FEB being always considered as the last working day).
        Optional. In case an instrument code has been defined, value comes from bond reference data. Otherwise, 'SameDay' is used.
        :return: enum DateRollingConvention
        """
        return self._get_enum_parameter(DateRollingConvention, "paymentRollConvention")

    @payment_roll_convention.setter
    def payment_roll_convention(self, value):
        self._set_enum_parameter(DateRollingConvention, "paymentRollConvention", value)

    @property
    def year_basis(self):
        """
        The Day Count Basis method used to calculate the interest payments.
        Dcb_Actual_365 used by default.
        :return: enum DayCountBasis
        """
        return self._get_enum_parameter(DayCountBasis, "yearBasis")

    @year_basis.setter
    def year_basis(self, value):
        self._set_enum_parameter(DayCountBasis, "yearBasis", value)

    @property
    def calendar(self):
        """
        Calendar used to adjust deposit duration calculation.
        By default the calendar corresponding to notional currency is used.
        :return: str
        """
        return self._get_parameter("calendar")

    @calendar.setter
    def calendar(self, value):
        self._set_parameter("calendar", value)

    @property
    def end_date(self):
        """
        The maturity date of the term deposit contract.
        Mandatory.
        Either the endDate or the tenor must be provided.
        :return: str
        """
        return self._get_parameter("endDate")

    @end_date.setter
    def end_date(self, value):
        self._set_datetime_parameter("endDate", value)

    @property
    def fixed_rate_percent(self):
        """
        Fixed interest rate percent to be applied for notional by deal terms.
        E.g. "10" means 10%
        :return: float
        """
        return self._get_parameter("fixedRatePercent")

    @fixed_rate_percent.setter
    def fixed_rate_percent(self, value):
        self._set_parameter("fixedRatePercent", value)

    @property
    def instrument_code(self):
        """
        Code to define the term deposit instrument.
        For the moment, only RICs for CDs and Wholesales deposits are supported, with deposit code (ex:"EUR1MD=").
        :return: str
        """
        return self._get_parameter("instrumentCode")

    @instrument_code.setter
    def instrument_code(self, value):
        self._set_parameter("instrumentCode", value)

    @property
    def instrument_tag(self):
        """
        User defined string to identify the instrument.
        It can be used to link output results to the instrument definition.
        Only alphabetic, numeric and '- _.#=@' characters are supported.
        Optional.
        :return: str
        """
        return self._get_parameter("instrumentTag")

    @instrument_tag.setter
    def instrument_tag(self, value):
        self._set_parameter("instrumentTag", value)

    @property
    def notional_amount(self):
        """
        The notional amount of the term deposit at the start date.
        Optional.
        By default 1,000,000 is used.
        :return: float
        """
        return self._get_parameter("notionalAmount")

    @notional_amount.setter
    def notional_amount(self, value):
        self._set_parameter("notionalAmount", value)

    @property
    def notional_ccy(self):
        """
        The ISO code of the notional currency.
        Should be explicitly specified if InstrumentCode hasn't been specified.
        May be retrieved from reference data.
        :return: str
        """
        return self._get_parameter("notionalCcy")

    @notional_ccy.setter
    def notional_ccy(self, value):
        self._set_parameter("notionalCcy", value)

    @property
    def start_date(self):
        """
        The date the term deposit starts accruing interest. Its effective date.
        Optional. By default it is derived from the ValuationDate and the day to spot convention of the contract currency.
        :return: str
        """
        return self._get_parameter("startDate")

    @start_date.setter
    def start_date(self, value):
        self._set_datetime_parameter("startDate", value)

    @property
    def tenor(self):
        """
        The period code that represents the time between the start date and end date of the contract.
        Mandatory if instrumentCode is null.
        Either the endDate or the tenor must be provided.
        Sample value: 1M
        :return: str
        """
        return self._get_parameter("tenor")

    @tenor.setter
    def tenor(self, value):
        self._set_parameter("tenor", value)

    @property
    def interest_payment_frequency(self):
        return self._get_enum_parameter(Frequency, "interestPaymentFrequency")

    @interest_payment_frequency.setter
    def interest_payment_frequency(self, value):
        self._set_enum_parameter(Frequency, "interestPaymentFrequency", value)

    @property
    def interest_calculation_method(self):
        return self._get_enum_parameter(DayCountBasis, "interestCalculationMethod")

    @interest_calculation_method.setter
    def interest_calculation_method(self, value):
        self._set_enum_parameter(DayCountBasis, "interestCalculationMethod", value)

    @property
    def payment_business_days(self):
        return self._get_parameter("paymentBusinessDays")

    @payment_business_days.setter
    def payment_business_days(self, value):
        self._set_parameter("paymentBusinessDays", value)

    @property
    def start_tenor(self):
        return self._get_parameter("startTenor")

    @start_tenor.setter
    def start_tenor(self, value):
        self._set_parameter("startTenor", value)
