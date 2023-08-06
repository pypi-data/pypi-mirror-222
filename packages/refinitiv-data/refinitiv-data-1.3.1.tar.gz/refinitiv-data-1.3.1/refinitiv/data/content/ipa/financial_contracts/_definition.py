# coding: utf8

from typing import Optional, List, TYPE_CHECKING, Any, Union

from ._base_definition import BaseDefinition
from ._base_definition import FCBaseDefinition
from ...._tools import create_repr, iterable, try_copy_to_list

if TYPE_CHECKING:
    from .._object_definition import ObjectDefinition
    from ...._types import OptStrStrs


def validate_universe(universe: Any) -> None:
    validate = True
    if iterable(universe):
        for item in universe:
            validate = isinstance(item, BaseDefinition)
            if not validate:
                break

    else:
        validate = isinstance(universe, BaseDefinition)

    if not validate:
        raise TypeError(
            f"Provided type for parameter 'universe' is invalid. "
            f"Expected types: "
            f"[bond.Definition, cap_floor.Definition, cds.Definition, "
            f"cross.Definition, option.Definition, repo.Definition, "
            f"swap.Definition, swaption.Definition, term_deposit.Definition]"
        )


DefnDefns = Union[BaseDefinition, List[BaseDefinition]]


class Definitions(FCBaseDefinition):
    """
    API endpoint for Financial Contract analytics,
    that returns calculations relevant to each contract type.

    Parameters
    ----------
    universe : list
        Array of Financial Contract definitions.
    fields: list of str, optional
        Array of requested fields. each requested field will represent
        a column of the tabular response. By default all relevant fields
        are returned.
    pricing_parameters : PricingParameters, optional
        Pricing parameters that are specific to the financial contracts
        defined in universe.

    Methods
    -------
    get_data(session=session, on_response=on_response, async_mode=None)
        Returns a response to the data platform
    get_data_async(session=session, on_response=on_response, async_mode=None)
        Returns a response to the async data platform

    Examples
    --------
     >>> import refinitiv.data.content.ipa.financial_contracts as rdf
     >>> option_definition = rdf.option.Definition(
     ...     instrument_code="FCHI560000L1.p",
     ...     underlying_type=rdf.option.UnderlyingType.ETI,
     ...     fields=[
     ...         "MarketValueInDealCcy",
     ...         "DeltaPercent",
     ...         "GammaPercent",
     ...         "RhoPercent",
     ...         "ThetaPercent",
     ...         "VegaPercent",
     ...         "ErrorCode",
     ...         "ErrorMessage",
     ...     ],
     ... )
     >>> bond_definition = rdf.bond.Definition(
     ...     issue_date="2002-02-28",
     ...     end_date="2032-02-28",
     ...     notional_ccy="USD",
     ...     interest_payment_frequency="Annual",
     ...     fixed_rate_percent=7,
     ...     interest_calculation_method=rdf.bond.DayCountBasis.DCB_ACTUAL_ACTUAL
     ... )
     >>> definition = rdf.Definitions(
     ...    [
     ...        bond_definition,
     ...        option_definition
     ...    ]
     ... )
     >>> response = definition.get_data()
    """

    def __init__(
        self,
        universe: "DefnDefns",
        fields: "OptStrStrs" = None,
        pricing_parameters: Optional["ObjectDefinition"] = None,
    ) -> None:
        validate_universe(universe)
        universe = try_copy_to_list(universe)
        fields = try_copy_to_list(fields)
        if not isinstance(universe, list):
            universe = [universe]
        super().__init__(
            universe=universe,
            fields=fields,
            pricing_parameters=pricing_parameters,
            __plural__=True,
        )

    def __repr__(self):
        return create_repr(self)
