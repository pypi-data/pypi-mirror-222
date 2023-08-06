# coding: utf8

from .._object_definition import ObjectDefinition
from ...._tools import try_copy_to_list
from ...._types import OptStr, OptStrings, OptDateTime


class ForwardCurveDefinition(ObjectDefinition):
    """
    Parameters
    ----------
    index_tenor : str, optional

    forward_curve_tenors : list of str, optional
        Defines expected forward rate surface tenor/slices
    forward_curve_tag : str, optional

    forward_start_date : str or date or datetime or timedelta, optional
        Defines the forward start date by date format
    forward_start_tenor : str, optional
        Defines the forward start date by tenor format: "Spot" / "1M" / ...
    """

    def __init__(
        self,
        index_tenor: OptStr = None,
        forward_curve_tag: OptStr = None,
        forward_curve_tenors: OptStrings = None,
        forward_start_date: "OptDateTime" = None,
        forward_start_tenor: OptStr = None,
    ) -> None:
        super().__init__()
        self.index_tenor = index_tenor
        self.forward_curve_tenors = try_copy_to_list(forward_curve_tenors)
        self.forward_curve_tag = forward_curve_tag
        self.forward_start_date = forward_start_date
        self.forward_start_tenor = forward_start_tenor

    @property
    def forward_curve_tenors(self):
        """
        Defines expected forward rate surface tenor/slices
        :return: list string
        """
        return self._get_list_parameter(str, "forwardCurveTenors")

    @forward_curve_tenors.setter
    def forward_curve_tenors(self, value):
        self._set_list_parameter(str, "forwardCurveTenors", value)

    @property
    def forward_curve_tag(self):
        """
        :return: str
        """
        return self._get_parameter("forwardCurveTag")

    @forward_curve_tag.setter
    def forward_curve_tag(self, value):
        self._set_parameter("forwardCurveTag", value)

    @property
    def forward_start_date(self):
        """
        Defines the forward start date by date format
        :return: str
        """
        return self._get_parameter("forwardStartDate")

    @forward_start_date.setter
    def forward_start_date(self, value):
        self._set_date_parameter("forwardStartDate", value)

    @property
    def forward_start_tenor(self):
        """
        Defines the forward start date by tenor format: "Spot" / "1M" / ...
        :return: str
        """
        return self._get_parameter("forwardStartTenor")

    @forward_start_tenor.setter
    def forward_start_tenor(self, value):
        self._set_parameter("forwardStartTenor", value)

    @property
    def index_tenor(self):
        """
        :return: str
        """
        return self._get_parameter("indexTenor")

    @index_tenor.setter
    def index_tenor(self, value):
        self._set_parameter("indexTenor", value)
