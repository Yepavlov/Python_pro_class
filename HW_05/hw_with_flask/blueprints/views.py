from flask import Blueprint
from webargs import fields
from webargs.flaskparser import use_kwargs

from HW_05.hw_with_flask.utils.database_handler import execute_query

city_by_genre_blueprint = Blueprint("city_by_genre", __name__)


@city_by_genre_blueprint.route("/get-city-by-genre")
@use_kwargs({"genre": fields.Str(required=True)}, location="query")
def get_city_by_genre(genre: str):
    query = f"""
            WITH CityRank AS 
                (SELECT 
                    g.Name as GenreName, 
                    COUNT(i.CustomerId) as CustomerTotal, 
                    i.BillingCity,
                    DENSE_RANK() OVER (ORDER BY COUNT(i.CustomerId) DESC) as CityRank
                FROM invoices i 
                LEFT JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId 
                LEFT JOIN tracks t ON ii.TrackId = t.TrackId 
                LEFT JOIN genres g ON t.GenreId = g.GenreId 
                WHERE g.Name = ?
                GROUP BY i.BillingCity)
            SELECT BillingCity
            FROM CityRank
            WHERE CityRank = 1
            """
    response = execute_query(query=query, args=(genre,))
    cities = [city[0] for city in response]
    if cities:
        return (
            f"The city(s) with the highest number of customers who listen to music "
            f"in the {genre} genre is (are): {', '.join(cities)}."
        )
    else:
        return f"No data found for the {genre} genre."


@city_by_genre_blueprint.errorhandler(422)
def handle_validation_error(err):
    messages = getattr(err, "data", {}).get("messages", {})
    if "genre" not in messages:
        return "Genre is a required parameter!"
