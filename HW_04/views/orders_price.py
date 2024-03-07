from flask import Blueprint
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from HW_04.database_handler import execute_query

order_price_route = Blueprint("order_price", __name__)


@order_price_route.route("/order_price")
@use_kwargs(
    {
        "country": fields.Str(
            missing=None, validate=validate.Regexp(regex="^[A-Za-z\s]*$")
        )
    },
    location="query",
)
def order_price(country: str = None) -> str:
    """
    This function returns the total sale amount for a given country,
    or for all countries if no specific country is provided.

    Parameters:
    country (str): The name of the country to filter by. If null or not provided, the function calculates data for all
    countries.

    Returns:
    str: A formatted string message with total sales amount for the given country or globally if no country
    was provided.
    """
    if country:
        query = f"""
                SELECT
                    c.Country,
                    ROUND(SUM(i.Quantity * i.UnitPrice), 2) AS TotalPurchaseValue
                FROM
                    invoice_items i
                    JOIN invoices i2 ON i.InvoiceId = i2.InvoiceId
                    JOIN main.customers c ON c.CustomerId = i2.CustomerId
                WHERE
                    c.Country = '{country}'
                GROUP BY
                    c.Country
                ORDER BY
                    TotalPurchaseValue DESC
                """
    else:
        query = """SELECT
                    COUNT(DISTINCT c.Country) AS NumberOfCountries,
                    ROUND(SUM(i.Quantity * i.UnitPrice), 2) AS TotalPurchaseValue
                FROM
                    invoice_items i
                    JOIN invoices i2 ON i.InvoiceId = i2.InvoiceId
                    JOIN main.customers c ON c.CustomerId = i2.CustomerId
                """
    result = execute_query(query=query)
    if not result:
        return f"There are no sales in {country}"
    if country:
        return f"Total sales for {country} are ${result[0][1]}"
    else:
        return f"Total sales for the {result[0][0]} countries are ${result[0][1]}"
