from flask import Blueprint, render_template
from webargs import fields
from webargs.flaskparser import use_kwargs

from HW_04.database_handler import execute_query

tracks_info_route = Blueprint("tracks_info_route", __name__)


@tracks_info_route.route("/tracks_info")
@use_kwargs({"track_id": fields.Int(missing=None)}, location="query")
def get_tracks_info(track_id: int = None) -> str:
    if track_id:
        query = f"""
        SELECT
            t.TrackId,
            t.Name AS TrackName,
            t.Composer,
            t.Milliseconds,
            t.Bytes,
            t.UnitPrice,
            COUNT(distinct i2.CustomerId) AS NumberOfCustomers,
            ROUND(SUM(i.UnitPrice * i.Quantity), 2) AS TotalSales,
            g.Name AS GenreName,
            m.Name AS MediaTypeName,
            a.Title AS TitleName,
            ar.Name AS ArtistName,
            pl.Name AS PlaylistName
        FROM
            tracks t
            LEFT JOIN invoice_items i ON t.TrackId = i.TrackId
            LEFT JOIN invoices i2 ON i.InvoiceId = i2.InvoiceId
            LEFT JOIN customers c ON i2.CustomerId = c.CustomerId
            LEFT JOIN genres g ON t.GenreId = g.GenreId
            LEFT JOIN media_types m ON t.MediaTypeId = m.MediaTypeId
            LEFT JOIN albums a ON t.AlbumId = a.AlbumId
            LEFT JOIN artists ar ON a.ArtistId = ar.ArtistId
            LEFT JOIN playlist_track pt ON t.TrackId = pt.TrackId
            LEFT JOIN playlists pl ON pt.PlaylistId = pl.PlaylistId
        WHERE t.TrackId = {track_id}
        GROUP BY
            t.TrackId;
        """
    else:
        query = f"""
        SELECT
            t.TrackId,
            t.Name AS TrackName,
            t.Composer,
            t.Milliseconds,
            t.Bytes,
            t.UnitPrice,
            COUNT(distinct i2.CustomerId) AS NumberOfCustomers,
            ROUND(SUM(i.UnitPrice * i.Quantity), 2) AS TotalSales,
            g.Name AS GenreName,
            m.Name AS MediaTypeName,
            a.Title AS TitleName,
            ar.Name AS ArtistName,
            pl.Name AS PlaylistName
        FROM
            tracks t
            LEFT JOIN invoice_items i ON t.TrackId = i.TrackId
            LEFT JOIN invoices i2 ON i.InvoiceId = i2.InvoiceId
            LEFT JOIN customers c ON i2.CustomerId = c.CustomerId
            LEFT JOIN genres g ON t.GenreId = g.GenreId
            LEFT JOIN media_types m ON t.MediaTypeId = m.MediaTypeId
            LEFT JOIN albums a ON t.AlbumId = a.AlbumId
            LEFT JOIN artists ar ON a.ArtistId = ar.ArtistId
            LEFT JOIN playlist_track pt ON t.TrackId = pt.TrackId
            LEFT JOIN playlists pl ON pt.PlaylistId = pl.PlaylistId
        GROUP BY
            t.TrackId;
        """
    result = execute_query(query=query)
    if not result:
        return f"There is no track_id as {track_id}"
    if track_id:
        return render_template("track_info.html", track_info=result[0])
    else:
        return render_template("all_tracks_info.html", all_tracks_info=result)
