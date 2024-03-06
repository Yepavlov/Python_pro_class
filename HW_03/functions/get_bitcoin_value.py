from http import HTTPStatus
from typing import Union
import requests
from flask import Response, Blueprint, render_template
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

get_bitcoin_value_route = Blueprint("get_bitcoin_value", __name__)
URL_BITCOIN = "https://bitpay.com/api/rates"
URL_CURRENCY_SYMBOL = "https://test.bitpay.com/currencies"


@get_bitcoin_value_route.route("/get-bitcoin-value")
@use_kwargs(
    {
        "currency": fields.Str(missing="USD", validate=validate.Regexp(r"^[A-Z]+$")),
        "amount": fields.Int(missing=1),
    },
    location="query",
)
def get_bitcoin_value(currency: str, amount: int) -> Union[str, Response]:
    """
    Get the value of a specified amount in Bitcoin based on the given currency.

    Parameters:
    - currency (str): The currency code (e.g., USD, EUR).
    - amount (int): The amount to convert to Bitcoin.

    Returns:
    - str: HTML content rendered from the template ("result_bitcoin.html") with the result of the conversion
    rounded to two decimal places.
    """
    response = send_get_request(URL_BITCOIN)
    bitcoin_value = get_bitcoin_in_currency(currency, response)
    if bitcoin_value is not None:
        result = count_bitcoin_mount_in_currency(bitcoin_value, amount)
        symbol = get_currency_symbol(currency)
        return render_template(
            "result_bitcoin.html",
            amount=amount,
            currency=currency,
            result=result,
            symbol=symbol,
        )
    else:
        return Response("ERROR: Currency not found", status=HTTPStatus.NOT_FOUND)


def send_get_request(url: str) -> Union[dict, Response]:
    """
    Send an HTTP GET request to the specified URL.

    Parameters:
    - url (str): The URL to send the GET request to.

    Returns:
    - dict: The JSON response.
    """
    response = requests.get(url)
    if response.status_code not in (
        HTTPStatus.OK,
        HTTPStatus.CREATED,
        HTTPStatus.ACCEPTED,
        HTTPStatus.TOO_MANY_REQUESTS,
    ):
        return Response("ERROR: something went wrong", status=response.status_code)
    return response.json()


def get_bitcoin_in_currency(
    user_currency: str, response: dict
) -> Union[int, float, None]:
    """
    Get the Bitcoin value in the specified currency from the API response.

    Parameters:
    - user_currency (str): The currency code (e.g., USD, EUR).
    - response (dict): The API response containing currency rates.

    Returns:
    - Union[int, float, None]: The Bitcoin value in the specified currency or None if not found.
    """
    user_currency_dict = next(
        (currency for currency in response if currency["code"] == user_currency), None
    )
    return user_currency_dict["rate"] if user_currency_dict is not None else None


def count_bitcoin_mount_in_currency(
    bitcoin_value: Union[float, int], amount: int
) -> str:
    """
    Count the Bitcoin amount in the specified currency.

    Parameters:
    - bitcoin_value (Union[float, int]): The value of "1" Bitcoin in the specified currency.
    - amount (Union[float, int]): The amount to convert to Bitcoin.

    Returns:
    - str: The result of the conversion rounded to two decimal places.
    """
    result = round((bitcoin_value * amount), 2)
    return str(result)


def get_currency_symbol(user_currency: str) -> str:
    """
    Get the currency symbol for a given currency code.

    Parameters:
    - user_currency (str): The currency code for which the symbol is to be retrieved.

    Returns:
    - str: The currency symbol if found, or an empty string if the currency code is not present in the response.
    """
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Accept-Version": "2.0.0",
    }
    response = requests.get(URL_CURRENCY_SYMBOL, headers=headers).json()
    user_currency_dict = next(
        (
            currency
            for currency in response["data"]
            if currency["code"] == user_currency
        ),
        None,
    )
    return user_currency_dict["symbol"] if user_currency_dict is not None else None
