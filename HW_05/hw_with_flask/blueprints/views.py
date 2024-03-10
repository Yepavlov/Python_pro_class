from flask import Blueprint
from webargs import fields
from webargs.flaskparser import use_kwargs

from HW_05.hw_with_flask.utils.database_handler import execute_query
from HW_05.hw_with_flask.utils.return_cities_by_genre import return_cities_by_genre

city_by_genre_blueprint = Blueprint("city_by_genre", __name__)


@city_by_genre_blueprint.route("/get-city-by-genre")
@use_kwargs({"genre": fields.Str(required=True)}, location="query")
def get_city_by_genre(genre: str):
    query = f"""
            SELECT g.Name as GenreName, COUNT(i.CustomerId) as CustomerTotal, i.BillingCity  
            FROM invoices i 
            LEFT JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId 
            LEFT JOIN tracks t ON ii.TrackId = t.TrackId 
            LEFT JOIN genres g ON t.GenreId = g.GenreId 
            WHERE g.Name = ?
            GROUP BY i.BillingCity
            ORDER BY CustomerTotal DESC, i.BillingCity ASC
            """
    response = execute_query(query=query, args=(genre,))
    result = return_cities_by_genre(response)
    cities = [city[2] for city in result]
    return (
        f"The city(s) with the highest number of customers who listen to music "
        f"in the {genre} genre is (are): {cities}"
    )


@city_by_genre_blueprint.errorhandler(422)
def handle_validation_error(err):
    messages = getattr(err, "data", {}).get("messages", {})
    if "genre" not in messages:
        return "Genre is a required parameter!"
