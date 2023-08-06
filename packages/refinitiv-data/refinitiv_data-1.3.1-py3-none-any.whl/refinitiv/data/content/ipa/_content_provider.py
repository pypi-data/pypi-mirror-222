from typing import Union, Any

import numpy as np
import pandas as pd
from numpy import iterable

from ._enums import Axis
from ._object_definition import ObjectDefinition
from ...delivery._data._data_provider import RequestFactory
from ...delivery.endpoint_request import RequestMethod
from ..._tools._common import ArgsParser, merge_dict_to_dict

types_by_axis = {
    Axis.DATE: "datetime64",
    "startDate": "datetime64",
    "endDate": "datetime64",
    Axis.DELTA: float,
    Axis.EXPIRY: float,
    Axis.MONEYNESS: float,
    Axis.STRIKE: float,
    Axis.TENOR: float,
    "discountFactor": float,
    "ratePercent": float,
}


def get_type_by_axis(axis):
    axis_values_type = types_by_axis.get(axis)

    if not axis_values_type:
        raise ValueError(f"Cannot find axis's values type for axis {axis}.")

    return axis_values_type


def parse_value(value: Any) -> Union[float, int, np.datetime64]:
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            pass
        else:
            return value

        try:
            value = pd.to_datetime(value).to_numpy()
        except ValueError:
            try:
                value = pd.to_datetime(value, dayfirst=True).to_numpy()
            except ValueError:
                pass
        else:
            return value

        try:
            value = float(value)
        except ValueError:
            raise ValueError(f"not valid format: {value}")

    return value


value_arg_parser = ArgsParser(parse_value)
x_arg_parser = value_arg_parser
y_arg_parser = value_arg_parser


# ---------------------------------------------------------------------------
#   RequestFactory
# ---------------------------------------------------------------------------


def parse_universe(universe):
    retval = []

    if not iterable(universe):
        universe = [universe]

    # convert universe's objects into json
    for i, item in enumerate(universe):
        extended_params = None
        if not hasattr(item, "get_dict"):
            kwargs = item._kwargs
            item = kwargs.get("universe")
            extended_params = kwargs.get("extended_params")
        item_dict = item.get_dict()
        if extended_params:
            item_dict.update(extended_params)
        retval.append(item_dict)

    return retval


def parse_outputs(outputs):
    retval = []

    if not isinstance(outputs, list):
        outputs = [outputs]

    for item in outputs:
        if hasattr(item, "value"):
            item = item.value

        retval.append(item)

    return retval


universe_arg_parser = ArgsParser(parse_universe)
outputs_arg_parser = ArgsParser(parse_outputs)


class CurvesAndSurfacesRequestFactory(RequestFactory):
    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if not extended_params:
            return body_parameters

        if kwargs.get("__plural__") is True:
            body_parameters.update(extended_params)
            return body_parameters

        universes = body_parameters.get("universe", [{}])
        universes[0] = merge_dict_to_dict(universes[0], extended_params)
        return body_parameters

    def get_request_method(self, *, method=None, **kwargs):
        return method or RequestMethod.POST

    def get_body_parameters(self, *args, universe=None, outputs=None, **kwargs):
        body_parameters = {}

        # universe
        universe = universe_arg_parser.get_list(universe)
        body_parameters["universe"] = universe

        # outputs
        if outputs:
            outputs = outputs_arg_parser.get_list(outputs)
            body_parameters["outputs"] = outputs

        return body_parameters


class CrossCurrencyCurvesDefinitionsRequestFactory(RequestFactory):
    def get_request_method(self, *, method=None, **kwargs):
        return method or RequestMethod.POST

    def get_body_parameters(self, *args, request_items: ObjectDefinition, **kwargs):
        if isinstance(request_items, ObjectDefinition):
            result = request_items.get_dict()
            return result
        return {}

    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if extended_params:
            result = dict(body_parameters)
            result.update(extended_params)
            return result
        return body_parameters


class DatesAndCalendarsRequestFactory(RequestFactory):
    def get_request_method(self, *, method=None, **kwargs):
        return method or RequestMethod.POST

    def get_body_parameters(self, *args, universe, **kwargs):
        body_parameters = []
        for request_item in universe:
            body_parameters.append(request_item.get_dict())
        return body_parameters

    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if extended_params:
            if isinstance(extended_params, list):
                for idx, extended_param_item in enumerate(extended_params):
                    if extended_param_item:
                        body_parameters[idx].update(extended_param_item)
            else:
                for item in body_parameters:
                    item.update(extended_params)
        return body_parameters


class DateScheduleRequestFactory(RequestFactory):
    def get_request_method(self, *, method=None, **kwargs):
        return method or RequestMethod.POST

    def get_body_parameters(self, *args, universe, **kwargs):
        return universe.get_dict()

    def extend_body_parameters(self, body_parameters, extended_params=None, **kwargs):
        if extended_params:
            body_parameters.update(extended_params)
        return body_parameters
