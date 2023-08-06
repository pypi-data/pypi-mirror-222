# coding: utf8

from typing import Optional, Union

from refinitiv.data._types import OptDateTime
from .._base import Info
from .._enums import (
    AverageType,
    FixingFrequency,
)


class EtiFixingInfo(Info):
    """
    Parameters
    ----------
    average_type : AverageType or str, optional
        The type of average used to compute.
    fixing_frequency : FixingFrequency or str, optional
        The fixing's frequency.
    average_so_far : float, optional
        The value of the average_type
    fixing_calendar : str, optional
        The calendar of the underlying's currency.
    fixing_end_date : str or date or datetime or timedelta, optional
        The end date of the fixing period. Should be less or equal to the expiry.
    fixing_start_date : str or date or datetime or timedelta, optional
        The beginning date of the fixing period.
    include_holidays : bool, optional
        Include the holidays in the list of fixings
    include_week_ends : bool, optional
        Include the week-ends in the list of fixings
    """

    def __init__(
        self,
        average_type: Union[AverageType, str] = None,
        fixing_frequency: Union[FixingFrequency, str] = None,
        average_so_far: Optional[float] = None,
        fixing_calendar: Optional[str] = None,
        fixing_end_date: "OptDateTime" = None,
        fixing_start_date: "OptDateTime" = None,
        include_holidays: Optional[bool] = None,
        include_week_ends: Optional[bool] = None,
    ) -> None:
        super().__init__()
        self.average_type = average_type
        self.fixing_frequency = fixing_frequency
        self.average_so_far = average_so_far
        self.fixing_calendar = fixing_calendar
        self.fixing_end_date = fixing_end_date
        self.fixing_start_date = fixing_start_date
        self.include_holidays = include_holidays
        self.include_week_ends = include_week_ends

    @property
    def average_type(self):
        """
        The type of average used to compute. Possible values:
        - ArithmeticRate
        - ArithmeticStrike
        - GeometricRate
        - GeometricStrike
        :return: enum AverageType
        """
        return self._get_enum_parameter(AverageType, "averageType")

    @average_type.setter
    def average_type(self, value):
        self._set_enum_parameter(AverageType, "averageType", value)

    @property
    def fixing_frequency(self):
        """
        The fixing's frequency. Possible values:
        - Daily
        - Weekly
        - BiWeekly
        - Monthly
        - Quaterly
        - SemiAnnual
        - Annual
        :return: enum FixingFrequency
        """
        return self._get_enum_parameter(FixingFrequency, "fixingFrequency")

    @fixing_frequency.setter
    def fixing_frequency(self, value):
        self._set_enum_parameter(FixingFrequency, "fixingFrequency", value)

    @property
    def average_so_far(self):
        """
        The value of the average_type
        :return: float
        """
        return self._get_parameter("averageSoFar")

    @average_so_far.setter
    def average_so_far(self, value):
        self._set_parameter("averageSoFar", value)

    @property
    def fixing_calendar(self):
        """
        The calendar of the underlying's currency.
        :return: str
        """
        return self._get_parameter("fixingCalendar")

    @fixing_calendar.setter
    def fixing_calendar(self, value):
        self._set_parameter("fixingCalendar", value)

    @property
    def fixing_end_date(self):
        """
        The end date of the fixing period. Should be less or equal to the expiry.
        :return: str
        """
        return self._get_parameter("fixingEndDate")

    @fixing_end_date.setter
    def fixing_end_date(self, value):
        self._set_datetime_parameter("fixingEndDate", value)

    @property
    def fixing_start_date(self):
        """
        The beginning date of the fixing period.
        :return: str
        """
        return self._get_parameter("fixingStartDate")

    @fixing_start_date.setter
    def fixing_start_date(self, value):
        self._set_datetime_parameter("fixingStartDate", value)

    @property
    def include_holidays(self):
        """
        Include the holidays in the list of fixings
        :return: bool
        """
        return self._get_parameter("includeHolidays")

    @include_holidays.setter
    def include_holidays(self, value):
        self._set_parameter("includeHolidays", value)

    @property
    def include_week_ends(self):
        """
        Include the week-ends in the list of fixings
        :return: bool
        """
        return self._get_parameter("includeWeekEnds")

    @include_week_ends.setter
    def include_week_ends(self, value):
        self._set_parameter("includeWeekEnds", value)
